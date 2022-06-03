# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:04:18 2022
@FileName: 2148.py
@author: YUNJUSEOK
"""
# 59%
class Solution:
    def countElements(self, nums: List[int]) -> int:
        cnt = 0;
        for i in nums:
            if( ( self.getGreater( nums, i ) ) and ( self.getSmaller( nums, i ) ) ):
                cnt += 1;
        
        return cnt;
    
    
    def getGreater( self,nums , vl ):
        for j in nums:
            if( j > vl ):
                return True;
        
        return False;
    def getSmaller( self,nums , vl ):
        for j in nums:
            if( j < vl ):
                return True;
        
        return False;
    
# 14.53%
# 로직은 짧아졌지만 값은 더 길어졌다.
class Solution:
    def countElements(self, nums: List[int]) -> int:
        cnt = 0;
        max1 , min1 = max( nums ), min( nums );
        for i in nums:
            if( i != max1 and i != min1 ):
                cnt += 1;
        
        return cnt;
    
    
