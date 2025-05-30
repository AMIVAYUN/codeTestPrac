# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:24:25 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def get3Number( num ):
    ans = [];
    
    while num != 0:
        
        num,mod = divmod( num, 3 );
        if( mod == 0 ):
            num -= 1;
            mod = 4;
        
        ans.append( str( mod ) );
            
    
    ans.reverse();
    
    return ans;
            
            
    
def solution(n):
    
    ans = get3Number( n );

    
    if( len( ans ) > 1 ):
        
        for i in range( len( ans ) - 1 ):
            if( ans[ i ] + ans[ i + 1 ] == '10' ):
                ans = ans[ :i ] + ['4'] +ans[ i + 2: ];
            

    

    
    return ''.join( ans );