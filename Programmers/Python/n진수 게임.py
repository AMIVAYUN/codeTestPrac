# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:38:20 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def getNnumber( num, n ):
    
    if( num == 0 ):
        return ['0'];
    ans = [];
    dit = { 0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    while num != 0:
        
        num, mod = divmod( num, n );
        
        ans.append( dit[ mod ] );
        
    ans.reverse();
    return ans;
        
    
    
    

def solution(n, t, m, p):
    #n진법의 숫자 t개를 m명이서 말하는 데 내 순서는 p번째;
    answer = [];
    p -= 1;
    
    lst = [];

    for i in range( 0, m*t + 1 ):
        lst += getNnumber( i, n );
    count = 0;
    idx = p;
    while count < t and idx < len( lst ) :
        answer.append( lst[ idx ] )
        idx += m;
        count += 1;

    
    
    return ''.join( answer );

