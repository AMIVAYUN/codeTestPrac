# -*- coding: utf-8 -*-
"""
Created on Mon May 30 14:11:08 2022
@FileName: 숫자풀이 영단어.py
@author: YUNJUSEOK
"""



        


def solution(s):
    answer = "";
    dit2 = {};
    dit = {'zero': '0','one': '1', 'two': '2', 'three':'3', 'four':'4', 'five': '5', 'six':'6', 'seven': '7', 'eight':'8','nine' : '9',
       '0':'0','1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6' ,'7' : '7', '8' : '8', '9': '9'
       }
    str0 = ""
    for i in dit:
        if i in s:
            dit2[ dit[ i ]]= s.index( i ) 
    
    dit2 = sorted( dit2.items(), key = lambda x: x[ 1 ]  )
    
    for i in dit2:
        answer += i[ 0 ];
    
     
    return int( answer )


print( solution( "111111111" ) )

def solution2(s):
    answer = "";
    lst = [];
    dit = {'zero': '0','one': '1', 'two': '2', 'three':'3', 'four':'4', 'five': '5', 'six':'6', 'seven': '7', 'eight':'8','nine' : '9',
       '0':'0','1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6' ,'7' : '7', '8' : '8', '9': '9'
       }
    for i in dit:
        if i in s:
            
            for j in range( s.count( i ) ):
                con = ( dit[ i ], s.index( i ) );
                
                while( con in lst ):
                    con = ( dit[ i ], s.index( i, con[1] + 1, len( s ) ) );
                    
                lst.append( con );
                
            
                
    
    lst = sorted( lst, key = lambda x : x[ 1 ]  );
    
    for i in lst:
        answer += i[ 0 ];

        
    return int( answer )


solution2( "100" ) 
