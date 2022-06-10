# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 15:34:22 2022
@FileName: 2110.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2110

Binary Search

"""

def main():
    
    N, C = map( int, input().split() );

    house = [];

    for i in range( N ):
        house.append( int( input() ) );
    
    house = sorted( house );
    
   
    
    lt , rt = 1 , house[ -1 ] - house [ 0 ];
    
    while lt <= rt:
        mid = ( lt + rt ) // 2;
        
        pos = house[ 0 ];
        count = 1;
        
        for i in range( 1, len( house ) ):
            if( house[ i ] - ( pos + mid ) >= 0 ):
                count += 1;
                pos = house[ i ];
            
        
        
    
       
        if count >= C:
            result = mid;
            lt = mid + 1;
        else:
            rt = mid - 1;
            
    
    print( result )
        


if( __name__ == "__main__"):
    main();