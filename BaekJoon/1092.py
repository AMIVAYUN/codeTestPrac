# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:30:31 2023

@author: 주석

지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 
모든 화물은 박스에 안에 넣어져 있다. 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다.
 모든 크레인은 동시에 움직인다.

각 크레인은 무게 제한이 있다.
 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 
 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.


counter

3
10 6 5
11
6 8 9 6 8 6 9 6 8 6 9

//6


"""

'''

sol1 


3

10 6 5

11

6 8 9 6 8 6 9 6 8 6 9
[10, 6, 5]
deque([9, 9, 9, 8, 8, 8, 6, 6, 6, 6, 6])
deque([9, 9, 8, 8, 8, 6, 6, 6, 6, 6])
deque([9, 8, 8, 8, 6, 6, 6, 6, 6])
deque([8, 8, 8, 6, 6, 6, 6, 6])
deque([8, 8, 6, 6, 6, 6, 6])
deque([8, 6, 6, 6, 6, 6])
deque([6, 6, 6, 6])
deque([6, 6])
8

역순 정렬은 답이 아님. 항상 최적해를 찾는 것이 매우 중요

from collections import deque;


N = int( input() );


cranes = list( map( int, input().split() ) );


M = int( input() );


boxes = list( map( int, input().split() ) );

# 역순 정렬
cranes = list( sorted( cranes, key = lambda x: -x  ) );

# 역순 정렬
boxes = deque( sorted( boxes, key = lambda x: -x ) );
flag = True;
if( boxes[ 0 ] > cranes[ 0 ] ):
    flag = False;



now = 0;
time = 0;

while boxes and flag:
    print( boxes )
    for i in range( N ):
        if( len( boxes ) == 0 ):
            break;
        if( cranes[ i ] < boxes[ 0 ] ):
            break;
        
        boxes.popleft();
    
    

    time += 1;


print( time if flag else -1 );


'''

from collections import deque;
import bisect;

N = int( input() );


cranes = list( map( int, input().split() ) );


M = int( input() );


boxes = list( map( int, input().split() ) );

# 역순 정렬
cranes = list( sorted( cranes ) );

# 역순 정렬
boxes = list( sorted( boxes ) );
flag = True;
if( boxes[ -1 ] > cranes[ -1 ] ):
    flag = False;



now = 0;
time = 0;

while boxes and flag:

    idx = 0;
    while boxes and idx < N:
        target = cranes[ idx ];
        pos = bisect.bisect_right( boxes, target) - 1;
        
        if( pos == -1 ):
            idx += 1;
            continue;
        
        boxes.pop( pos );
        idx += 1;

    

    time += 1;


print( time if flag else -1 );

