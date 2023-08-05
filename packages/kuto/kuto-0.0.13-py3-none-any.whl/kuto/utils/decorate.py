"""
使用allure需要下载，并配置到环境变量，下载地址：https://github.com/allure-framework/allure2/releases
"""
import os
# import allure
import pytest
import inspect as sys_inspect

from kuto.utils.log import logger
from kuto.utils.read_file import read_json, read_yaml, read_csv, read_excel


# # 对应模块
# def epic(text):
#     return allure.epic(text)
#
#
# # 对应class
# def feature(text):
#     return allure.feature(text)
#
#
# # 对应method
# def story(text):
#     return allure.story(text)
#
#
# # 报告子模块，兼容历史版本
# def module(text):
#     return allure.story(text)
#
#
# # 用例标题标题
# def title(text):
#     return allure.title(text)
#
#
# # 报告步骤
# def step(text):
#     return allure.step(text)


def order(index):
    """
    指定用例执行顺序
    doc: https://blog.csdn.net/weixin_43880991/article/details/116221362
    """
    return pytest.mark.run(order=index)


def depend(depends: list or str = None, name=None):
    """
    设置用例依赖关系
    doc: https://www.cnblogs.com/se7enjean/p/13513131.html
    """
    if isinstance(depends, str):
        depends = [depends]
    return pytest.mark.dependency(name=name, depends=depends)


# 参数化数据
def data(list_data: list):
    """
    必须传入一个list，使用时通过在参数列表传入parma进行调用
    """
    return pytest.mark.parametrize('param', list_data)


# 从json文件获取数据进行参数化
def file_data(file=None, key=None, row=None):
    # logger.debug(config.get_env())

    """
    @param row: 第几行，针对csv和excel文件
    @param file: 文件名
    @param key: 针对json和yaml文件
    """
    # 获取被装饰方法的目录
    stack_t = sys_inspect.stack()
    ins = sys_inspect.getframeinfo(stack_t[1][0])
    file_dir = os.path.dirname(os.path.abspath(ins.filename))
    # logger.debug(file_dir)
    parent_dir = os.path.dirname(file_dir)
    parent_dir_dir = os.path.dirname(parent_dir)
    parent_dir_dir_dir = os.path.dirname(parent_dir_dir)

    # 判断当前、父目录、爷目录、太爷爷目录下的test_data目录下是否有file_name文件
    path_list = [file_dir, parent_dir, parent_dir_dir, parent_dir_dir_dir]
    file_path = None
    full_list = []
    for _path in path_list:
        # environ = config.get_env()
        # if environ:
        #     full_path = os.path.join(_path, 'data', environ, file)
        # else:
        full_path = os.path.join(_path, 'data', file)
        full_list.append(full_path)
        # print(full_path)
        if os.path.isfile(full_path) is True:
            file_path = full_path
            break
    if file_path is None:
        raise Exception(f"can not found {file} in {full_list}")

    # logger.debug(file_path)
    if file_path.endswith(".json"):
        content = read_json(file_path, key)
    elif file_path.endswith(".yml"):
        content = read_yaml(file_path, key)
    elif file_path.endswith(".csv"):
        content = read_csv(file_path, row)
    elif file_path.endswith(".xlsx"):
        content = read_excel(file_path, row)
    else:
        raise TypeError("不支持的文件类型，仅支持json、yml、csv、xlsx")

    if content:
        return data(content)
    else:
        raise ValueError('数据不能为空')

