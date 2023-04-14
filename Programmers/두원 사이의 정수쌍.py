# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:26:05 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution( r1, r2 ):
    import math;
    answer = 0;
    lst = [ i for i in range( 0, r2 + 1 ) ];
    
    start = r2 - r1;
    
    for i in range( 1, r2 + 1 ):
        
        lt = math.ceil( ( ( r1 **2 - i**2 ) ** 0.5).real );
        rt = math.floor( ( ( r2 ** 2 - i ** 2 ) ** 0.5 ).real ) ;
  
        
        
        answer += ( rt - lt + 1 ) * 4;
    
    
    lt = r1;
    
    rt = r2;
    
    answer += ( r2 - r1 ) * 4;
    
    return answer;
'''
#SOL1 WA
def solution(r1, r2):
    answer = 0;
    import bisect;
    Mn = min( r1, r2 // 2 );
    lst = [ i for i in range( r2 + 1 ) ];
    leng = len( lst );
    #print( lst );
    for x in range( Mn, r2 + 1 ):
        ltMx = r1 ** 2 - x ** 2;
        rtMx = r2 ** 2 - x ** 2;
        lt = 0; rt = leng;
        left = None;
        
        while lt<= rt and lt >= 0 and rt >= 0:
            mid = ( lt + rt ) // 2;
            
            if( ( lst[ mid ] ) **2 >= ltMx ):
                rt = mid - 1;
                left = mid;
            else:
                
                lt = mid - 1;
        
       
        
        right = None;
        lt = 0; rt = leng;
        while lt<= rt and lt >= 0 and rt >= 0:
            mid = ( lt + rt ) // 2;
            
            if( ( lst[ mid ] ) **2 <= rtMx ):
                lt = mid + 1;
                right = mid;
            else:
                
                rt = mid - 1;
        if( left != None and right != None ):
            answer += ( lst[ right ] - lst[ left ] + 1 )
            #print("rs:", x, lst[ left ], lst[ right ] );
    return answer * 4;
    
'''