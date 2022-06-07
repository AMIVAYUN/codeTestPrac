# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 12:30:16 2022
@FileName: 타겟 넘버.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/43165
"""


answer = 0
mx = 0;
target = 0;
nums = [];
def dfs( depth, num ):
    global nums,target,mx,answer;
    if( depth == mx ):
        if(  num == target ):
            answer +=1;
            
        
        return;
    
    
    dfs( depth + 1, num + nums[ depth ] );
    
    dfs( depth + 1, num - nums[ depth ] );
    
    return

def solution(numbers, tg):
    global nums, target,answer, mx;
    mx = len( numbers );
    nums = numbers;
    target = tg;
    answer = 0;
    
    dfs( 0, 0 )
    
    
    return answer

lst =[ 'ABCDAADEF' ]

str0 = ""
for i in lst[0]:
    if( i not in str0 ):
        print( i, str0 )
        str0 += i 

print( str0 )