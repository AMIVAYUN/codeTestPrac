# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 01:54:02 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

def t1():
    '''
    Returns
    -------
    None.
    
    반례
    10
    ABB
    BB * 9
    '''

    


    from collections import defaultdict;

    N = int( input() );

    rs = defaultdict( int );

    lst = [];

    for i in range( N ):
        word = input();
        lst.append( ( len( word ), list( word ) ) );
        for wd in word:
            rs[ wd ] = 0;
        
    numidx = defaultdict( lambda: defaultdict( int ) ) ;

    lst = sorted( lst , reverse = True );


    for i in lst:
        start, str0 = i[ 0 ], i[ 1 ];
        leng = i[ 0 ] - 1;
        for j in range( leng, -1, -1 ):
            numidx[ j + 1 ][ str0[ leng - j ] ] += 1
            
    print( numidx )
    idx = 9;

    for key in numidx:
        numidx[ key ] = sorted( numidx[ key ].items(), key = lambda x: ( -x[ 1 ] ) );
        for val in numidx[ key ]:
            if( rs[ val[ 0 ] ] == 0 ):
                rs[ val[ 0 ] ] = idx;
                idx -= 1;

    numlst = [];

    for num in lst:
        str0 = ""
        for alphabet in num[ 1 ]:
            str0 += str( rs[ alphabet ] );
        numlst.append( int( str0 ) );
        

    print( sum( numlst ) )
    
    
def t2():
    from collections import defaultdict;
    N = int( input() );
    lst = [];
    vocab = defaultdict( int );
    for i in range( N ):
        lst.append( input() );
    
    
    for word in range( N ):
        length = len( lst[ word ] ) - 1;
        for idx in range( len( lst[ word ] ) ):
            vocab[ lst[ word ][ idx ] ] += 10 ** ( length - idx )
    
    
    vocab = sorted( vocab.items(), key = lambda x: ( -x[ 1 ] ) );
    
    
    start = 9;
    result = 0;
    for key in vocab:
        result += key[ 1 ] * start;
        start -= 1;     
    print( result )
t2()
    
    
