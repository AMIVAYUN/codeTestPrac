# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:39:00 2022
@FileName: 1987.py
@author: YUNJUSEOK
@link : https://www.acmicpc.net/problem/1987

"""
dx = [ 0, 0, -1, 1 ]
dy = [ 1, -1, 0, 0 ]
R, C = map( int, input().split() )
lst = [];
context = [False] * 26;
cnt = 0;
def main():
    global lst, R, C, context;
    
    
    for y in range( R ):
        lst.append( list( input() ) )
    context[ ord( lst[0][0]) - 65  ] = True
    dfs( 0, 0, 0 );
    print( cnt );
def dfs(cnt1, x, y ):
    global lst, R, C,context, cnt;
    
    cnt1 += 1;
    
    cnt = max( cnt1, cnt );
    
    
    
    for i in range( 4 ):
        
        
        
        if( x + dx[ i ] >=0 and x + dx[ i ] < C and y + dy[ i ]>=0 and y + dy[ i ] < R and not( context[ ord( lst[ y + dy[ i ]][ x + dx[ i ] ]) - 65  ] ) ):
            context[ ord( lst[ y + dy[ i ]][ x + dx[ i ] ]) - 65  ] = True
            
            dfs( cnt1, x + dx[ i ], y + dy[ i ] );
            
            context[ ord( lst[ y + dy[ i ]][ x + dx[ i ] ]) - 65  ] = False
        
        
     

      
            
            
if(__name__ == "__main__" ):
    main();
