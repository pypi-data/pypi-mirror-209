#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/21 下午4:17
# @Author : gyw
# @File : agi_py_repo
# @ description:
from paddleocr import PaddleOCR

paddle_ocr_predictor = None


def get_paddle_ocr_predictor(lang="ch"):
    global paddle_ocr_predictor
    if paddle_ocr_predictor is None:
        #  定义ocr
        if lang == "ch":
            paddle_ocr_predictor = PaddleOCR(lang="ch")
        else:
            raise NotImplementedError
    return paddle_ocr_predictor


def paddle_ocr_predict(img_path, lang="ch"):
    """
    paddle ocr 的预测代码
    :param img_path:
    :param lang:
    :return:
    """
    predictor = get_paddle_ocr_predictor(lang=lang)
    result = predictor.ocr(img_path, cls=True)
    text = ""
    for line in result[0]:
        text += line[-1][0]
    return text
