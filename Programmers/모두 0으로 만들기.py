parent = [];


def bfs(graph, start, depths):
    global parent;
    from collections import deque;

    dq = deque();

    visit = [1] * len(graph);
    visit[start] = 0;
    dq.append((start, 0));

    while dq:
        now, depth = dq.popleft();

        for next in graph[now]:
            if (visit[next]):
                visit[next] = 0;
                parent[next] = now;
                depths[next] = depth + 1;
                dq.append((next, depth + 1));

    return depths;


def solution(a, edges):
    global parent;

    answer = 0;

    leng = len(a);

    parent = [i for i in range(leng)];
    graph = [[] for _ in range(leng)];

    depths = [0] * leng;

    # 루트 기반 트리 만들기
    for edge in edges:
        x, y = edge;

        graph[x].append(y);
        graph[y].append(x);

    depths = bfs(graph, 0, depths);

    nodes = [[i, depths[i]] for i in range(leng)];

    nodes = list(sorted(nodes, key=lambda x: -x[1]));

    answer = 0;
    for node in nodes[:-1]:
        idx, depth = node;
        pidx = parent[idx];
        a[pidx] += a[idx];
        answer += abs(a[idx]);
        a[idx] = 0;

    return answer if a[0] == 0 else -1


'''
sol1 wa
def find( x ):
    global parent;


    if( parent[ x ] != x ):
        return find( parent[ x ] );

    return parent[ x ];

def findDepth( x, depth ):
    global parent;

    if( parent[ x ] != x ):

        return findDepth( parent[ x ], depth + 1 );

    return depth;

def union( x, y ):
    px, py = find( x ), find( y );
    if( x > y ):
        parent[ px ] = py;
    else:
        parent[ py ] = px;

    return;


def solution(a, edges):
    global parent;

    answer = 0;

    leng = len( a );

    graph = [ [] for _ in range( leng ) ];

    parent = [ i for i in range( leng ) ];

    nodes = [ ( i ,0 ) for i in range( leng ) ];

    # 루트 기반 트리 만들기
    for edge in edges:
        x, y = edge;

        union( x , y );

    #각 노드별 depth 저장.
    for idx in range( leng ):
        depth = findDepth( idx, 0 );

        nodes[ idx ] = ( idx, depth );

    #연산 

    nodes = list( sorted( nodes, key = lambda x: -x[ 1 ] ) );
    print( parent );
    for node in nodes[ : -1 ]:
        i, depth = node;

        answer += abs( a[ i ] );

        a[ parent[ i ] ] += a[ i ];
        a[ i ] = 0;
        print( a , answer);    

    if( a[ 0 ] != 0 ):
        return -1
    else:
        return answer;









    return answer
'''
