# -*- coding: utf-8 -*-
"""
Created on Wed May 17 18:54:27 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

'''

떡 장수 동희는 매일 갓 만든 떡 팖

떡 1 ~ 9

호랑이 전날에 먹었던 떡 먹지 않음.

N일 동안 떡을 팔러 장터에 나감.

재료 공급 사정에 따라 종류가 매일 달라짐.

N일 동안 호랑이에게 잡아먹히지 않도록 떡을 골라줄 것


'''
import sys;

sys.setrecursionlimit(int(1e6));


def Print():
    global dp, r_day, N;
    for i in range(N):
        for rc in r_day[i]:
            if (dp[i][rc] == 1):
                print(rc);
                break;


# SOL1 9% WA
'''
def dfs( day ):
    global dp, r_day, flag, N;
    if flag : return;
    if( day == N ):
        flag = True;
        Print();
        return;


    for rc in r_day[ day ]:
        if( dp[ day ][ rc ] > -1 ):
            continue;

        if day > 0:
            stan = dp[ day - 1 ][ rc ] < 0;
        else:
            stan = True;
        if(  stan and not flag ):
            dp[ day ][ rc ] = 1;
            dfs( day + 1 );
            dp[ day ][ rc ] = 0;

'''


def dfs(day, stack ):
    global dp, r_day, flag, N;
    if flag: return;
    if (day == N):
        flag = True;
        for i in stack:
            print( i );
        return;

    for rc in r_day[day]:
        if( flag ):
            break;
        if (dp[day][rc] > 0 ):
            continue;
        if( len( stack ) and stack[ -1 ] == rc ):
            continue;


        dp[day][rc] = 1;
        stack.append( rc )
        dfs(day + 1, stack );
        stack.pop();


flag = False;

N = int(input());

r_day = {};

for i in range(N):
    rice_cakes = list(map(int, input().split()))[ 1: ];

    r_day[i] = rice_cakes;

dp = [[ 0 ] * 10 for _ in range(N)];

dfs(0, [] );

if flag == False:
    print(-1);



