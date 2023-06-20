# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 23:06:39 2023

@author: 주석
"""

'''

숫자 구매를 위해 준비한 금액 >> M원

문방구에서 파는 숫자 0 ~ N - 1 

i 가격 Pi

항상 원하는 만큼 숫자 구매 가능

방번호가 0이 아니면 0으로 시작 불가


'''


N = int( input() );

Ps = list( map( int, input().split() ) );

M = int( input() );

Mx = 0;

dp = [-float("inf") for _ in range(M+1)]

for i in range( N - 1, -1, -1 ):
    print( dp );
    p = Ps[i]
    for j in range(p, M+1):
        dp[j] = max( dp [ j ], i, dp[ j - p ] * 10 + i );
print( dp [ M ] )
            