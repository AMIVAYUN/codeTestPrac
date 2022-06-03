# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:54:58 2022
@FileName: 다트게임.py
@author: YUNJUSEOK
@lINK: https://programmers.co.kr/learn/courses/30/lessons/17682
"""


lst = [];
num = "";
idx = -1;
def solution(dartResult):
    global lst, idx, num;
    cond = False;
    dit = { 'S': single, 'D': double, 'T':triple,'*':star,'#': out };
    for i in dartResult:
        if( i not in dit ):
            if( not( cond ) ):
                idx += 1;
                cond = True;
            num += i;
        
        else:
            if( cond ):
                lst.append( int( num ) );
                num = "";
                dit[ i ]();
                cond = False;
            else:
                dit[ i ]();
       
                
            
    answer = sum( lst );     
        
    return answer

def single():
    global lst,idx;
    lst[ idx ] *= 1;

def double():
    global lst,idx;
    lst[ idx ] **= 2;

def triple():
    global lst,idx;
    lst[ idx ] **= 3;

def star():
    global lst,idx;
    if( idx == 0 ):
        lst[ idx ] *= 2;
    else:
        lst[ idx -1 ] *=2;
        lst[ idx ] *= 2;
def out():
    lst[ idx ] *= -1;
    
    