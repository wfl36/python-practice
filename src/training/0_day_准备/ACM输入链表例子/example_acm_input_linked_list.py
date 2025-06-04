#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/6/4 10:47
@Author : leo
@File   : example_acm_input_linked_list.py
"""

"""
ACM 模式下，如果输入的是链表，
需要自己根据输入数据，在内存中构建链表
比如有道题目输入是链表。然后会给出下面一行数据：
23 22 1 5 6 3
"""

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

data = str(input()).split(" ")
dummyNode = ListNode(-1)
curNode = dummyNode

for i in range(len(data)):
    curNode.next = ListNode(data[i])
    curNode = curNode.next


# 最后打印的时候，是要遍历操作后的链表, 拼接输出 ->
while dummyNode.next.next:
    print(dummyNode.next.val, end="->")
    dummyNode = dummyNode.next