# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 10:05:36 2022
@FileName: 4386.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/4386

도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.

별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
모든 별들은 별자리 위의 선을 통해 서로 
직/간접적으로 이어져 있어야 한다.
별들이 2차원 평면 위에 놓여 있다. 
선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때,
 별자리를 만드는 최소 비용을 구하시오



첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)

둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 
실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다. 
좌표는 1000을 넘지 않는 양의 실수이다.


첫째 줄에 정답을 출력한다. 절대/상대 오차는 10-2까지 허용한다.



"""
def find( x ):
    global parent;
    
    if( parent[ x ] != x ):
        parent[ x ] = find( parent[ x ] );
        
    return parent[ x ];

def union( x, y ):
    global parent;
    
    root_x, root_y = find( x ), find( y );
    
    if( root_x < root_y ):
        parent[ root_y ] = x;
    else:
        parent[ root_x ] = y;

    return;

def getDist( a, b ):
    return ( ( a[ 0 ] - b[ 0 ] ) **2 + ( a[ 1 ] - b[ 1 ] ) **2 ) **0.5

n = int( input() );

stars =[];

for i in range( n ):
    x, y = map( float, input().split() );
    x *= 1000;
    y *= 1000;
    
    stars.append( ( x, y ) )
    
    
import itertools
lst = [ i for i in range( n ) ]
cmb = list( itertools.combinations( lst, 2 ) )

vertex = [];

for case in cmb:
    vertex.append( (  case[ 0 ] , case[ 1 ] , getDist( stars[ case[ 0 ] ], stars[ case[ 1 ] ] ) ) )

vertex = sorted( vertex, key = lambda x: x[ 2 ] );
total = 0;
parent = [ i for i in range( n ) ]
for v in vertex:
    a, b, cost = v;
    
    if( find( a ) != find( b ) ):
        total += cost;
        union( a, b )

total = '{0:.2f}'.format(total/1000)


print( total )
