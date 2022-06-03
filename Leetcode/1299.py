# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:37:57 2022
@FileName: .py
@author: YUNJUSEOK
"""
#Given an array arr, replace every element in that array with the greatest element 
#among the elements to its right, and replace the last element with -1.
#After doing so, return the array.
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lenx = len( arr );
        result = [ -1 ] * lenx;
        for i in range( lenx - 1 ):
            subarr = arr[ i + 1: ];
            max1 = max( subarr );
            result[i] = max1;
                
        
        return result;
        
heapq