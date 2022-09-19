# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 16:33:26 2022
@FileName: 20438.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/20438
"""
N,K,Q,M = map( int, input().split() );


Ks = list( map( int, input().split() ) )


Qs = list( map( int, input().split() ) )

# 15% TimeOut
def getNum( Nums ):
    global Ks,Qs

    Qset = set( Qs )

    Kset = set( Ks )

    Qset = Qset.difference( Kset );
    
    lst = []

    for num in Qset:
        lst = lst + [ i for i in range( num, N + 3, num ) if Nums[ 0 ] <= i <= Nums[ -1 ] ]
        
    lstset = set( lst );

    lstset = lstset.difference( Kset );



    print( len( Nums ) - len( lstset ) )
    
    
    
selst = [];
for i in range( M ):
    S,E = map( int, input().split() );
    selst.append( ( S,E ) )
    
for i in range( M ):
    Nums = [ i for i in range( selst[ i ][ 0 ], selst[ i ][ 1 ] + 1 ) ]
    
    getNum( Nums )
def t2():
    
    N, K, Q, M = map( int, input().split() );
    
    Ks = list( map( int, input().split() ) );
    
    Qs = list( map( int, input().split() ) );
    
    
    dp = [ 0 ] * ( N + 3 );
    
    Qset, Kset = set( Qs ), set( Ks );
    
    Qset = Qset.difference( Kset );
    
    for k in Kset:
        dp[ k ] = 1;
    
    for i in range( 3, N + 3 ):
        dp[ i ] = dp[ i - 1 ] + dp[ i ];
        flag = True;
        for q in Qset:
            if( i % q == 0 ):
                flag = False;
        
        if( flag ):
            dp[ i ] += 1;
    
        
        
    
    for i in range( M ):
        S,E = ( map( int, input().split() ) );
        
        
        
        print(  dp[ E ] - dp [ S+ 1 ]  );
        
def t3_dp():
    # A
        
    N, K, Q, M = map( int, input().split() );

    Ks = list( map( int, input().split() ) );

    Qs = list( map( int, input().split() ) );


    dp = [ 0 ] * ( N + 3 );

    Qset, Kset = set( Qs ), set( Ks );

    Qset = Qset.difference( Kset );

    attendance = [ 0 ] * ( N + 3 );

    for student_num in Qset:
        for student in range( student_num, N + 3, student_num ):
            if( student not in Kset ):
                
                attendance[ student ] = 1;
        
    for i in range( 3, N + 3 ):
        if( attendance[ i ] ):
            dp[ i ] = dp[ i - 1 ]
        else:
            dp[ i ] = dp[ i - 1 ] + 1


    for i in range( M ):
        S,E = ( map( int, input().split() ) );
        
        
        
        print(  dp[ E ] - dp[ S - 1 ] );
        
        
        


        

