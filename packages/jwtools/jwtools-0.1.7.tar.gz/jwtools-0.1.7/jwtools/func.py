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


def get_max_dimension(lst):
    """
    获取列表的最大维度
    :author wjh
    :date 2023-05-23
    :param lst:
    :return:
    """
    if isinstance(lst, list):
        dimensions = [get_max_dimension(item) for item in lst]
        max_dim = max(dimensions) if dimensions else 0
        return max_dim + 1
    else:
        return 0


def flatten_list(lst) -> list:
    """
    平铺列表为一维列表
    递归函数，遍历列表的每个元素。如果元素是列表，则递归调用该函数继续平铺。如果元素是非列表元素，则直接添加到最终的一维列表中
    :author wjh
    :date 2023-05-23
    :param lst: 多维列表
    :return: 平铺后列表
    """
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened


def print_line(title='', fill_char='-', length=30, newline=True):
    """
    输出分隔线
    :author wjh
    :date 2023-05-23
    :param title: 标题
    :param fill_char: 填充字符
    :param length: 长度
    :param newline: 是否换行
    :return:
    """
    separator = fill_char * int(length / 2) + title + fill_char * int(length / 2)
    if newline:
        print(separator)
    else:
        print(separator, end='')
