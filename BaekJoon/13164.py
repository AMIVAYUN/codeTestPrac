# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:09:25 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


'''
행복 유치원 원장인 태양이는 어느 날 N명의 원생들을 키 순서대로 일렬로 줄 세우고, 총 K개의 조로 나누려고 한다. 각 조에는 원생이 적어도 한 명 있어야 하며, 
같은 조에 속한 원생들은 서로 인접해 있어야 한다. 조별로 인원수가 같을 필요는 없다.

이렇게 나뉘어진 조들은 각자 단체 티셔츠를 맞추려고 한다. 
조마다 티셔츠를 맞추는 비용은 조에서 가장 키가 큰 원생과 가장 키가 작은 원생의 키 차이만큼 든다. 
최대한 비용을 아끼고 싶어 하는 태양이는 K개의 조에 대해 티셔츠 만드는 비용의 합을 최소로 하고 싶어한다.
 태양이를 도와 최소의 비용을 구하자.
'''
# 반례 5 3
#1 100 101 102 103
'''
N, K = map( int, input().split() );

lst = list( map( int, input().split() ) );

sum_ = 0;

k = ( N + 1 ) // K;

for idx in range( 0, N, k ):
    temp = lst[ idx: idx + k ];
    
    sum_ += ( temp[ -1 ] - temp[ 0 ] );
    
    print( sum_, temp );
print( sum_ )
'''
'''
sum_ = float( "inf" );
def dfs( cnt, Mn, idx ):
    global sum_, lst, K, k;
    if( cnt == 0 ):
        
        if( idx == len( lst ) ):
            sum_ = min( sum_, Mn );
        
        return;
        
    for offset in range( 1, k + 1 ):
        if( idx + offset <= len( lst ) ):
            temp = lst[ idx: idx + offset ];
            off = temp[ -1 ] - temp[ 0 ];
            Mn += off;
            
            dfs( cnt - 1, Mn, idx + offset );

            Mn -= off;
    
N, K = map( int, input().split() );

k = ( N + 1 )//K;

lst = list( map( int, input().split() ) );


dfs( K, 0, 0 );

print( sum_ );

'''
N, K = map( int, input().split() );
lst = list( map( int, input().split() ) );

lst_ = list( sorted( [ lst[ i + 1 ] - lst[ i ] for i in range( len( lst ) - 1  ) ] ) );

print( sum( lst_[ : len( lst_ ) - ( K - 1 ) ] ) );