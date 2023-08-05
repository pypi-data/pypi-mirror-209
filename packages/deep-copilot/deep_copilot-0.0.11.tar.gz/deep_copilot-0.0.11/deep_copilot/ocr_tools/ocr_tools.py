#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/21 下午4:17
# @Author : gyw
# @File : agi_py_repo
# @ description:
from .paddle_tools import paddle_ocr_predict


def ocr(image_path, model="paddle", *args, **kwargs):
    if model == "paddle":
        return paddle_ocr_predict(image_path, *args, **kwargs)
    else:
        raise NotImplementedError(f"no such ocr model, {model}")
