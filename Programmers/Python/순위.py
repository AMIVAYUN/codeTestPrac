# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:04:53 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(n, results):
    from collections import defaultdict
    if( n == 1 ):
        return 1;
    answer = 0
    win_graph = defaultdict(set)    # key가 이긴 애들
    lose_graph = defaultdict(set)   # value가 이긴 애들 --> key가 진 애들
    
    for x, y in results:
        win_graph[ x ].add( y );
        lose_graph[ y ].add( x );
    
    '''
    ** 모순 없다. 
    
    value가 이긴 친구들은 key도 이긴 것
    
    key가 진 애들은 value들이 진 애들 한테도 진 것
    
    
    '''
    
    from collections import deque;
    
    for key in range( 1, n + 1 ):
        winq, loseq = deque( win_graph[ key ]), deque( lose_graph[ key ] );
        win_checker = [ 0 ] * ( n + 1 );
        lose_checker = [ 0 ] * ( n + 1 );
        
        for val in win_graph[ key ]:
            win_checker[ val ] = 1;
        
        for val in lose_graph[ key ]:
            lose_checker[ val ] = 1;
            
        
        while winq:
            val = winq.popleft();
            win_graph[ key ].update( win_graph[ val ] );
            for next in win_graph[ val ]:
                if( win_checker[ next ] == 0 ):
                    win_checker[ next ] = 1;
                    winq.append( next );
        '''
        A가 B한테 짐
        
        B가 진 애들은 당연히 A는 이김
        
        A가 진 애들은 B는 이김
        '''
        while loseq:
            val = loseq.popleft();
            lose_graph[ key ].update( lose_graph[ val ] );
            for next in lose_graph[ val ]:
                if( lose_checker[ next ] == 0 ):
                    lose_checker[ next ] = 1;
                    loseq.append( next );
        
        
        if( len( win_graph[ key ] ) + len( lose_graph[ key ] ) == n - 1 ):
            answer += 1;
    

    #SOL 1 WA 
    '''
    from collections import deque;
    for key in range( 1, n + 1 ):
        
        for val in list( win_graph[ key ] ):
            win_graph[ key ].update( win_graph[ val ] );
            
        
        for val in list( lose_graph[ key ] ):
            
            lose_graph[ key ].update( lose_graph[ val ] );
            
        if key in lose_graph[ key ]:
            
            lose_graph[ key ].remove( key ) ;
        if key in win_graph[ key ]:
            
            win_graph[ key ].remove( key ) ;
        
        if( len( win_graph[ key ]) + len( lose_graph[ key ] ) == n - 1 ):
            answer += 1;
    
    print( win_graph, lose_graph );
        
    '''
    
    return answer
    

solution( 5, [[4,3],[4,2],[3,2],[1,2],[2,5]])
    