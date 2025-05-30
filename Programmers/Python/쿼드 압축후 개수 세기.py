# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:24:19 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def union( graph ):
    global parent, answer;
    
    answer[ graph[ 0 ][ 0 ] ] += 1;
    
    return;
    
    
            
def getQuadCompression( graph ):
    global parent;
    
    n = len( graph );
    
    if( n == 1 ):
        answer[ graph[ 0 ] [ 0 ] ] += 1;
        return;
    
    if( isSame( graph ) ):
        union( graph )
        return;
    
    else:
        
        half = n // 2;
        
        Agraph = [ row[ : half ] for row in graph[ :half ] ]
        Bgraph = [ row[ half: ] for row in graph[ :half ] ]
        Cgraph = [ row[ : half ] for row in graph[ half: ] ]
        Dgraph = [ row[ half: ] for row in graph[ half: ] ]
        
        
        getQuadCompression( Agraph );
        getQuadCompression( Bgraph );
        getQuadCompression( Cgraph );
        getQuadCompression( Dgraph );
        


def isSame( graph ):
    start = graph[ 0 ][ 0 ];
    for x in range( len( graph ) ):
        for y in range( len( graph ) ):
            if( graph[ x ][ y ] != start ):
                return False;
    
    return True;
n, parent = 0, [];
answer = [];
def solution(arr):
    global n, parent,answer;
    answer = [ 0, 0 ]
    n = len( arr );
    parent = [ [ ( x, y ) for y in range( n ) ] for x in range( n ) ]
    
    getQuadCompression( arr );
    
    
    
    
    
    return answer
    
    
    

'''
def getNlist( m ):
    num = 1;
    ans = [ 1 ];
    for i in range( 10 ):
        if( num == m ):
            return ans;
        num *= 2;
        ans.append( num );
        
    return ans;
def checkbyquad( arr, offset, x, y ):
    global seta;
    cond = False;
    idxs = [];
    start = arr[ x ][ y ];
    for x in range( x, x + offset ):
        for y in range( y, y + offset ):
            if( start != arr[ x ][ y ] ):
                cond = True;
                break;
            idxs.append( ( x, y ) );
                
        if( cond ):
            break;
    if( not( cond ) ):
        for pos in idxs:
            if( pos in seta ):
                seta.remove( pos );
    
    return;
            

seta = set();
def solution(arr):
    global seta
    m = len( arr );
    lst = getNlist( m );
    
    seta = set();
    
    for x in range( m ):
        for y in range( m ):
            seta.add( ( x, y ) );

    answer = [];

    
    for quad in lst:
        
        for i in range( 0, m, quad ):
            for j in range( 0, m, quad ):
                checkbyquad( arr, quad, x, y );

    
    
    print( seta )
    return answer;
'''