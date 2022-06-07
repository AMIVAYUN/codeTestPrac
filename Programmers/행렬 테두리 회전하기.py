# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 13:30:02 2022
@FileName: 행렬 테두리 회전하기.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/77485
"""

    
def getRotate( query ):
    import copy;
    global answer,lst;
    answer.append( lst[ query[ 0 ] ][query[ 1 ] ] )
    lst2 = copy.deepcopy( lst );
    for i in range( query[ 1 ] + 1, query[ 3 ] + 1 ):
        lst[ query[ 0 ] ][ i ] = lst2[ query[ 0 ] ][ i - 1 ];
    for i in range( query[ 0 ] + 1 , query[ 2 ] + 1 ):
        lst[ i ][ query[ 3 ] ] = lst2[ i - 1 ][ query[ 3 ] ];
    for i in range( query[ 3 ] - 1 , query[ 1 ] - 1, -1 ):
        lst[ query[ 2 ] ][ i ] = lst2[ query[ 2 ] ][ i + 1 ];
    for i in range( query[ 2 ] -1, query[ 0 ] - 1 , -1):
        lst[ i ][ query[ 1 ] ] = lst2[ i + 1 ][ query[ 1 ] ];




def getRotate( query ):
    import copy;
    global answer,lst;
    init = lst[ query[ 0 ] ][ query[ 1 ] ] 
    mapper = lst[ query[ 0 ] ][ query[ 1 ] : query[ 3 ] + 1 ] + [ lst[ i ][ query[ 3 ] ] for i in range( query[ 0 ] + 1, query[ 2 ] + 1 ) ] + lst[ query[ 2 ] ][ query[ 3 ]: query[ 1 ] -2 : -1 ] + [ lst[ i ][ query[ 1 ] ] for i in range( query[ 2 ] , query[ 0 ] ,-1 )]
    mapper = [ mapper[ -1 ] ] + mapper[ : len( mapper ) -1 ]
    print( mapper )
    lst2 = copy.deepcopy( lst );
    for i in range( query[ 1 ] + 1, query[ 3 ] + 1 ):
        lst[ query[ 0 ] ][ i ] = lst2[ query[ 0 ] ][ i - 1 ];
        if ( init > lst2[ query[ 0 ] ][ i - 1 ]):
            init = lst2[ query[ 0 ] ][ i - 1 ]
    for i in range( query[ 0 ] + 1 , query[ 2 ] + 1 ):
        lst[ i ][ query[ 3 ] ] = lst2[ i - 1 ][ query[ 3 ] ];
        if( init > lst2[ i - 1 ][ query[ 3 ] ] ):
            init = lst2[ i - 1 ][ query[ 3 ] ]
    for i in range( query[ 3 ] - 1 , query[ 1 ] - 1, -1 ):
        lst[ query[ 2 ] ][ i ] = lst2[ query[ 2 ] ][ i + 1 ];
        if( init > lst2[ query[ 2 ] ][ i + 1 ] ):
            init =  lst2[ query[ 2 ] ][ i + 1 ];
    for i in range( query[ 2 ] -1, query[ 0 ] - 1 , -1):
        lst[ i ][ query[ 1 ] ] = lst2[ i + 1 ][ query[ 1 ] ];
        if( init > lst2[ i + 1 ][ query[ 1 ] ]):
            init = lst2[ i + 1 ][ query[ 1 ] ];
    
    answer.append( init );
    return
def getRotate( query ):
    import copy;
    global answer,lst;
    init = lst[ query[ 0 ] ][ query[ 1 ] ] 
    
    
    
    mapper = lst[ query[ 0 ] ][ query[ 1 ]: query[ 3 ] + 1 ] 
    for i in range( query[ 0 ], query[ 2 ] ):
        if( lst[ i ][ query [ 3 ] ] not in mapper ):
            mapper.append( lst[ i ][ query[ 3 ] ] )
    

    mapper += lst[ query[ 2 ] ][ query[ 3 ] : query[ 1 ] -1 : -1 ]
    for i in range( query[ 2 ], query[ 0 ] - 1, -1 ):
        if lst[ i ][ query [1 ] ] not in mapper:
            mapper.append( lst[ i ][ query [ 1 ] ] )
    
    
    print( mapper )
    idx = 0;
    

    for i in range( query[ 1 ], query[ 3 ] + 1 ):
        print( query[ 0 ], i )
        lst[ query[ 0 ] ][ i ] = mapper[ idx ];
        if ( init > mapper[ idx ] ):
            init = mapper[ idx ]
        idx +=1;
        
        
      
    for i in range( query[ 0 ] + 1 , query[ 2 ] ):
        print( i,query[ 3 ] )
        lst[ i ][ query[ 3 ] ] = mapper[ idx ];
        
        if( init > mapper[idx] ):
            init = mapper[idx]
        idx +=1;  
    
     
    for i in range( query[ 3 ] , query[ 1 ] - 1, -1 ):
        print(  query[ 2 ], i )
        lst[ query[ 2 ] ][ i ] = mapper[idx];
        if( init > mapper[idx] ):
            init =  mapper[idx];
        idx += 1;
    for i in range( query[ 2 ] - 1, query[ 0 ] , -1):
        print( i, query[ 1 ])
        lst[ i ][ query[ 1 ] ] = mapper[ idx ];
        if( init > mapper[idx] ):
            init = mapper[ idx ];
        idx+=1;
    
    answer.append( init );
    return
        
        
               


solution( 6,6,[[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])


## 정답 로직


def getRotate( query ):
    import copy;
    global answer,lst,lst2;
    init = lst[ query[ 0 ] ][ query[ 1 ] ] 
    
    for i in range( query[ 1 ] + 1, query[ 3 ] + 1 ):
        lst[ query[ 0 ] ][ i ] = lst2[ query[ 0 ] ][ i - 1 ];
        if ( init > lst2[ query[ 0 ] ][ i - 1 ]):
            init = lst2[ query[ 0 ] ][ i - 1 ]
    for i in range( query[ 0 ] + 1 , query[ 2 ] + 1 ):
        lst[ i ][ query[ 3 ] ] = lst2[ i - 1 ][ query[ 3 ] ];
        if( init > lst2[ i - 1 ][ query[ 3 ] ] ):
            init = lst2[ i - 1 ][ query[ 3 ] ]
    for i in range( query[ 3 ] - 1 , query[ 1 ] - 1, -1 ):
        lst[ query[ 2 ] ][ i ] = lst2[ query[ 2 ] ][ i + 1 ];
        if( init > lst2[ query[ 2 ] ][ i + 1 ] ):
            init =  lst2[ query[ 2 ] ][ i + 1 ];
    for i in range( query[ 2 ] -1, query[ 0 ] - 1 , -1):
        lst[ i ][ query[ 1 ] ] = lst2[ i + 1 ][ query[ 1 ] ];
        if( init > lst2[ i + 1 ][ query[ 1 ] ]):
            init = lst2[ i + 1 ][ query[ 1 ] ];
    
    answer.append( init );
    lst2 = [ i[:] for i in lst ]

    return
lst = []
answer = [];
lst2 = [];
def solution(rows, columns, queries):
    global answer, lst, lst2;
    import copy;
    
    lst = [ [] for i in range( rows ) ] 
    
    for i in range( rows ):
        for j in range( 1, columns + 1 ):
            #row로 해서 틀렸었다.
            
            lst[ i ].append( (i * columns) + j );
    queries = [ [ j - 1 for j in i ] for i in queries  ];
    lst2 = copy.deepcopy( lst );
    for i in queries:
        getRotate( i );
        
 
    return answer

