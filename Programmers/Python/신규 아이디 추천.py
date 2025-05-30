# -*- coding: utf-8 -*-
"""
Created on Fri May 27 12:33:31 2022
@FileName: 신규 아이디 추천.py
@author: YUNJUSEOK

@link: https://programmers.co.kr/learn/courses/30/lessons/72410
"""


def solution(new_id):
    new_id = new_id.lower();
    new_id = list( new_id )
    
    
    new_id = [ i for i in new_id if  i.isalnum() or i in [ '-','.','_']  ]
    new_id = ''.join( i for i in new_id );

    while( '..' in new_id ):
      new_id = new_id.replace( '..' , '.' );
    

        
    new_id = new_id[ 1: ] if new_id[0] == '.' and len(new_id) > 1 else new_id;
    new_id = new_id[ :len( new_id ) -1 ] if new_id[ -1 ] == '.' else new_id
    
    new_id = "a" if len( new_id ) < 1 else new_id;
    
    if( len( new_id ) >= 16 ):
        new_id = new_id[ :15 ];
        if( new_id[-1] =='.'):
            new_id = new_id[ :-1 ];
    if( len( new_id ) < 3 ):
        new_id = new_id + ( new_id[-1] * ( 3 - len( new_id ) ) )
        
    return ''.join( i for i in new_id );

print( solution("z-+.^.") )