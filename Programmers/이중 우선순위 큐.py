# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:40:14 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(operations):
    import bisect;
    from collections import deque;
    
    answer = [];
    
    lst = deque( [] );
    
    for oper in operations:

        if( oper[ 0 ] == "I" ):
            target = oper.split( "I " );
            
            
            if( target[ 1 ] != '' ):
                ins = int( target[ 1 ] );
          
                bisect.insort( lst, ins );
            
        
        else:
            target = oper.split( "D " );
            ins = int( target[ 1 ] );

            
            if( len( lst ) > 0 ):
                
                if( ins == 1 ):
                    #최대 삭제
                    lst.pop()
                else:
                    lst.popleft();
                
    print( lst );   
    Mx = lst[ -1 ] if len( lst ) else 0;
    Mn = lst[ 0 ] if len( lst ) else 0;
    
    
    return [ Mx, Mn ]