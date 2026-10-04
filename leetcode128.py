# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 01:21:21 2026

@author: vinay
"""
from typing import List

def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)  
    longest = 0
    
    for n in numSet:
        if (n-1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length+=1
            longest = max(length, longest)
    return longest

nums = [100, 4, 200, 1, 3, 2]
longestConsecutive(nums)
