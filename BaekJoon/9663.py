# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:32:27 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

N  = int( input() );

cnt = 0;

col = [ 0 ] * ( N + 1 );

def nqueens_1( depth, col ):
    global N, cnt;
    if( isOk( depth, col ) ):
        if( depth == N ):
            cnt += 1;
        else:
            for j in range( 1, N + 1 ):
                tmp = col[:]
                tmp[ depth + 1 ] = j;
                nqueens( depth + 1 , tmp );
def nqueens( depth ):
    global N, cnt;
    if( depth == N ):
        cnt += 1;
    else:
        for j in range( 1, N + 1 ):
            
            col[ depth + 1 ] = j;
            if( isOk( depth + 1 ) ):
                nqueens( depth + 1 );
            
            col[ depth + 1 ] = 0;
def isOk( depth ):
    cons = True;
    for i in range( 1, depth ):
        if( not( cons ) ):
            break;
        if( col[ depth ] == col[ i ] or abs( col[ i ] - col[ depth ] ) == abs( i - depth ) ):
            cons = False;
    
    return cons;


nqueens( 0  )

print( cnt )

n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)  