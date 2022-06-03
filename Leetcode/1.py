# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:36:20 2022
@FileName: 1 TwoSum.py
@author: YUNJUSEOK
https://leetcode.com/problems/two-sum/
"""


            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range( len( nums ) ):
            for j in range( i + 1 ,len( nums ) ):
                if( nums[ i ] + nums[ j ] == target):
                    return [ i, j ];

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range( len( nums ) ):
            pos = target-nums[ i ]
            if(  nums.__contains__( pos )):
                idx = nums.index( pos );
                if( idx == i ):
                    continue;
                
                return [ i, idx ]
        
        
                
   
        
        
        