# -*- coding: utf-8 -*-
"""
Created on Wed May  4 14:43:39 2022
@FileName: .py
@author: YUNJUSEOK
"""
# 처음에 res를 그냥 반환했지만 ABAB : ABABAB 에서 AB가 아닌 ABAB를 반환해 에러가 났었다. ==> GCD로 해결
# 이유는 두 문자열의 길이의 최대 공약수 까지가 해당 답의 maximum이기 떄문이다.
# 두번째 에러 => ABCDEF 와 ABC가 ABC로 출력이 되었다 이는 fnres에 추가 조건인 둘다 만족하는가를 체크함으로써 해결
class Solution:
    def gcd( a, b ):
        if( b == 0 ):
            return a;
        if( a > b):
            return gcd( a % b , b );
        else:
            return gcd( b , a );
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 , l2 = len( str1 ), len( str2 );
    
        res = '';
        for i in range( 0, l1 ):
            if( i > l2 ):
                break;
            pos = str1[ : i + 1 ];
            if( pos in str2 ):
                res = pos;

        maxi = gcd( l1 , l2 );
        fnres = res[ : maxi ];
        return fnres if( str1 == fnres*( l1//maxi ) ) and ( str2 == fnres*(l2//maxi ) ) else ""