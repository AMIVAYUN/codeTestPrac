# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:45:23 2022
@FileName: 크레인 인형 뽑기.py
@author: YUNJUSEOK

@Link: https://programmers.co.kr/learn/courses/30/lessons/64061
"""
from collections import deque;
def solution(board, moves):
    dit = { 1:deque( [ i[0] for i in board if i[ 0 ] > 0] ),2:deque( [ i[1] for i in board if i[1] > 0 ] ),3:deque( [ i[2] for i in board if i[ 2 ] > 0 ] ),4:deque( [ i[ 3 ] for i in board if i[ 3 ] > 0 ] ),5:deque( [ i[ 4 ] for i in board if i[ 4 ] > 0 ] ) }
    answer = 0;
    lst = [];
    for i in moves:
        if( dit[ i ] ):
            if( lst ):
                const = lst.pop();
                val = dit[ i ].popleft();
                if( const == val ):
                    answer +=2;
                else:
                    lst.append( const );
                    lst.append( val );
            else:
                lst.append( dit[ i ].popleft() );
                    
                
            
                
            
   
    
  
    
    return answer
solution( [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]] ,[1,5,3,5,1,2,1,4])


from collections import deque;
def solution(board, moves):
    dit = {};
    for i in range( len( board ) ):
        dit[ i + 1 ] = deque( [ j[i] for j in board if j[ i ] > 0 ] ) 
    answer = 0;
    lst = [];
    for i in moves:
        if( dit[ i ] ):
            if( lst ):
                const = lst.pop();
                val = dit[ i ].popleft();
                if( const == val ):
                    answer +=2;
                else:
                    lst.append( const );
                    lst.append( val );
            else:
                lst.append( dit[ i ].popleft() );
                    
                
            
                
            
   
    
  
    
    return answer