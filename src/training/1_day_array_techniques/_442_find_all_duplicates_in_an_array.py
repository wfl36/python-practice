#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2025/6/4 16:37
@Author : leo
@File   : _442_find_all_duplicates_in_an_array.py
"""
from typing import List


def find_all_duplicates(nums: List[int]) -> List[int]:
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    for x in nums:
        nums[(x - 1) % n] += n
    res = []
    for i in range(n):
        if nums[i] > 2 * n:
            res.append(i + 1)
    return res

print(find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))

# 第二种实现
def findDuplicates(nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
        if nums[abs(nums[i]) - 1] < 0:
            res.append(abs(nums[i]))
        else:
            nums[abs(nums[i]) - 1] *= -1
    return res
