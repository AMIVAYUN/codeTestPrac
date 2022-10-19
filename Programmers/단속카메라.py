# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 13:48:58 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(routes):
    answer = 1
    
    routes = list (sorted( routes ) )
    
    field = set();
    
    for route in routes:
        lst = [ i for i in range( route[ 0 ], route[ 1 ] + 1 ) ];
        
        field |= set( lst );
    
    import itertools;
    from collections import defaultdict;
    for i in range( 1, len( field ) + 1 ):
        cmb = itertools.combinations( field, i );
        
        dit = defaultdict( int )
        for case in cmb:
    
            lst = [ 0 ] * len( routes );
            for route in routes:
                idx = 0;
                start, end = route;
                flag = False;
                for number in case:
                    if( number < start or number > end ):
                        flag = True;
                        break;
                
                if( flag ):
                    lst[idx] = flag;
                idx += 1;
            
            if( sum( lst ) == len( routes ) ):
                print( lst )
                continue;
            
            dit[ case ] = 1;
            
        for key in dit:
            if( dit[ key ] ):
                print( key )
                return key;
    
    
    return 0;
        
solution( [[-7, 0], [-6, -4], [-5, -3], [-3, -1], [-1, 4], [1, 2], [3, 4]] )                
            
        
'''
    start, end = routes[ 0 ];
    stan = end;
    print( routes );
    for start_tmp, end_tmp in routes[ 1: ]:

        if( end < start_tmp ):
            print( "case 1", end,stan,end_tmp)
            answer += 1;
            stan = end_tmp;
            end = end_tmp
        
        elif( start_tmp <= end and start_tmp <= stan ):
            print( "case 2", end,stan,end_tmp)
            end = end_tmp;
        
        elif( start_tmp <= end and start_tmp > stan ):
            print( "case 3",end,stan,end_tmp )
            answer += 1;
            end = end_tmp;
            stan = end_tmp;

#
        # 시작점이 end보다 클 때
        
    
    return answer
'''