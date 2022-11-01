# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 12:08:01 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

import sys;
sys.setrecursionlimit( int( 1e6 ) );
'''
def dfs( nowal, nowco ,alp, cop, problems, cost ):
    global answer;

    if( cost > answer ):
        return ;
    if( nowal >= alp and nowco >= cop ):
        answer = min( answer, cost );
        return;
    
    if( nowal < alp ):
        diff = alp - nowal;
        dfs( alp, nowco, alp, cop, problems, cost + diff );
    if( nowco < cop ):
        diff = cop - nowco;
        
        dfs( nowal, cop, alp, cop, problems, cost + diff );
    
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        diff_alp = 0;
        diff_cop = 0;
        
        if( nowal < alp_req ):
            diff_alp = alp_req - nowal;
        
        if( nowco < cop_req ):
            diff_cop = cop_req - nowco;
        
        dfs( alp_req + alp_rwd, cop_req + cop_rwd, alp, cop, problems, cost + diff_alp + diff_cop );
        
    return
'''
def dfs( nowal, nowco , Mx, problems, val ):
    print( nowal, nowco, Mx, problems, val );
    
    global answer;
    
    if( nowal >= Mx[ 0 ] and nowco >= Mx[ 1 ] ):
        answer = min( answer, val );
        return;
    
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        if( alp_req <= nowal and cop_req <= nowco ):
            dfs( nowal + alp_rwd, nowco + cop_rwd, Mx, problems, cost + val )
    
    
    return
    
    
answer = 0;
def solution(alp, cop, problems):
    global answer ;
    idx = 0;
    
    while idx < len( problems ):
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[ idx ];
        if( ( alp_rwd + cop_rwd ) / cost <= 1 ):
            problems.pop( idx );
            continue;
            
        idx += 1;
        
    Mnx = min( [ problems[ i ][ 0 ] for i in range( len( problems ) ) ] );
    Mny = min( [ problems[ i ][ 1 ] for i in range( len( problems ) ) ] );
    
    Mxx = max( [ problems[ i ][ 0 ] for i in range( len( problems ) ) ] );
    Mxy = max( [ problems[ i ][ 1 ] for i in range( len( problems ) ) ] );
    
    answer = Mxx  + Mxy - ( alp + cop ) ;
    cost = 0;
    if( alp < Mnx ):
        cost += Mnx - alp;
        alp = Mnx;
    
    if( cop < Mny ):
        cost += Mny - cop;
        cop = Mny;
        
    
    dfs( alp, cop, ( Mxx, Mxy ), problems, cost );
    
    return answer

#solution(10,	10,	[[10,15,2,1,2],[20,20,3,3,4]])

solution( 	0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]] )

print( answer )