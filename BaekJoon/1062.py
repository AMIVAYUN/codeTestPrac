# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:58:24 2022
@FileName: 1062.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1062
    '''
    # s1
    lst = [];

    for i in range( N ):
        lst.append( input() );
        
    Mx = 0;

    Sdit = defaultdict( int );

    for i in range( N ):
        Sdit[ tuple( sorted( set( lst[ i ] ) ) ) ] += 1;
        for st in lst[ i ]:
            vocab.add( st );
    print( Sdit )
    print( vocab );

    for i in range( 1, K + 1 ):
        cmb = list( itertools.combinations( vocab , i ) );
        
        for case in cmb:
            cnt = 0;
            scase = tuple( sorted( case ) );
            Mx = max( Sdit[ scase ], Mx );
        
    print( Mx );
    '''
"""
def s2():
    
    from collections import defaultdict;
    import itertools;
    N , K = map( int, input().split() );
    Sdit = defaultdict( int );
    basic = set( sorted( set( 'antatica' ) ) );
    basicNum = len( basic )
    lst = set();
    
    for i in range( N ):
        case1 = set( input() ) - basic;
        Sdit[ tuple( sorted( case1 ) ) ] += 1;
        lst = lst |  set( sorted( case1 ) ) ;
    if( K < basicNum ):
        print( 0 );
        return;
        
    Mx = 0;
    k = K - basicNum;
    cmb = list( itertools.combinations( lst ,  k ) ) 
    
    for case in cmb:
        cnt = 0;
        
        for num in range( 1, k + 1 ):
            clst = list( itertools.combinations( case, num ) );
            
            for idx in clst:
                cnt += Sdit[ idx ];
    
        Mx = max( Mx, cnt );
    
    print( Mx );

#s2()

def s3():
    
    from collections import defaultdict;
    import itertools;
    N , K = map( int, input().split() );
    Sdit = defaultdict( int );
    basic = { 'a','c','i','n','t' };
    basicNum = 5
    vocab = { k:v for k, v in enumerate( set( map( chr, range( ord( 'a' ), ord( 'z' ) + 1 ) ) ) - basic ) }
    lst = set();
    if( K < basicNum ):
        print( 0 );
        return;
        
        
    for i in range( N ):
        case1 = set( input() ) - basic;
        Sdit[ tuple( sorted( case1 ) ) ] += 1;
        lst = lst |  set( sorted( case1 ) ) ;
    
    Mx = 0;
    k = K - basicNum;
    cmb = list( itertools.combinations( lst ,  k ) ) 

    for case in cmb:
        cnt = 0;
        case_ = set( case );
      
        
        for idx in Sdit:
            set_ = set( idx );
            if( set_ & case_ == set_ ):
                cnt += Sdit[ idx ] ;
    
        Mx = max( Mx, cnt );
    
    print( Mx );

#s3()
'''
{'u': 0, 'f': 1, 'p': 2, 'y': 3, 'v': 4, 'o': 5, 'l': 6, 'q': 7, 'b': 8, 'd': 9, 'h': 10, 's': 11, 'j': 12,
 'e': 13, 'm': 14, 'x': 15, 'r': 16, 'z': 17, 'g': 18, 'k': 19, 'w': 20}
'''
def s4():
    
    from collections import defaultdict;
    import itertools;
    N , K = map( int, input().split() );
    Sdit = defaultdict( int );
    basic = { 'a','c','i','n','t' };
    basicNum = 5
    # s4_1 : 복붙 과정에서 누락.
    if( K < 5 ):
        print( 0 );
        return;
    
    lst = set();
    vocab = { k:v for v, k in enumerate( set( map( chr, range( ord( 'a' ), ord( 'z' ) + 1 ) ) ) - basic ) }
    for i in range( N ):
        temp = 0;
        for char in set( input() ) - basic:
            num = ( 1 << vocab[ char ] ) ;
            temp |= num;
            lst.add( num )
        Sdit[ temp ] += 1;
    
    k = K - basicNum;

    cmb = list( itertools.combinations( lst , k ) );
    # s4_2 반례 : 2 25 antatica antaztica --> 내 결과: 0 정답 : 2
    if( len( lst ) < k ):
        print( N );
        return;
    Mx = 0;
    
    print( cmb );
    print( "Sdit", Sdit )
    for case in cmb:
        cnt = 0;
        
        tmp = sum( case );
        print( tmp )
        print( bin( tmp ) )
        for idx in Sdit:
            if( idx & tmp == idx ):
                cnt += Sdit[ idx ];
        
        Mx = max( Mx, cnt );
            
    print( Mx );
    return;
    
s4()

