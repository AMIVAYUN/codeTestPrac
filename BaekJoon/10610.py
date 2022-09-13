# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 12:53:58 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
# 21% timeout



number = input();


lst = list( number );

lst = list( sorted( lst ,reverse = True) );

if( '0' not in lst ):
    print( -1 );

else:
    

    import itertools;
    
    
    leng = len( lst );
    
    
    ans = -1
    cond = False;
    for size in range( 2, leng + 1 ):
        
        perm = itertools.permutations( lst[ -1 * size: ], size ); 
        
        
        for case in perm:
            if( list( case ) [ -1 ] != '0' ):
                continue;
            if( int ( "".join( ( lst [ :-2 ] + list( case ) ) ) ) % 30 == 0 ):
                ans =    int ( "".join( ( lst [ :-2 ] + list( case ) ) ) )
                
                cond = True;
                break;
            
            
        
        if( cond ):
            break;
        
    
    print( ans );
    
    #t2
    
            
number = input();


lst = list( number );

lst = list( sorted( lst ,reverse = True) );

sum_ = sum( [ int( i ) for i in lst ] );
if( '0' not in lst ):
    print( -1 );

else:
    if( sum_ % 3 ):
        print( -1 );
        
    else:
        print( int( ''.join( lst ) ) )
    

