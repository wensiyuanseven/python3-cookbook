#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: collections.deque演示
Desc : deque有一个maxlen参数，当append的时候，如果超过，那么最前面的就被挤出队列。

collections.deque用法
https://zhuanlan.zhihu.com/p/32201189
初始化deque的时候可以给他传一个参数maxlen，如果deque中的元素超过maxlen的值，那么就会从deque中的一边去删除元素，也就是deque始终保持maxlen最大长度的元素，如果超过了就会自动把以前的元素弹出(删除)

yield用法
https://juejin.cn/s/python%20yield%20next%20%E7%94%A8%E6%B3%95
https://blog.csdn.net/mieleizhi0522/article/details/82142856

with用法
https://www.runoob.com/python3/python-with.html

字符串前面加'r' 用法
https://zhuanlan.zhihu.com/p/110102003

open() 函数
https://www.runoob.com/python/python-func-open.html



"""
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


# Example use on a file
if __name__ == '__main__':
    with open(r'/Users/liushali/前端_code/python3/python3-cookbook/cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'Python', 5):  # 因为 yield 是可迭代的 所以可以循环
            for pline in prevlines:
                print(pline, end='')  # 不换行
            print(line, end='')  # 不换行
            print('-' * 20)
