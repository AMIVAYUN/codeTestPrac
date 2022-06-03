# -*- coding: utf-8 -*-
"""
Created on Thu May 12 19:34:14 2022
@FileName: 1608.py
@author: YUNJUSEOK
Title:1608. Special Array With X Elements Greater Than or Equal X
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
Desc: 
    You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

    Notice that x does not have to be an element in nums.

    Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
"""

# O( N² )
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        max0 = max( nums );        
        for i in range( 1, max0 + 1 ):
            count = 0;
            for j in range( len( nums ) ):
                if( i <= nums[ j ] ):
                    count +=1;
            
            if( count == i ):
                return i;
        
        
        return -1;
        
        
        
        
# 개선
# 물어 보자. 시간 복잡도는 일단 N²log n 인데 더 빠르다. 나의 생각: sorting을 한다 가정해도 위의 식은 연산 수가 max값 기준이기에 더 많다라는 생각이다.

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        len0 = len( nums );   
        for i in range( 1, len0 + 1 ):
            test = sorted( [i] + nums );
            idx = test.index( i );
            if( i == len( test[ idx + 1: ] ) ):
                return i
            
        
        
        return -1;
        
        
        
        
        