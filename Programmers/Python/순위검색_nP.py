# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:48:11 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
def foundlen( dit, query ):
    score = int( query[ -1 ] )
    key = "".join( query[ :-1 ] );
    
    lst = dit[ key ];
    
    lt = 0; rt = len( lst );
    ans = 0;
    while lt <= rt:
        
        mid = (lt + rt) // 2
        
        if( mid < len( lst ) and score <= lst[ mid ] ):
            rt= mid - 1;
        else:
            lt = mid + 1;
            ans = lt
    print( key, dit[ key ], ans )
    return len( lst[ ans: ] );
    
    
import itertools;

def solution( info, query ):
    info_lst = [ tuple( i.split() ) for i in info ]
    dit = {};
    
    for i in info_lst:
        score = int( i[ -1 ] );
        
        keys = list( i[ :-1 ] );
        
        for i in range( 5 ):
            case = itertools.combinations( [ 0,1,2,3] , i );
            
            for j in case:
                temp = keys[ : ];
                for idx in j:
                    temp[ idx ] = "-";
                key = "".join( temp );
                if key in dit:
                    dit[ key ].append( score );
                else:
                    dit[ key ] = [ score ];
    
    for val in dit.values():
        val.sort();
        
    
    
    query_lst = [ tuple( i.replace( "and", " " ).split() ) for i in query ]
    answer = []
    
    for i in query_lst:
        len_ = foundlen( dit, i );
        answer.append( len_ )
    
    
    return answer;

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])