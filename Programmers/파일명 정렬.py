# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:10:25 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

'''
    head -> 사전순 정렬 전부 소문자 화
    
    number -> 숫자 순 정렬
    
    
    '''
def solution( files ):
    import re;
    from collections import defaultdict;
    answer = [];
    checker = [ str(i) for i in range( 10 ) ]
    pos = 0;
    ddit = defaultdict( tuple );
    for file in files:
        idx = 0;
        
        while idx < len( file ):
            if( file[ idx ] in checker ):
                break;
                
            idx += 1
            
        n_idx_end = idx;
        
        while n_idx_end < len( file ):
            if( file[ n_idx_end ] not in checker ):
                break;
            
            n_idx_end += 1;
            
        
        head = file[ :idx ].lower();
        
        number = file[ idx: n_idx_end ];
        
        
        ddit[ file ] = ( head, number, pos );
        
        
        pos += 1;
    
    lst = ddit.items();
    
    lst = list( sorted( lst, key = lambda x: ( x[ 1 ][ 0 ], int( x[ 1 ][ 1 ] ), x[ 1 ][ 2 ] ) ) )
    
    
    answer = [];
    
    for i in lst:
        answer.append( i[ 0 ] );
        
        
    return answer;
''' 
def solution( files ):
    import re;
    from collections import defaultdict;
    answer = [];
    ddit = defaultdict( list );
    idx = 0;
    for file in files:
        test = re.match( '([a-zA-Z]?)(.*)([0-9]+)([a-zA-Z]?)', file ).group()
        new = re.split( '([a-zA-Z]+)[-]*', test )
        
        new = new[ 1: ];
        
        ddit[ file ].append( ( new[ 0 ].lower(), new[ 1 ], idx ) );
    
        idx += 1;
    lst = ddit.items();
    
    lst = sorted( lst , key = lambda x: ( x[ 1 ][ 0 ][ 0 ], int( x[ 1 ][ 0 ][ 1 ] ), x[ 1 ][ 0 ][ 2 ] ) ); 
    
    for lang in lst:
        answer.append( lang[ 0 ] );
        
        

        
    
    return answer;
'''
'''
# SOL1;
def solution(files):
    
    from collections import defaultdict;
    
    ddit = defaultdict( list );
    for ch in files:
        origin = ch[:];
        ch = ch.lower();
        idx = 0;
        n_idx = 0;
        
            
            # HEAD 찾기
            
        while idx < len( ch ) and ch[ idx ] != '-' and not ( ch[ idx ].isnumeric() ):
            idx += 1;
            n_idx += 1;
        flag = False;
        #Num찾기
        if( ch[ idx ] == '-' ):
            flag = True;
            idx += 1;
        while n_idx < len( ch ) and ch[ n_idx ].isnumeric():
            n_idx += 1;
            
        if( flag ):
            
            ddit[ origin ].append( ( ch[ : idx - 1 ] , ch[ idx+1: n_idx ] ) );
        
        else:
            if( ch[ idx: n_idx ] == "" ):
                number = float("inf");
            else:
                number = int( ch[ idx: n_idx ] );
            ddit[ origin ].append( ( ch[ : idx ] , number ) );
    
    lst = ddit.items();

    
    lst = list( sorted( lst , key = lambda x: ( x[ 1 ][ 0 ][ 0 ], x[ 1 ][ 0 ][ 1 ] )) )
  
    answer = [];
    
    for i in lst:
        answer.append( i[ 0 ] )
    return answer
    
    '''