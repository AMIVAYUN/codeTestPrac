# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:49:53 2022
@FileName: .py
@author: YUNJUSEOK
"""

#Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
#The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
class Solution:
    def gcd( a, b ):
        if( b == 0 ):
            return a;
        if( a > b ):
            return gcd( a%b , b );
        else:
            return gcd( b, a );
    def findGCD(self, nums: List[int]) -> int:
        max1 = max( nums );
        min1 = min( nums );
        return gcd( max1, min1 );