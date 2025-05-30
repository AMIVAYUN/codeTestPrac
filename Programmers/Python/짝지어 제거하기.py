# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 21:24:36 2022
@FileName: 짝지어 제거하기.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12973
"""
str0 = "baabaa" 
# 초기 로직 : 해당 로직은 결국 str0를 한번 더 쭉 탐색하는 연산이 있기에 O(N²)이다. 그래서 효율성에서 떨어졌다.
for i in str0:
    if( i * 2 in str0 ):
        print( i * 2 )
        str0 = str0.replace(i * 2, "" )
        
        
print( str0 )
str2 = "aa"
str3 = "a"


# STACK을 활용하여 좀 더 효율적으로 풀 수 있었다.
def solution(s):
    s = list( s );
    stack = [ s[ 0 ] ];
    for i in s[ 1: ]:
        if len( stack ) > 0 and i == stack[ -1 ]:
            stack.pop();
        else:
            stack.append( i );
        
            
    return int( len ( stack ) == 0 ) 
    
solution( "baabaa")

