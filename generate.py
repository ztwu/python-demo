#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'generate.py'
# Author:   'yancai'

"""
GROUPING SET维度生成脚本
 - 依赖环境：
    1. Python，不需要第三方包
    2. Windows、Linux、Mac通吃

 - 使用方法：
    1. 修改`dims`中的维度，注意格式！注意缩进！
    2. 执行执行此脚本：python generate.py
    3. 拷贝此脚本输出的维度至SQL脚本中
    4. 注意删除最后一行最后一个逗号，如果不知道什么意思，没关系，SQL脚本报错就知道什么情况了

"""

import itertools


# TODO: 维度字典，在此字典中增加或修改维度名称，`True`表示包含全部，`False`表示不包含全部
dims = {
	"app_id": True,
}

area = [
    (),
    ("province_id",),
    ("province_id", "city_id"),
    ("province_id", "city_id", "district_id"),
    ("province_id", "city_id", "district_id", "school_id"),
]


def unfold(ls):
    r = []
    [r.extend(list(i)) for i in ls if len(i) > 0]
    return r


def gen():
    """生成构建cube的列表
    """
    iters = []
    for k, v in dims.items():
        if v:
            iters.append([(), (k,)])
        else:
            iters.append([(k,)])
    return iters


def main():
    for i in itertools.product(area, *gen()):
        s = str(tuple(unfold(i))).replace(",)", ")").replace("'", "") + ","
        print(s)


if __name__ == "__main__":
    main()
    pass
