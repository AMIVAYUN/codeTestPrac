# -*- coding: utf-8 -*-
"""
Created on Tue May  3 17:28:51 2022
@FileName: 553.py
@author: YUNJUSEOK
"""
## 엄청난 반례들을 겪을 수 있었다. 단순히 자릿수들로만 찾으려고 하니 틀린것 같다 다시 한번 생각해보자.

# 생각을 잘해야했다. 내가 생각한 것은 숫자 별 나열이였고, 여기서 말하는 값은 그 다음 바로 작은 수다.


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n1 = str( n );
        rMx = max( n1 );
        cnt = n1.count( rMx );
        str1 = '';
        if( ( rMx == n1[0] and cnt == 1 ) or len( n1 ) == cnt ):
            return -1;
        if( cnt > 1 ):
            result = n1.split( rMx );
            for i in result:
                str1 += i;
            c = rMx * cnt + ''.join( sorted(str1) ) 
            return c;
        rMn = min( [ i for i in n1 if( i > n1[0] ) ] )
        a, b = n1.split( rMn );
        result = ''.join( ( list( rMn ) + ( sorted( a+b ) ) ) )
        return result;
        