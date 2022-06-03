###### -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:23:21 2022
@FileName: 2606.py
@author: YUNJUSEOK
@Link : https://www.acmicpc.net/problem/2606
@Desc : 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
        1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
@Input : 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
         둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
         이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
         

"""

#처음 로직

'''
메모리 초과가 낫다.
'''
import sys;
sys.setrecursionlimit( int(1e6) );


count = 0;
dit2 = {};
def getPos( key ):
    global dit2;
    if( dit2[ key ] == 1 ):
        dit2[ key ] = 0;
        return 1;
    else:
        return 0;


def getCount( dit, key ):
    global count;
    global dit2;
    if( not( dit.keys().__contains__( key )  ) ):
        return;
    count += getPos( key );
    lst = dit.get( key );
    for i in lst:
        if( not( dit.keys().__contains__( i ) ) ):
            count += getPos( i );
        else:
            getCount( dit, i );
            
        



def main():
    global count;
    global dit2;
    lenC = int( input() );
    lenN = int( input() );
    dit = {};
    
    for i in range( lenN ):
        a, b = map( int, input().split() )
        if( dit.keys().__contains__( a ) ):
            dit[a].append( b );
        else:
            dit[a] = [ b ];

    for j in range( lenC ):
        dit2[ j + 1 ] = 1;
    dit2[1] = 0;
    
    getCount( dit, 1 );

    print( count );

if( __name__=="__main__"):
    main();



#정답 로직
import sys;
sys.setrecursionlimit( int(1e6) );


lenC = int( input() );
lenN = int( input() );
lst = [ [0] * ( lenC + 1 ) for i in range( lenC + 1 )]

visit = [1] * ( lenC + 1 );
visit[ 0 ] = 1;
    
for i in range( lenN ):
    a, b = map( int, input().split() )
    lst[ a ][ b ] = 1;
    lst[ b ][ a ] = 1;

count = 0;

def getCount2( key ):
    global count, lenC, lst, visit;
    for i in range( lenC + 1 ):
        print( key );
        if( lst[ key ][ i ] == 1 ):
            count += visit[ i ];
            visit[ i ] = 0;
            lst[ key ][ i ] = 0;
            getCount2( i );

getCount2( 1 );

print( count - 1 );