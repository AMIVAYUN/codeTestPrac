# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:23:46 2022
@FileName: 시저암호.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12926
"""
def solution(s, n):
    lst = [ ord( i ) + n if i != ' ' else ord( i ) for i in s ];
    answer = '';
    for i in lst:
        if i == 32:
            answer += chr( i )
            continue;
        else:
            if not( 65<=i<=90 or 97<=i<=112  ):
                i -= 26;
                answer += chr( i );
            else:
                answer += chr( i );

    return answer

#예외처리가 잘못되었다 AaZz

def solution(s, n):
    answer = ""
    lst = [ ord( i ) for i in s ];
    for i in lst:
        if i == 32:
            answer += chr( i );
        elif i <= 90:
            i += n;
            if( i > 90 ):
                i -= 26;
            answer += chr( i );
        else:
            i += n;
            if( i > 122 ):
                i -= 26;
            answer += chr( i );
    return answer;


print( solution("AaZz", 25 ) );

print( ord( "Z" ) );