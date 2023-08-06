import datetime
import hashlib
import random
import time
import os
import sys
import traceback
from typing import Dict, Tuple, List


def get_text_md5(text) -> str:
    """
    计算字符串md5
    :param text:
    :return:
    """
    # print('md5处理：%s' % text)
    md5 = hashlib.md5(text.encode("utf-8")).hexdigest()
    return md5


def write_text_to_file(filename: str, content: str, encoding="utf-8") -> bool:
    """
    把文本写入文件
    :author wjh
    :date 2023-05-18
    :param filename: 要写入的文件名。
    :param encoding: 文件编码，默认为utf-8
    :param content: 文本内容
    :return: 是否写入成功。
    """
    try:
        with open(filename, "w", encoding=encoding) as f:
            f.write(content)
    except Exception as e:
        return False

    return True


def read_text_from_file(filename, encoding="utf-8") -> str:
    """
    从指定文件中读取文本内容并返回。
    :author wjh
    :date 2023-05-18
    :param filename：要读取的文件名。
    :param encoding：文件的编码方式，默认为utf-8。
    :return: 从文件中读取到的文本内容。
    """
    with open(filename, "r", encoding=encoding) as file:
        text = file.read()
    return text


def print_vf(*args):
    """
    print var or function
    :author wjh
    :date 2023-05-22
    :param args:
    :return:
    """
    for arg in args:
        if callable(arg):
            print(arg())
        else:
            print(arg)
