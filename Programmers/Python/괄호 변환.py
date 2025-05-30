# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:24:14 2022
@FileName: 괄호 변환.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/60058
"""
'''
() 개수 맞으면 균형 괄호
() 의 짝까지 모두 맞으면 올바른 괄호
input => 비었으면 빈 문자열
        입력을 균형 괄호 2개로 분리. ( u, v )
        u는 균형잡힌 문자열 & v는 빈 문자열 가능
        u가 올바르면 v에 대ㅐㅎ 1부터 다시 수행
        
        - v가 비었으면 '('를 붙힘
        - 문자열 v에 대해 1단계부터 다시 수행 
        - ')'를 다시 붙힘
        - u의 첫번째와 마지막 문제 제거후 나머지 문자열의 괄호 방향을 뒤집음
        - 생성된 문자열 반환
        
'''
'''
() 개수 맞으면 균형 괄호
() 의 짝까지 모두 맞으면 올바른 괄호
input => 비었으면 빈 문자열
        입력을 균형 괄호 2개로 분리. ( u, v )
        u는 균형잡힌 문자열 & v는 빈 문자열 가능
        u가 올바르면 v에 대ㅐㅎ 1부터 다시 수행
        
        - v가 비었으면 '('를 붙힘
        - 문자열 v에 대해 1단계부터 다시 수행 
        - ')'를 다시 붙힘
        - u의 첫번째와 마지막 문제 제거후 나머지 문자열의 괄호 방향을 뒤집음
        - 생성된 문자열 반환
        
'''
def isBalanced( p ):
    dit = { '(': 0 , ')': 0}
    for i in p:
        dit [ i] += 1;
    
    return dit['('] == dit[ ')']
def iscorrect( p ):
    if( len( p ) == 0 ):
        return False;
    if( p[0] == ')'):
        return False;
    dit = { '(':')' }
    stack = [ p[ 0 ] ];
    idx = 1;
    while idx < len( p ):
        
        if( len( stack ) != 0  ):
            val = stack.pop();
            if( dit[ val ] == p[ idx ] ):
                idx += 1;
            else:
                stack.append( val );
                stack.append( p[ idx ] );
                idx += 1;
        elif( len( stack ) == 0 and p[ idx ] != '(' ):
            return False;
        else:
            stack.append( p[ idx ] ) 
            idx+=1;
        
    return len( stack ) == 0
        
        
        
def getUv( p ):
    dit = { '(' : 0, ')' : 0 }

    dit [ p[ 0 ] ] += 1;
    
    for i in range( 1, len( p ) ):
        dit[ p[ i ] ] += 1;
        if( dit[ ')' ] == dit[ '(' ] ):
            return p[ : i + 1 ] , p [ i + 1: ]
        
def solution(p):
    print( p )
    mapper = { '(': ')', ')':'('}
    lenx = len( p )
    answer = ""
    
    if( lenx == 0 ):
        return p;
    if( iscorrect( p ) ):
        return p;
    
    u,v = getUv( p );
    if( iscorrect( u ) ):
        answer += u + solution( v );
    else:
        answer += '('+ solution( v ) + ')';
        for ch in u[ 1: -1 ]:
            answer += mapper[ ch ];
        
    return answer

