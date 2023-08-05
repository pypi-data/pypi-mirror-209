#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/8 下午7:16
# @Author : gyw
# @File : agi_py_repo
# @ description:
import re
import pickle
import math
import time
import shutil
import os.path

from tqdm import tqdm
import numpy as np
from typing import List
from deep_copilot.ocr_tools.ocr_tools import ocr
from deep_copilot.date_tools.datetimeutil import second_to_hms
from deep_copilot.video_and_image_tools.base_video_tools import generate_key_frame
from deep_copilot.string_tools.string_copilot import remain_ch_en_number
from deep_copilot.video_and_image_tools.base_video_tools import generate_video_frames, VideoFrame
from deep_copilot.video_and_image_tools.base_image_tools import get_pictures_feature
from deep_copilot.string_tools.string_copilot import remove_blank, get_uuid_str
from deep_copilot.date_tools.datetimeutil import hms_to_second
from deep_copilot.faiss_tools.faiss_tools import build_search_engine, search_with_engine
from deep_copilot.log_tools.log_tool import logger


class FramePair(object):
    def __init__(self, source_frame: VideoFrame, reference_frame: VideoFrame, score):
        """
        视频帧对
        :param source_frame:原始视频帧
        :param reference_frame:参考视频帧
        :param score:
        """
        self.source_frame = source_frame
        self.reference_frame = reference_frame
        self.score = score
        self.offset = source_frame.frame_index - reference_frame.frame_index

    def __str__(self):
        return f"score {self.score}, offset {self.offset},source frame {str(self.source_frame)} reference frame {str(self.reference_frame)}"


def generate_video_frames_feature(video_frames: List[VideoFrame], model_name):
    """
    为影片的每一帧生成对应的 tensor
    :param video_frames:
    :return:
    """
    logger.info(f"begin to generate video feature")
    batch_size = 8
    batch_list = list(zip(*(iter(video_frames),) * batch_size))
    index = len(video_frames) % batch_size
    if index != 0:
        left = video_frames[-index:]
        batch_list.append(left)
    for video_frames in tqdm(batch_list):
        frame_paths = [video_frame.frame_path for video_frame in video_frames]
        frames_feature = get_pictures_feature(frame_paths, model_name=model_name)
        for video_frame, frame_feature in zip(video_frames, frames_feature):
            video_frame.frame_feature[model_name] = frame_feature


def video_match_pairs_func(source_video_frames, reference_videos_frames, model_name):
    """

    :param source_video_frames:
    :param reference_videos_frames:
    :return:
    """
    source_video_tensors = [video_frame.frame_feature[model_name]
                            for video_frame in source_video_frames]
    all_reference_frame_pair = []
    for reference_video_frames in reference_videos_frames:
        reference_video_tensors = [video_frame.frame_feature[model_name]
                                   for video_frame in reference_video_frames]
        reference_video_engine = build_search_engine(reference_video_tensors)
        search_results = search_with_engine(source_video_tensors, reference_video_engine, 0.95)
        one_reference_frame_pairs = []
        for source_frame, search_result in zip(source_video_frames, search_results):
            if search_result:
                reference_frame_index, score = search_result[0]  # 如果有多个，选取第一个
                reference_frame = reference_video_frames[reference_frame_index]
                frame_pair = FramePair(source_frame, reference_frame, score)
                one_reference_frame_pairs.append(frame_pair)
        all_reference_frame_pair.append(one_reference_frame_pairs)
    return all_reference_frame_pair


def video_pairs_group_by_offsets(video_match_pairs: List[FramePair]):
    """
    分组是为了将时间点的匹配变成时间区间的匹配
    这里的困难在于时间点匹配结果不是完全正确的，因此需要设计一些适应性的算法进行检索

    这里设计的算法是分组，目的是将相似的偏移量合并到一组
    比如 {1，2} {3，4} {20，26} {21，27} 这四对
    需要将 {1，2} {3，4} 作为一组  {20,26} {21，27} 作为另一组
    但是考虑到相似帧匹配结果不完全准确，可能还会有 {12，14} 这些扰动项，需要设计兼容算法

    设计两个阈值，偏移量的相差阈值 offset_by_pair_offset_threshold  和相邻区间合并阈值 neighbour_time_threshold
    让相对帧对之间的 offset 的两两差值控制在一定区间内 offset_by_pair_offset_threshold ，表示可能位于同一区间
    在将筛选出来的相似帧进行排序
    对排序后的相似帧进行相邻区间合并操作

    :param video_match_pairs: 视频帧对列表
    :return:
    """

    offset_by_pair_offset_threshold = 2  # 偏移量是这里是依据 frame index 进行计算
    neighbour_time_threshold = 2  # 预设 2s 就不属于连续时间片段
    regions = []  # source 的 区间
    groups = []
    group = []
    pair_offsets = np.array([frame_pair.offset for frame_pair in video_match_pairs])
    # 偏移量之间的差值 其中 offsets_by_pair_offset[i][j]=pair_offsets[i]-pair_offsets[j]
    offsets_by_pair_offset = pair_offsets[:, np.newaxis] - pair_offsets[np.newaxis, :]
    abs_offsets_by_pair_offset = np.abs(offsets_by_pair_offset)
    # x_positions , y_positions 是指 视频帧对index
    # 当两个视频帧对i,j偏移量的差值小于一定阈值，就放入候选匹配视频帧对，这些有可能构成重合区间
    x_positions, y_positions = np.where(abs_offsets_by_pair_offset <= offset_by_pair_offset_threshold)
    all_useful_positions = set()
    for x_position, y_position in zip(x_positions, y_positions):
        if x_position == y_position:
            continue
        all_useful_positions.update({x_position, y_position})
    candidate_frame_pairs = [video_match_pairs[position] for position in all_useful_positions]
    # 将候选视频帧对按照源视频的帧的顺序排列
    candidate_frame_pairs = sorted(candidate_frame_pairs, key=lambda x: [x.source_frame.frame_index])
    if not candidate_frame_pairs:
        return regions
    last_source_time = hms_to_second(candidate_frame_pairs[0].source_frame.frame_time)
    for pair in candidate_frame_pairs:
        source_frame_time = hms_to_second(pair.source_frame.frame_time)
        if source_frame_time - last_source_time < neighbour_time_threshold:
            group.append(pair)
        else:
            groups.append(group[:])
            group = [pair]
        last_source_time = source_frame_time
    if group:
        groups.append(group[:])
    for group in groups:
        min_source_pair = min(group, key=lambda x: x.source_frame.frame_index)
        max_source_pair = max(group, key=lambda x: x.source_frame.frame_index)
        source_region_begin = min_source_pair.source_frame.frame_time
        source_region_end = max_source_pair.source_frame.frame_time
        source_region = hms_to_second(source_region_end) - hms_to_second(source_region_begin)

        # fix 参考剧集的位置需要进一步 调整， 因为 可能 原始剧集同多个位置的参考剧集合并
        # 过滤掉不合理的参考剧集数据
        candidate_references = sorted([x.reference_frame for x in group], key=lambda x: x.frame_index)
        groups_references = []
        one_group = []
        last_reference_time = hms_to_second(candidate_references[0].frame_time)

        for reference_frame in candidate_references:
            reference_frame_time = hms_to_second(reference_frame.frame_time)
            if reference_frame_time - last_reference_time < neighbour_time_threshold:
                one_group.append(reference_frame)
            else:
                groups_references.append(one_group[:])
                one_group = [reference_frame]
            last_reference_time = reference_frame_time
        if one_group:
            groups_references.append(one_group[:])

        for one_group in groups_references:
            min_ref_pair = min(one_group, key=lambda x: x.frame_index)
            max_ref_pair = max(one_group, key=lambda x: x.frame_index)
            ref_region_begin = min_ref_pair.frame_time
            ref_region_end = max_ref_pair.frame_time
            ref_region = hms_to_second(ref_region_end) - hms_to_second(ref_region_begin)
            if ref_region / 3 < source_region < 3 * ref_region or ref_region < 0.5:  # 有时候ref的区间很小，因为静态画面
                regions.append([source_region_begin, source_region_end])
    return regions


def merge_and_ranking_regions_for_beginning(regions, neighbour_time_threshold=2):
    """
    对于一个待处理的 source video，利用多种手段找到其候选重合区间后，
    如何针对这些区间进行合并和排序
    排序权重为
    合并区间占总区间的比例的和
    具体为
    存在如下区间
    region1 = [0,1] [3,5]
    region2 = [3,4] [7,8]

    合并并排序后的区间为 regions3 = [3,5] [0,1] [7,8] 这里[3,5]在前面，是因为它由两个区间合并而来，并且交并比最高
    所以可以利用 region3 的各区间 在不同 regions 里的计数作为排序得分
    优化2
    只考虑占比貌似也有问题，因为有的转场画面会在很多的剧集里出现，
    :param regions: [(begin_hms,end_hms)]
    :return:
    """
    reference_num = len(regions)
    flat_regions = [one_reference_region for one_reference_regions in regions for one_reference_region in
                    one_reference_regions]
    flat_regions = list(sorted(flat_regions, key=lambda x: hms_to_second(x[0])))
    merged_regions = []
    for region in flat_regions:
        if merged_regions:
            last_region = merged_regions[-1]
            # 如果区间当前的区间左侧小于上一个区间的右侧+neighbour_time_threshold 则进行融合
            if hms_to_second(region[0]) - hms_to_second(last_region[1]) < neighbour_time_threshold:
                # 如果当前区间右侧小于上一个区间右侧，则进行选择上一区间
                if hms_to_second(region[1]) < hms_to_second(last_region[1]):
                    pass
                else:
                    # 否则，选择当前区间的右侧
                    last_region[1] = region[1]
            else:
                merged_regions.append(region)
        else:
            merged_regions.append(region)
    filter_merged_regions = []
    for merged_region in merged_regions:
        if hms_to_second(merged_region[1]) - hms_to_second(merged_region[0]) < 2:
            continue
        else:
            filter_merged_regions.append(merged_region)
    merged_regions = filter_merged_regions
    scores = [0 for _ in merged_regions]
    score_limit = set()  # 每个参考视频对每个候选区间只允许一个投票，出现多个情形仅考虑到
    merged_regions_seconds = [[hms_to_second(region[0]), hms_to_second(region[1])] for region in merged_regions]
    # print(merged_regions)
    for reference_index, one_reference_regions in enumerate(regions):
        for one_reference_region in one_reference_regions:
            one_reference_region_begin = hms_to_second(one_reference_region[0])
            one_reference_region_end = hms_to_second(one_reference_region[1])
            for region_index, merged_region in enumerate(merged_regions_seconds):
                # 如果参考视频对该区间已经投过票了，则不允许再次投票
                if f"{reference_index}_{region_index}" in score_limit:
                    continue
                if one_reference_region_begin >= merged_region[0] and \
                        one_reference_region_end <= merged_region[1]:
                    scores[region_index] += 1
                    score_limit.add(f"{reference_index}_{region_index}")
                    break
    zipped = sorted(zip(merged_regions, scores),
                    key=lambda x: [math.fabs(x[1] - reference_num), hms_to_second(x[0][0])])
    if not zipped:
        return []
    sorted_merged_regions, sorted_scores = zip(*zipped)
    return sorted_merged_regions


def generate_video_frames_info_by_video_path(video_path, frame_dir, model_name, interval=1, video_id=None):
    """
    根据视频文件，拆帧 并 生成对应特征
    :param video_path:
    :param frame_dir:
    :param model_name:
    :param interval:
    :param video_id:
    :return:
    """
    name, ext = os.path.splitext(os.path.basename(video_path))
    name = remove_blank(name)
    tmp_frame_dir = os.path.join(frame_dir, name)
    video_frames = generate_video_frames(video_path, tmp_frame_dir,
                                         interval, video_id, end=5 * 60)
    generate_video_frames_feature(video_frames, model_name=model_name)
    shutil.rmtree(tmp_frame_dir)
    return video_frames


def find_multi_epi_opening(source_video, candidate_videos, model_name="phash"):
    """

    :param source_video: [原视频的本地地址，原视频的episode_id]
    :param candidate_videos: [[参考视频1的本地地址，参考视频1的episode_id],[参考视频2的本地地址，参考视频2的episode_id]]
    :return:
    """
    begin_time = time.time()
    source_video, source_video_id = source_video
    series_reference_videos = []
    series_reference_videos_id = []
    for video, video_id in candidate_videos:  # 只取小于等于两个参考视频
        series_reference_videos.append(video)
        series_reference_videos_id.append(video_id)
    opening_start = 0
    opening_end = 0
    # 建立目标视频以及候选视频
    frame_dir = os.path.join("data", "tmp", get_uuid_str())

    logger.info(f"process {source_video}")
    try:
        logger.info(f"begin to analysis video : {source_video}")
        if len(series_reference_videos) != 2:
            logger.info(f"less than one series video {source_video}")

        logger.info(f"begin process source video {source_video} , "
                    f"reference videos is {series_reference_videos}")

        source_video_frames = generate_video_frames_info_by_video_path(
            source_video, frame_dir,
            model_name=model_name, video_id=source_video_id,
        )
        series_reference_videos_frames = []
        for series_reference_video_id, series_reference_video in zip(
                series_reference_videos_id, series_reference_videos):
            video_frames = generate_video_frames_info_by_video_path(
                series_reference_video, frame_dir,
                video_id=series_reference_video_id, model_name=model_name)
            series_reference_videos_frames.append(video_frames)

        # 视频帧对匹配
        series_video_match_pairs = video_match_pairs_func(
            source_video_frames, series_reference_videos_frames, model_name=model_name)
        regions = []
        for match_pairs in series_video_match_pairs:
            # 一组只选出一个片头区间
            candidate_regions = video_pairs_group_by_offsets(match_pairs)
            regions.append(candidate_regions)

        merged_regions = merge_and_ranking_regions_for_beginning(regions)
        if merged_regions:
            opening_region = merged_regions[0]
            if hms_to_second(opening_region[0]) < 1:  # 如果起始时间小于1，则从0开始
                opening_region[0] = second_to_hms(0)
            logger.info(f"origin region is {opening_region[1]}")
            from deep_copilot.video_and_image_tools.sceneutil import SceneDetector
            sub_title = remain_ch_en_number(os.path.basename(source_video).split("_")[2])

            scene_detector = SceneDetector(source_video)
            opening_region_end = hms_to_second(opening_region[1])
            opening_region_start = hms_to_second(opening_region[0])
            scene_detect_start = opening_region_end - 10 if opening_region_end - 10 > 0 else 0
            scene_detect_end = opening_region_end + 5
            scene_boundaries = scene_detector.detect_scene_by_start_end(scene_detect_start, scene_detect_end)
            if scene_boundaries[-1] < opening_region_end:
                scene_boundaries.append(opening_region_end)

            sub_title_frame_pos = None  # 第一个出现副标题的帧
            candidate_title_frame_pos = None  # 出现 第xxx集 的帧，作为候选
            # 原始时间点 先往前、再往后，因为有时候后面剧情的字幕会出现点题现象
            scene_boundary_regions = sorted(
                list(zip(scene_boundaries[:-1], scene_boundaries[1:])),
                key=lambda x:
                (x[1] > opening_region_end, math.fabs(x[1] - opening_region_end))
            )  # 大于结束时间在后，而后按照时间升序
            for start, end in scene_boundary_regions:
                logger.info(f"search the subtitle from {start} to {end}")
                tmp_key_frame_dir = os.path.join(frame_dir, "tmp_key_frame_dir")
                key_frames = generate_key_frame(
                    source_video, tmp_key_frame_dir, method="interval_fix",
                    interval=10, start=start, end=end)
                # 如果原始结束时间在两者之间
                if start < opening_region_end < end:
                    # 大的为True,排在后面
                    key_frames = sorted(key_frames, key=lambda x: hms_to_second(x[2]) > opening_region_end)
                for key_frame, frame_index, hms in tqdm(key_frames):
                    ocr_result = ocr(key_frame)
                    ocr_result = remain_ch_en_number(ocr_result)
                    frame_pos = hms_to_second(hms)
                    if sub_title in ocr_result:
                        logger.info(f"find sub_title {sub_title} in ocr_result {ocr_result}")
                        if end - start <= 2:
                            sub_title_frame_pos = start
                        else:
                            sub_title_frame_pos = frame_pos
                        break
                    elif re.search("第(.*)集", ocr_result):
                        logger.info(f"find pattern 第(.*)集 in ocr_result {ocr_result}")
                        if end - start <= 2:
                            candidate_title_frame_pos = start
                        else:
                            candidate_title_frame_pos = frame_pos
                if sub_title_frame_pos:
                    break
            if sub_title_frame_pos:
                opening_region[1] = second_to_hms(sub_title_frame_pos)
                opening_region_end = sub_title_frame_pos
            elif candidate_title_frame_pos:
                opening_region[1] = second_to_hms(candidate_title_frame_pos)
                opening_region_end = candidate_title_frame_pos

            if opening_region_end - opening_region_start < 5 and opening_region_start != 0:
                logger.info(f"not found opening region , video path is {source_video}")
                opening_start = "no beginning"
                opening_end = "no beginning"
            else:
                logger.info(f"final opening region is {opening_region}, video path is {source_video}")
                opening_start = hms_to_second(opening_region[0])
                opening_end = hms_to_second(opening_region[1])
        else:
            logger.info(f"not found opening region , video path is {source_video}")
            opening_start = "no beginning"
            opening_end = "no beginning"
        if os.path.exists(frame_dir):
            shutil.rmtree(frame_dir)
    except:
        logger.exception("")
    finally:
        logger.info(f"episode beginning recognition cost time: {time.time() - begin_time}")
        if os.path.exists(frame_dir):
            shutil.rmtree(frame_dir)
    return opening_start, opening_end
