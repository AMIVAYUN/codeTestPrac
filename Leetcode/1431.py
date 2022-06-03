# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:57:17 2022
@FileName: 1431.py
@author: YUNJUSEOK
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max1 = max( candies ) - extraCandies;
        result = [  i >= max1 for i in candies ];
        return result;
        
