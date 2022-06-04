# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 21:20:03 2022
@FileName: 오픈채팅방.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/42888
"""




namespace = {};
def enter( uid ):
    global namespace;
    msg = namespace[ uid ]+"님이 들어왔습니다."
    return msg;
def leave( uid ):
    global namespace;
    msg = namespace[ uid ]+"님이 나갔습니다."
    return msg;
def solution(record):
    dit = {"Enter": enter , "Leave": leave}
    answer = [];
    global namespace;
    from collections import deque;
    deq = deque();
    for i in record:
        tmp = i.split( " " );
        if ( tmp[ 0 ] in dit ):
            deq.append( (tmp[ 0 ], tmp[ 1 ] ) )
            if( tmp[ 0 ] == 'Enter' ):
                namespace[ tmp[ 1 ] ] = tmp[ 2 ];
        else:
            namespace[ tmp[ 1 ] ] = tmp[ 2 ];
    while deq:
        proc = deq.popleft();
        msg = dit[ proc[ 0 ] ]( proc[ 1 ] )
        answer.append( msg );
    
    
    return answer