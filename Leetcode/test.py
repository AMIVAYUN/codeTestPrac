# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:07:11 2022
@FileName: Subtest.py
@author: YUNJUSEOK
"""

import heapq
class Solution:
    def replaceElements(self, arr):
        # 9:51pm 12/29/2020 as a mock interview
        # 9:54pm
        # maintain a priority queue
        
        h, res = [], [-1]
        
        for i in reversed(range(len(arr))):
            heapq.heappush(h, -arr[i])
            res.append(-h[0])
            
        return res[::-1][1:]
    
    
    
a = Solution();
res1= a.replaceElements([17,18,5,4,6,1])

print( res1 );