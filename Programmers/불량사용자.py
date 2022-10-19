# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:54:12 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


answer = set()
def getRs( depth, ddit ,patterns, lst ):
    global answer;
    if( depth == len( patterns ) ):
        tmp = tuple( sorted( lst ) );
        answer.add( tmp );
        return;
    
    for str0 in ddit[ patterns[ depth ] ]:
        if( str0 not in lst ):
            lst.append( str0 );
            getRs( depth + 1 , ddit, patterns, lst );
            lst.pop();
    
            
def solution(user_id, banned_id):
    import re;
    from collections import defaultdict; 
    global answer;
    ddit = defaultdict( set );
    
    
    
    patterns = [];
    for ban_id in banned_id:
        
        tmp = ban_id.split( '*' );
        
        pattern = '.'.join( tmp );
        
        patterns.append( pattern );


    
    
    for pattern in patterns:
        
        for user in user_id:
            
            if( re.match( pattern, user ) != None and len( pattern ) == len( user )):
                ddit[ pattern ].add( user );
    
    
    getRs( 0, ddit, patterns, [] )
    
   
    
    return len( answer );