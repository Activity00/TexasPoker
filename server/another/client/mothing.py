# coding: utf-8

"""
@author: 武明辉 
@time: 2018/1/18 11:25
"""
import doctest

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
print(d)

if __name__ == '__main__':
    doctest.testmod()
