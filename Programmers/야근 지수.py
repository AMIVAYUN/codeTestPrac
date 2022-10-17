# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:58:32 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

'''
def solution(n, works):
    answer = 0
    
    while n > 0 and sum( works ) > 0:
        Mn = min( works );
        
        idx = -1;
        while max( works ) != Mn and n > 0:
            idx = ( idx + 1 ) % len( works ); 
            if( works[ idx ] <= Mn ):
                continue;
            works[ idx ] -= 1;
            n -= 1;
            
        
    return sum( [ i ** 2 for i in works ] );
'''
'''
def solution1(n, works):
    answer = 0
    leng = len( works );
    import bisect;
    sum_ = sum( works );
    works = list( sorted( works ) );
    

    
    while n > 0 and sum_ > 0:
        
        Mx = works[ -1 ];
        
        target = bisect.bisect_left( works, Mx );
        
        
        idx = leng - 1;
        
        while n > 0 and sum_ > 0 and idx >= target:
            
                
            works[ idx ] -= 1;
            n -= 1;
            sum_ -= 1;
            idx -= 1;
                  
        
    return sum( [ i ** 2 for i in works ] );
'''
def solution(n, works):
    answer = 0
    leng = len( works );
    import bisect;
    sum_ = sum( works );
    works = list( sorted( works ) );
    

    
    while n > 0 and sum_ > 0:
        
        Mx = works[ -1 ];
        
        target = bisect.bisect_left( works, Mx );
        
        
        idx = leng - 1;
        
        while n > 0 and sum_ > 0 and idx >= target:
            
                
            works[ idx ] -= 1;
            n -= 1;
            sum_ -= 1;
            idx -= 1;
                  
        
    return sum( [ i ** 2 for i in works ] );
solution( 4, [4, 3, 3] )

solution( 99, [2, 15, 22, 55, 55] )