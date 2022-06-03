# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:51:07 2022
@FileName: 493.py
@author: YUNJUSEOK
"""


class Solution:
    # 틀림 내가 문제를 잘못 이해했다. 끝까지 가야 했었다.
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        len1 = len( nums1 );
        len2 = len( nums2 );
        result = [0] * len1 ;
        for i in range( len1 ):
            j = nums2.index( nums1[ i ] );
            if( j == len2 - 1 or nums2[ j ] > nums2[ j + 1 ] ) :
                result[i] = -1;
            else: 
                result[i] = nums2[ j + 1 ];
        
        return result;
                
# 하지만 해당 로직은 O(N²)의 구조를 갖게 되므로 좋지 못하다.
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        len1 = len( nums1 );
        len2 = len( nums2 );
        result = [ -1 ] * len1;
        
        for i in range( len1 ):
            k = nums2.index( nums1[i] );
            Mxidx = nums2[k]
            for j in range( k, len2 ):
                if( Mxidx < nums2[ j ] ):
                    Mxidx = nums2[ j ];
                    result[ i ] = Mxidx;
                    break;
        
        
        
        
        return result;
                
        
        