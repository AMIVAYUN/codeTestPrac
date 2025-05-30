# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 14:43:30 2022
@FileName: 체육복.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/42862
"""
#1차 7,12,13,14 실패
def solution(n, lost, reserve):
    cp = dict.fromkeys( reserve[:], True);
    cpl = dict.fromkeys( lost[:], True );
    for i in lost:
        
        if( ( i - 1 ) in cp ):
            cp.pop( i - 1 );
            cpl.pop( i );
            
        elif( ( i + 1 ) in cp ):
            cp.pop( i + 1 )
            cpl.pop( i );
    
    
    return n - len( cpl );


#timeout
Mx = 0;
def dfs(cnt, lost, reserve, chk ):
    global Mx;
    import copy;
    if( len( lost ) == 0 or len( reserve ) == 0 or chk):
        Mx = max( cnt, Mx );
        return;
    for i in lost:
        cpl = copy.deepcopy( lost );
        cpr = copy.deepcopy( reserve ); 
        if( ( i - 1 ) in reserve ):
            
            a = cpl.pop( i );
            b = cpr.pop( i - 1 );
            dfs( cnt + 1, cpl, cpr , False );
            cpl[ i ] = a;
            cpr[ i - 1 ] = b;
        if( ( i + 1 ) in reserve ):
            a = cpl.pop( i );
            b = cpr.pop( i + 1 );
            dfs( cnt + 1, cpl, cpr , False );
            cpl[ i ] = a;
            cpr[ i + 1 ] = b;
    dfs( cnt, lost, reserve, True );

def solution2(n, lost, reserve):
    n1 = n - len( reserve ) - len( lost );
    dfs( 0, dict.fromkeys( lost[:],0), dict.fromkeys( reserve[:],0),False);
    
    print( Mx + n1 + len( reserve ) )
    
solution2( 5,[ 2,4 ], [ 1, 3, 5 ] )



# 문제를 잘 읽자 단순 그리디에서 조건을 다 안 읽어서 틀린거나 다름 없다. 7,13,14 틀림.

def solution(n, lost, reserve):
    for i in lost:
        if i in reserve:
            idx0 = lost.index( i, 0, len( lost ) );
            idx1 = reserve.index( i, 0, len( reserve ) );
            lost.pop( idx0 );
            reserve.pop( idx1 );
    
    setL = set( lost );
    setR = set( reserve );
    ditL = { i : 0 for i in lost };
    ditR = { r : 0 for r in reserve };
    
    for i in lost:
        if( ( i - 1 ) in ditR ):
            del ditL[ i ];
            del ditR[ i - 1 ];
        elif( ( i + 1 ) in ditR ):
            del ditL[ i ];
            del ditR[ i + 1 ];
    
    return n - len( ditL );    

# 예시중에 sorted가 안된것이 있었다.

def solution(n, lost, reserve):
    ditL = { i : 0 for i in lost };
    ditR = { r : 0 for r in reserve };
    
    for i in ditL :
        if i in ditR:
            ditL[ i ] = 1;
            ditR[ i ] = 1;
    
    ditL = { i: 0 for i in ditL if not( ditL[ i ] ) }
    ditR = { i: 0 for i in ditR if not( ditR[ i ] ) }
    
    
    
    for i in sorted( ditR ):
        if( ( i - 1 ) in ditL ):
            ditL.pop( i - 1 ) ;
        elif( ( i + 1 ) in ditL ):
            ditL.pop( i + 1 );
           

    return n - len( ditL );