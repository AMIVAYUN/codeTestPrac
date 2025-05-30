# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 18:17:53 2022
@FileName: 조이스틱.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/42860

"BBABAAAABBBAAAABABB" 26
"BBAAAAAABBBAAAAAABB" 20
"BBBAAAAAAAB" 8
"ABAAAAAAAAABB" 7
"BBAABB" 8
"BBBAAAAABAAAAAAAAAAA" 12
"BAAAAAAAAAABAAAAAABB" 13
"AAABBAB" 7
"""


dit = { chr( 65 + i ): min( abs( 65 - ( 65 + i ) ), abs( 91 - ( 65 + i ) ) ) for i in range( 0, 26 ) }
def bfs( start, target ):
    from collections import deque;
    global dit;
    
    
    Mxlen = len( start );
    
    deq = deque();
    
    start, target = list( start ), list( target );
    
    
    deq.append( (start, 0, 0, 0, 0) );
    ans = [];
    while deq:
        
        now, mvcnt,wordcnt , words, pos = deq.popleft();
        wordcnt+= dit[ target[ pos ] ];
        now[ pos ] = target[ pos ];
        words += 1;
        
        if( ''.join( i for i in now ) == ''.join( j for j in target ) ):
            print( mvcnt, wordcnt )
            ans.append( ( mvcnt + wordcnt) );
            continue;
            
        if( words >= Mxlen ):
            if( ''.join( i for i in now ) == ''.join( j for j in target ) ):
                ans.append(  ( mvcnt + wordcnt)  );
                continue;
            continue;
        
        
        
        nextPos1 = ( pos + 1 ) 
        if( nextPos1 == Mxlen ):
            nextPos1 = 0;
            
            
            
        nextPos2 = ( pos - 1 )
        
        deq.append( ( now[:], mvcnt + 1, wordcnt , words , nextPos1 ) );
        
        if( nextPos2 < 0 ):
            nextPos2 = Mxlen - 1;
        
        
        
        
        deq.append( ( now[:], mvcnt + 1,wordcnt ,words , nextPos2 ) );
        
        
    return ans
            
        
 #   59.3
def getName( name, target ):
    global dit;
    if( name == target ):
        return 0
    name, target = list( name ),list(target );
    temp = name[:]
    cnt = 0;
    rs = [];
    if( name[ 0 ] != target[ 0 ] ):
        cnt += dit[ target[ 0 ] ];
        name[ 0 ] = target[ 0 ]
        temp[ 0 ] = target[ 0 ]
    recnt = cnt;
    #정방향
    for i in range( 1, len( name ) ):
        cnt += 1;
        
        cnt += dit[ target[ i ] ];
        name[ i ] = target[ i ]
        
        if( ''.join( i for i in name ) == ''.join( i for i in target ) ):
            rs.append( cnt );
            break;
        
    recnt += 1
    for i in range( len( name ) -1, 0, -1 ):
        recnt += dit[ target[ i ] ];
        temp[ i ] = target[ i ];
        
        if( ''.join( i for i in temp ) == ''.join( i for i in target ) ):
            rs.append( recnt );
            break;
        recnt += 1;
    return min( rs );
        
        
def solution(name):
    start = "A" * len( name );
    #answer = getName( start, name );
    ans = bfs( start, name );
    print( min( ans ) )
    return min( ans );

def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min(min_move, i + i + len(name) - next)
    answer += min_move
    return answer
