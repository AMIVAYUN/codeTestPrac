# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 17:29:15 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
'''
임의의 k점에 대하여 더 많이 맞춘 선수가 점수를 가져감. + 동점시 어피치 꺼


라이언은 가장 큰 점수차로 이기고 싶다.

배열 [ 10 to 1 idx에 따른 점수 분포]

'''

    
lion = {};
apeech = {};
cases = [];
answer = [];
items = [];
Mx = 0;

def getDiff( lst ):
    global apeech;
    checker = {};
    s_lion = 0;
    
    for item in lst:
        checker[ item[ 0 ] ] = 1;
        s_lion += item[ 0 ];
    
    s_apeech = 0;
    for key in apeech:
        if( apeech[ key ] > 0 and key not in checker ):
            s_apeech += key;
            
    
    return s_lion - s_apeech;
    
        
        

def getCases( remain, lst ):
    global cases,items,Mx, answer;

    val = getDiff( lst )
    if( Mx < val ):
        
        Mx = val
        answer = lst[:];
    #이 부분을 놓쳐서 헤맸다
    elif( Mx == val ):
        print( answer, lst )
        suma , sumb = sum( [ i [ 0 ] * i[ 1 ] for i in answer ] ), sum( [ i[ 0 ] * i[ 1 ] for i in lst ] );
        
        if( suma > sumb ):
            answer = lst[:];
    
    
    if( remain == 0 ):
        return;
    else:
        for item in items:
            if( item not in lst and remain >= item[ 1 ] ):
                lst.append( item );
                getCases( remain - item[ 1 ], lst );
                lst.remove( item );
    


def solution(n, info):
    global answer, apeech, lion, cases,items,Mx;
    
    idx = 10;
    
    for inf in info:
        lion[ idx ] = inf + 1;
        
        apeech[ idx ] = inf;
        
        idx -= 1;
    
    lion.pop( 0 );
    items = list( lion.items() );
    

    getCases( n, [] );
    
    if( Mx == 0 ):
       return [ -1 ];
    result = [ 0 ] * 11;
    for case in answer:
        result[ 10 - case[ 0 ] ] = case[ 1 ];
        
    pad = n - sum( result );
    
    if( result[ 10 ] == 0 ):
        result[ 10 ] = pad;
    
    return result
'''
solution( 5,	[2,1,1,1,0,0,0,0,0,0,0] )

solution( 10, [0,0,0,0,0,0,0,0,3,4,3])
'''
solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1] )