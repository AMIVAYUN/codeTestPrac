# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:28:49 2022
@FileName: 수식 최대화.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/67257
"""


def add( a, b ):
    return a + b;
def sub( a, b ):
    return a - b;
def mul( a, b ):
    return a * b;
def solution(expression):
    operating = { "+": add,"-": sub,"*": mul }
    import itertools;
    dit = { "0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0 }
    oper = [];
    operand = [];
    str0 = ""
    for i in expression:
        if( i not in dit ):
            operand.append( int( str0 ) );
            oper.append( i );
            str0 = ""
        else:
            str0 += i ;
    operand.append( int( str0 ) ) ;
    oper1 = list( set( oper ) );
    case = list( itertools.permutations( oper1, len( oper1 ) ) )
    answer = []
    
    for i in case:
        suboper,suboperand = oper[ : ], operand[ : ]
        for j in i:
            while j in suboper:
                idx = suboper.index( j, 0, len(suboper) );
                suboperand[ idx ] = operating[ j ]( suboperand[ idx ], suboperand[ idx + 1 ] );
                suboperand.pop( idx + 1 );
                suboper.pop( idx );
                
        answer.append( abs( suboperand[0] )  );
            
        
            
   
    
    return max( answer )