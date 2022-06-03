# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:36:29 2022
@FileName: .py
@author: YUNJUSEOK
"""

# 속도가 좋지 못하다 어제 했던 것처럼 stack을 사용해보자,
class Solution:
    def makeGood(self, s: str) -> str:
        num = [ ord ( i ) for i in s ];
        idx = 0;

        while( True ):
    
            if( idx >= len( num ) - 1 ):
      
                break;
        
    
            if( abs( num[ idx ] - num[ idx + 1 ] ) == 0x20 ):
        
                num = num[ :idx ]+num[ idx+2: ];
                idx = 0;
                continue;
    
    
            idx += 1;
            
        return ''.join( [ chr( i ) for i in num])
    
    
# stack을 통한 해결 이러한 앞 뒤자리 비교때는 stack을 적극 활용하자.
   
class Solution:
    def makeGood(self, s: str) -> str:
        num = [ ord ( i ) for i in s ];
        stack = [];
        l = len( num );
        for i in range( l ):
            if( stack and ( abs(num[ i ] - stack[ -1 ]) == 0x20  )  ):
                stack.pop();
            else:
                stack.append( num[ i ] );
        
        return ''.join( [ chr( i ) for i in stack ] );

a = Solution();

b = a.makeGood( "abBAcC")
print( b );    