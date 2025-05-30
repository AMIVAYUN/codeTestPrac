# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 00:24:14 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

'''
#sol1 timeout
def solution(gems):
    from collections import defaultdict;
    answer = []
    ddit = defaultdict( int );
    for gem in gems:
        ddit[ gem ] += 1;
    
    obj = len( ddit );
    
    mapper = defaultdict( int );
    start = 0;
    for key in ddit:
        mapper[ key ] = start;
        start += 1;
        
    if( obj == 1 ):
        return [1,1];
    lengems = len( gems );
    dp = [ [ set() ] * ( lengems )  for _ in range( lengems + 1 ) ];
    
    dp[ 1 ] = [ set( [ mapper[ gems[ i ] ] ] ) for i in range( lengems ) ] 
    
    for x in range( 2, lengems + 1 ):
        
        for y in range( lengems - x + 1 ):
            dp[ x ][ y ] =  dp[ x - 1 ][ y ] | set( [ mapper[ gems[ x + y - 1 ] ] ] ) ;
            if( len( ( dp[ x ][ y ] ) ) == obj  ) :
                return [ y + 1 , y + x ];
    

    return answer
    
    
    '''

'''
#sol2
def solution(gems):
    from collections import defaultdict;
    answer = []
    ddit = defaultdict( int );
    for gem in gems:
        ddit[ gem ] += 1;
    
    obj = len( ddit );
    
    mapper = defaultdict( int );
    start = 0;
    for key in ddit:
        mapper[ key ] = start;
        start += 1;
        
    if( obj == 1 ):
        return [1,1];
    
    lengems = len( gems );
    
    dp = [ [ set() ] * ( lengems )  for _ in range( lengems + 1 ) ];
    

    
    for offset in range( lengems + 1 ):
        
        for x in range( lengems - offset ):

            if( offset == 0 ):
                dp[ x ][ x + offset ] =  set( [ mapper[ gems[ x ] ] ] )
                                             
            else:
                dp[ x ][ x + offset ] = ( dp[ x ][ x + offset - 1 ] ) | set( [ mapper[ gems[ x + offset ] ] ] );
                if( len( dp[ x ][ x + offset ] ) == obj ):
                    return [ x + 1, x + offset + 1 ]
                    
'''
'''
#sol3
def solution(gems):
    from collections import defaultdict;
    from collections import deque;
    answer = []
    ddit = defaultdict( int );
    for gem in gems:
        ddit[ gem ] += 1;
    
    obj = len( ddit );
    
    mapper = defaultdict( int );
    start = 0;
    for key in ddit:
        mapper[ key ] = start;
        start += 1;
        
    leng = len( gems );
    gems_bit = [ mapper[ i ] for i in gems ];
    
    for offset in range( 1, leng + 1 ):

        start = ( gems_bit[ : offset ] )
        if( len( set( start ) ) == obj ):
            return [ 1, offset ];
        for i in range( offset, leng ):

            
                
            start.remove( gems_bit[ i - offset ] );
            start.append( gems_bit[ i ] );
            
            if( len( set( start ) )== obj ):
                tmp = offset - 1;
                return [ i - tmp + 1 , i + 1  ];



'''


def solution(gems):
    from collections import defaultdict;
    from collections import deque;
    answer = []
    ddit = defaultdict( int );
    
    leng = len( gems );
    
    
    for gem in gems:
        ddit[ gem ] += 1;
        
        
    obj = len( ddit );
    lll = leng + 1;
    idx = 0;
    
    start, end = 0, 0 ;
    context = defaultdict( int );
    
    while end != leng:
        context[ gems[ end ] ] += 1;
        end += 1
        if( len( context ) == obj ):
            while start < end:
                if( context[ gems[ start ] ] > 1) :
                    
                    context[ gems[ start ] ] -= 1;
                    start += 1;
                
                elif( lll > end - start ):
                    lll = end - start;
                    answer = [ start + 1, end ]
                    break;
                else:
                    break;
    
    return answer;


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"] )