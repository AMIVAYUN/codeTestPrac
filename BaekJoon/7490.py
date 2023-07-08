# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 13:35:00 2023

@author: 주석
"""


lst =[];
answer = [];
# 이어 붙이는게 우선순위임
def dfs( text, num, pos ):
    global answer, lst;
    
    if( pos == len( lst ) ):
        if( num == 0 ):
            answer.append( text[:] );
        return;
        
        
    text.append( "+" );
    dfs( text, num + lst[ pos ], pos + 1 );
    text.pop();
    
    text.append( "-" );
    dfs( text, num - lst[ pos ], pos + 1 );
    text.pop();
    
    text.append( " " );
    dfs( text, (num * 10) + lst[ pos ], pos + 1 );
    text.pop()
''' 수정
def getT():
    nums = [ i for i in range( 1, 8 ) ];
    case = list(  ('-', '+', ' ', '+', '+', '+') );
    idx = 0;
    case = list( case )[:];
    while idx < len( case ):

        if( case[ idx ] == " " ):
            nums[ idx ] = nums[ idx ] * 10 + nums[ idx + 1 ];
            case.pop( idx );
            nums.pop( idx + 1 );
            continue
        
        
        
        idx += 1;
        
    print( nums, case );
    start = nums[ 0 ];
    for idx in range( len( case ) ):
        
        if( case[ idx ] == '+' ):
            start += nums[ idx + 1 ];
        else:
            start -= nums[ idx + 1 ];
            
    
    print( start )
'''
def getAns( lst, case ):
    nums = lst[ : ];
    idx = 0;
    case = list( case )[:];
    while idx < len( case ):
        if( case[ idx ] == " " ):
            nums[ idx ] = nums[ idx ] * 10 + nums[ idx + 1 ];
            case.pop( idx );
            nums.pop( idx + 1 );
            continue
        
        
        
        idx += 1;
        
    
    start = nums[ 0 ];
    for idx in range( len( case ) ):
        
        if( case[ idx ] == '+' ):
            start += nums[ idx + 1 ];
        else:
            start -= nums[ idx + 1 ];
            
    
    return start;
    

import itertools;


T = int( input() );
num = [];
for i in range( T ):
    num.append( int( input() ) );

for i in range( T ):
    n = num[ i ];
    answer = [];
    lst = [ i for i in range( 1, n + 1 ) ];
    
    opers = [ ' ', '+', '-', ];
    
    cases = list( itertools.product( opers, repeat= n - 1 ) );
    
    for case in cases:
        result = getAns( lst, case );
        
        if( result == 0 ):
            answer.append( case );
        
    for ans in answer:
        
        anstr0 = str( lst[ 0 ] );
        
        for idx in range( len( ans ) ):
            anstr0 += ans[ idx ];
            anstr0 += str( lst[ idx + 1 ] );
        
        print( anstr0 );
    print();
    
    '''
    dfs( [], lst[ 0 ], 1 );
    
    for case in answer:
        
        str0 = str( lst[ 0 ] );
        
        for idx in range( len( case ) ):
            str0 += case[ idx ];
            str0 += str( lst[ idx + 1 ] );
        
        print( str0 );
    '''   

    