# -*- coding: utf-8 -*-
"""
Created on Mon May 23 13:44:24 2022
@FileName: 2667.py
@author: YUNJUSEOK

https://www.acmicpc.net/problem/2667

단지번호붙이기

문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

"""
# 2667
k = int( input() );
ex = [];
for i in range( k ):
    ex.append( list( map( int, input() ) ) )
    
    
posx = [ 0, 0, -1, 1 ];
posy = [ 1, -1, 0, 0 ];

lst = [];
count = 0;
def main():
    global count;
    
    
    
    for i in range( k ):
        for j in range( k ):
            if( dfs(  i, j ) ):
                lst.append( count );
                count = 0;
    b = len( lst ); 
    print( b );
    for i in range( b ):
        
        print(  sorted( lst ) [ i ] )
        

def dfs( m, n ):
    global ex;
    global count;
    
    if( n < 0  or m < 0 or m >= k or n >= k ):
        return False;
    if( ex[m][n] ==0 ):
        return False;
    else:
        count += ex[ m ][ n ];
        ex[ m ][ n ] = 0;
        for i in range( 4 ):
            m_ = m + posx[ i ];
            n_ = n + posy[ i ];
            
            dfs(  m_, n_ );
        return True;
    
    


if( __name__ == "__main__"):
    main();