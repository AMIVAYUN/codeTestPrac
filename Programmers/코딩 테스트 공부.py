# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 13:10:34 2022
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
'''
def dfs( nowal, nowco , Mx, problems, val ):
    global answer;
    
    if( nowal >= Mx[ 0 ] and nowco >= Mx[ 1 ] ):
        answer = min( answer, val );
        return;
    
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        if( alp_req <= nowal and cop_req <= nowco ):
            dfs( nowal + alp_rwd, nowco + cop_rwd, Mx, problems, cost + val )
    
        else:
            diff_al = alp_req - nowal if alp_req - nowal > 0 else 0;
            diff_co = cop_req - nowco if cop_req - nowco > 0 else 0;
            dfs( nowal + alp_rwd, nowco + cop_rwd, Mx, problems, cost + val + diff_al + diff_co );
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
'''
'''
def solution(alp, cop, problems):
    Mxalp,Mxcop = 0, 0;
    
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        Mxalp = max( Mxalp, alp_req );
        Mxcop = max( Mxcop, cop_req );
    
    dp = [ [ i + _ for _ in range( Mxcop + 1 )] for i in range( Mxalp + 1 ) ];
 
    for x in range( alp + 1 ):
        for y in range( cop + 1 ):
            dp[ x ][ y ] = 0;
    
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        startx, starty = alp_req, cop_req;

        
        while startx <= Mxalp and starty <= Mxcop:
            
            dp[ startx ][ starty ] = min( dp[ startx ][ starty ], dp[ startx - alp_rwd ][ starty - cop_rwd ] + cost )
                
            
            startx += alp_rwd;
            starty += cop_rwd;
            
            
        
        
            
    
    for row in dp:
        print( row );
    
    return dp[ -1 ][ -1 ]
    

'''
def solution(alp, cop, problems):
    Mxalp,Mxcop = 0, 0;
    
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        Mxalp = max( Mxalp, alp_req );
        Mxcop = max( Mxcop, cop_req );
    if Mxalp <= alp:
        alp = Mxalp
    if Mxcop <= cop:
        cop = Mxcop
    dp = [ [ float('inf') for _ in range( Mxcop + 1 )] for i in range( Mxalp + 1 ) ];
    dp[ alp ][ cop ] = 0;
    for x in range( alp, Mxalp + 1 ):
        for y in range( cop, Mxcop + 1 ):
            
            if( x + 1 <= Mxalp ):
                dp[ x + 1 ][ y ] = min( dp[ x + 1 ][ y ], dp[ x ][ y ] + 1 );
            if( y + 1 <= Mxcop ):
                dp[ x ][ y + 1 ] = min( dp[ x ][ y + 1 ], dp[ x ][ y ] + 1 );
            
    
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if( x >= alp_req and y >= cop_req ):
                    nextx = x + alp_rwd if x + alp_rwd <= Mxalp else Mxalp;
                    nexty = y + cop_rwd if y + cop_rwd <= Mxcop else Mxcop;
                
                    dp[ nextx ][ nexty ] = min( dp[ nextx ][ nexty ], dp[ x ][ y ] + cost );
    

    return dp[ Mxalp ][ Mxcop ];
                
            
                
            
            
        
        
            

    