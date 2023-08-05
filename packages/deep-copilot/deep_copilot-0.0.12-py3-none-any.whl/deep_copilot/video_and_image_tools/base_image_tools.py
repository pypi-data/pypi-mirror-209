#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/7/19 下午3:22
# @Author : gyw
# @File : content-service
# @ description:

import requests
from PIL import Image
from io import BytesIO
import os
import uuid
import tempfile
from .opencv_tools import phash

def save_pic_from_url(url, dest_path=None):
    """
    从URL存储图片到本地数据，url是可以直接访问的
    Args:
        url: url路径
        dest_path:存储的路径 None的话，存储在{project_dir}/tmp

    Returns:

    """
    if not dest_path:
        file = tempfile.NamedTemporaryFile("wb", suffix=".png")
        dest_path = file.name
    resp = requests.get(url)
    byte_stream = BytesIO(resp.content)
    im = Image.open(byte_stream)
    if im.mode == "RGBA":
        im.load()  # required for png.split()
        background = Image.new("RGB", im.size, (255, 255, 255))
        background.paste(im, mask=im.split()[3])
    im.save(dest_path, "png")
    return dest_path


def get_pictures_feature(picture_paths, model_name="phash"):
    """
    获取图像的特征
    :param picture_paths: 图片路径
    :param model_name: 模型名称
    :return:
    """
    if model_name == "phash":
        frames_feature = [phash(picture_path) for picture_path in picture_paths]
        return frames_feature
