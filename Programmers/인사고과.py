# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:43:52 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(scores):
    from collections import defaultdict;
    #x 기준점
    wanho = scores[ 0 ];
    x, y = 0, 1;
    tg_sum = sum( wanho );
    
    new_score = list( sorted( [ i for i in scores if sum( i ) >= tg_sum ], key = lambda x: ( -x[ 0 ], x[ 1 ]) ) );
    answer = 1;
    standard = 0;
    for score in new_score:
        if( wanho[ x ] < score[ x ] and wanho[ y ] < score[ y ] ):
            return -1;
        
        if( standard <= score[ y ] ):
            if( tg_sum < score[ x ] + score[ y ] ):
                answer += 1;
            
            standard = score[ 1 ];
    return answer;
            
    '''
    print( dp );
    print( lst );
    '''
'''
#WA 40
def solution(scores):
    wanho = scores[ 0 ];
    from collections import defaultdict;
    
    ddit = defaultdict( set );
    sum_ = defaultdict( int );
    for score in scores:
        ddit[ sum( score ) ].add( tuple( score ) );
        sum_[ sum( score ) ] += 1;
    keys = list( sorted( ddit.keys(), key = lambda x: -x ) );
    now = 1;
    maxA , maxB = max( [ i[ 0 ] for i in scores ] ), max( [ i [ 1 ] for i in scores ] );
    
    dimen2dp = [ [ 0 ] * ( maxB + 1 ) for x in range( maxA + 1 ) ];
    
    for key in keys:
        
        for x, y in ddit[ key ]:
            if( dimen2dp[ x ][ y ] == -1 ):
                #이미 과락시.
                if( x == wanho[ 0 ] and y == wanho[ 1 ] ):
                    return -1;
                
                continue;
            
            if( x == wanho[ 0 ] and y == wanho[ 1 ] ):
                return now;
            
            for nx in range( x ):
                for ny in range( y ):
                    dimen2dp[ nx ][ ny ] = -1;
            
            
        now += sum_[ key ];
                
                
'''        
    
    
    
    
'''
#WA 44
def solution(scores):
    from collections import defaultdict;
    
    ddit = defaultdict( int );
    
    for score in scores:
        ddit[ sum( score ) ] += 1;
    
    checkerA = list( sorted( scores , key = lambda x: ( x [ 0 ], x[ 1 ] ) ) );
    checkerB = list( sorted( scores , key = lambda x: ( x [ 1 ], x[ 0 ] ) ) );
    

    
    keys = list( sorted( ddit.keys(), key = lambda x: -x ) );
    wanho = sum( scores[ 0 ] );
    if( keys[ -1 ] == wanho and keys[ 0 ] != wanho ):
        return -1;
    
    now = 1;
    
    for key in keys:
        if( key == wanho ):
            break;
        now += ddit[ key ];
    
    
    return now;
''' 
'''
# heap WA 44
def solution(scores):

    #1년 인사고과 -> 인센티브
    
    #근무태도 + 동료평가 기록 -> 두 점수 모두 낮을 시 인센티브 받지 x
    
    #두 점수 합이 높은 순으로 석차 > 동일시 동석차 15// 15 1등2명 --> 3등

    answer = 1;


    wanho = sum( scores[ 0 ] );
    
    
    import heapq;
    
    tst = [];
    
    heapq.heapify( tst );
    
    for i in scores:
        
        heapq.heappush( tst, -1 * sum( i ) );
    
    if( tst[ -1 ] == -1 * wanho and tst[ 0 ] != -1 * wanho ):
        return -1;
    
    while tst:
        val = tst[ 0 ];
        if( val == -1 * wanho ):
            return answer;
        
        while tst and val == tst[ 0 ]:
            heapq.heappop( tst );
            answer += 1;
        
    
        
        
    return len( scores );
    
    '''