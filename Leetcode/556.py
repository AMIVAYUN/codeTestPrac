# -*- coding: utf-8 -*-
"""
Created on Tue May  3 21:18:26 2022
@FileName: .py
@author: YUNJUSEOK
"""

## 2147483476에서 에러가 뜬다 고쳐보자. 
n= 112313
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = [ i  for i in str( n ) ];
    
    
        lst = [];
        if( num == sorted( num, reverse = True ) or n >= 2**31 -1  ):
            return -1;
        lenx = len( num );
        idx = lenx - 1;
        while( idx >= 1):
            if( num[ idx ] > num[ idx - 1 ]  ):
                num[ idx ], num [ idx - 1 ] = num[ idx - 1 ], num[ idx ];
                
                break;
            idx -= 1;
                


        num2 = num[ 0: idx ] + sorted( num[ idx : lenx ] ) ;
        
        if( int(''.join( num2 )) > 2**31 - 1):
            return -1;
        
        return ''.join( num2 );
    
a= Solution();
k = a.nextGreaterElement( n );
print( k );
    
    
    
    
    