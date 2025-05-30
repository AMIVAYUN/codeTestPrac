# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:06:30 2023
@FileName: 1,2,3 떨어트리기.py
@author: YUNJUSEOK
@Link:https://school.programmers.co.kr/learn/courses/30/lessons/150364
"""
answer = [];
def getlist( order, cons, target ):
    ans = [];
    idx = 0;
    
    while idx < len( order ):

        num = 1;
        if( cons[ order[ idx ] ] == 1 ):
            ans.append( target[ order[ idx ] ] );
            cons[ order[ idx ] ] = 0;
            target[ order[ idx ] ] = 0;
            idx += 1;
            continue;
        while ( cons[ order[ idx ] ] - 1 ) * 3 < target[ order[ idx ] ] - num:
            num += 1;
        cons[ order[ idx ] ] -= 1;
        target[ order[ idx ] ] -= num;
        ans.append( num );
        idx += 1;
    
    return ans;
    
    
def isOk( target, cons, leaves ):
    
    
    for leaf in leaves:
        if( cons[ leaf ] <= target[ leaf ] <= 3 * cons[ leaf ] ):
            continue;
        else:
            return True;
    
    return False;

    
def solution(edges, target):
    global answer;
    from collections import defaultdict, deque;
    
    graph = defaultdict( list );
    
    for edge in edges:
        graph[ edge[ 0 ] - 1 ].append( edge[ 1 ] - 1);
    context = defaultdict( list );
    root = 0;
    leaves = [];
    keys= graph.keys()
    for key in keys:
        for node in graph[ key ]:
            if( node not in keys ):
                leaves.append( node );
    
    for key in keys:
        context[ key ] = [ 0, len( graph[ key ] ) ];
        graph[ key ] = list( sorted( graph[ key ] ) );
        
    cons = [ 0 ] * len( target );
    order = deque();

    flag = True;
    res = 0;
    frequency = defaultdict( int );
    while flag:

        dq = deque();
        subflag = isOk( target, cons, leaves );

        if subflag == False:
    
            break;
            
        
            
        dq.append( ( 0 ) );
        
        while dq:
            pos = dq.popleft();
   
            if( pos in leaves ):
                if( cons[ pos ] + 1 > target[ pos ] ):
                    flag = False;
                    res = pos;
                    break;
                
                cons[ pos ] += 1;
                order.append( pos );

                break;
            
            next = graph[ pos ][ context[ pos ][ 0 ] ];
            context[ pos ] = [ ( context[ pos ][ 0 ] + 1 ) % context[ pos ][ 1 ], context[ pos ][ 1 ]  ]
            
            dq.append( next );
    
    for leaf in leaves:
        if( leaf == res ):
            continue;
        
        if( cons[ leaf ] * 3 < target[ leaf ] ):
            return [-1];
        
    lst = getlist( order, cons, target );
    
    return lst;
    '''
    
    5를 123 3번만에  3 1 1 // 2 2 1 
    
    '''
   
   
'''
#SOL2 TIMEOUT 28.0
def dfs2( idx, order, now, cons, target, leng ):
    global answer;
    

    if( len( now ) >= len( answer ) ):
        return;
    if( target == cons ):

        answer = now[:]
        return;
    
    for i in range( 1, 4 ):
        if( idx + 1 <= leng and ( cons[ order[ idx ] - 1 ] + i <= target[ order[ idx ] - 1 ] ) ):
            now.append( i );
            cons[ order[ idx ] - 1 ] += i;
            dfs2( idx + 1, order, now, cons, target, leng );
            now.pop();
            cons[ order[ idx ] - 1 ] -= i;
    
            
def solution(edges, target):
    global answer;
    from collections import defaultdict, deque;
    
    graph = defaultdict( list );
    
    for edge in edges:
        graph[ edge[ 0 ] ].append( edge[ 1 ] );
    context = defaultdict( list );
    root = 1;
    leaves = [];
    keys= graph.keys()
    for key in keys:
        for node in graph[ key ]:
            if( node not in keys ):
                leaves.append( node );
    for key in keys:
        context[ key ] = [ 0, len( graph[ key ] ) ];
        graph[ key ] = list( sorted( graph[ key ] ) );
        
    cons = [ 0 ] * len( target );
    order = deque();

    flag = True;
    res = 0;
    while flag:

        dq = deque();
        
        dq.append( ( 1 ) );
        
        while dq:
            pos = dq.popleft();
   
            if( pos in leaves ):
                if( cons[ pos - 1 ] + 1 > target[ pos - 1 ] ):
                    flag = False;
                    res = pos;
                    break;
                    
                cons[ pos - 1 ] += 1;
                order.append( pos );
                break;
            
            next = graph[ pos ][ context[ pos ][ 0 ] ];
            context[ pos ] = [ ( context[ pos ][ 0 ] + 1 ) % context[ pos ][ 1 ], context[ pos ][ 1 ]  ]
            
            dq.append( next );
    
    #못가는지 검증
    for leaf in leaves:
        if( leaf == res ):
            continue;
        
        if( cons[ leaf - 1 ] * 3 < target[ leaf - 1 ] ):
            return [-1];
    
    answer = [ 3 ] * ( len( order ) + 1 ) 
    # 있는 것 필요한것 idx( order의 현재위치 ) , 전역변수 answer
    dfs2( 0, order, [], [ 0 ] * len( target ), target, len( order ) )
    
    return answer;
    
'''

'''
#SOL1 WA

def dfs( target, now, cons ,idx, leng, order ):
    
    global answer;
    
    if( len( answer ) < len( now ) ):
        return;
    
    if( cons == now[ 1: ] ):
        answer = cons;
        return;
    
    
    for i in range( 1, 4 ):
        if( cons[ order[ idx ] ] + i <= target[ order[ idx ] - 1 ] ):
            now.append( i );
            cons[ order[ idx ] ] += i;

            dfs( target, now, cons, ( idx + 1 ) % leng, leng, order );

            cons[ order[ idx ] ] -= i;
            now.pop();
        
 '''   
def solution(edges, target):
    '''
    트리의 1번 노드에 1 2 3 중 하나를 계속 떨어트려 리프노드에 숫잘 쌓음
    
    모든 간선은 부모가 자식을 가리킴
    ** 현재 길로 연결된 자식노드 다음으로 번호가 큰 자식 노드로 기존의 길은 끊는다.
    
    ** 현재 길로 연결된 노드 번호가 가장 크면 가장 작은 노드로 설정
    
    길이 하나라면 계속 하나의 길로
    
    리프 노드까지 떨어진 후에 새로운 숫자를 떨어트려야 함
    
    목표 : 리프노드에 쌓인 숫자 합을 target과 같게 만드는 것
    
    모든 경우중 * 가장 적은 숫자를 사용하여 * 사전 순으로 가장 빠른 경우
    
    
    14잖아
    
    
    
    '''
    '''
    global answer
    
    from collections import defaultdict;
    
    graph = defaultdict( list );
    
    for edge in edges:
        graph[ edge[ 0 ] ].append( edge[ 1 ] );
    
    root = 1;
    leaves = [];
    keys= graph.keys()
    for key in keys:
        for node in graph[ key ]:
            if( node not in keys ):
                leaves.append( node );
    
    leavcnt = len( leaves );
    
    context = defaultdict( list );
    
    for key in keys:
        context[ key ] = [ 0, len( graph[ key ] ) ];
        graph[ key ] = list( sorted( graph[ key ] ) );
    
    checker = [ 0 ] * ( len( target ) + 1 );
    frequency = defaultdict( int );
    from collections import deque;
    
    
    order = deque();
    
    while sum( checker ) < len( target ):
        dq = deque();
    
        dq.append( ( 1 ) );
        
        while dq:
            pos = dq.popleft();
            checker[ pos ] = 1;
            if( pos in leaves ):
                frequency[ pos ] += 1;
                order.append( pos );
                break;
            
            next = graph[ pos ][ context[ pos ][ 0 ] ];
            context[ pos ] = [ ( context[ pos ][ 0 ] + 1 ) % context[ pos ][ 1 ], context[ pos ][ 1 ]  ]
            
            dq.append( next );
           
    
    print( order,frequency );
    
    
    leng = len( order );
    answer = [ 1 ] * ( leng * max( target ) + 1 );
    start = 0;
    cons = [ 0 ] * ( len( target ) + 1 );
    dfs( target, [], cons ,0, leng, order );
    
    
    return answer;
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return answer
    '''