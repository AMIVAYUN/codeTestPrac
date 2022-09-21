# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 10:10:03 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

from collections import defaultdict;

'''
1
2
9999999999
9
'''

def t1():
    
    
    T = int( input() );
    
    for i in range( T ):
        n = int( input() );
        ddit = defaultdict( int );
        flag = False;
        for case in range( n ):
            
            ch = input();
            
            if( flag ):
                continue;
            
            for idx in range( 1, len( ch ) + 1 ):
                if( ddit[ ch[ : idx ] ] ):
                    print( "NO" );
                    flag = True;
            ddit[ ch ] = 1;
      
                
        if( flag ):
            continue;
        
        
        print( "YES" );
        
        

def t2():
    
    from collections import defaultdict;
    
    T = int( input() );
    
    for i in range( T ):
        
        n = int( input() );
        
        ddit = defaultdict( int );
        flag = False;
        
        for case in range( n ):
            
            ch = input();
            
            if( flag ):
                continue
                
            for idx in range( 1, len( ch ) ):
                
                ddit[ ch[: idx ] ] += 1;
            
            if( ddit[ ch ] ):
                flag = True;
            ddit[ ch ] = 1;
            
        
        if( flag ):
            print( "NO" );
        else:
            print( "YES" );
            
            
#PASS
def t3():
    
    
    T = int( input() );
    
    for i in range( T ):
        n = int( input() );
        ddit = defaultdict( int );
        flag = False;
        lst = [];
        for case in range( n ):
            
            ch = input();
            
            lst.append( ch ) ;
        
        
        lst = list( sorted( lst, key = lambda x:( len( x ), x ) ) );
        
        
        for ch in lst:
            if( flag ):
                break;
            if( ddit[ ch ] ):
                flag = True
            else:
                for idx in range( 1, len( ch ) ):
                    if( ddit[ ch[ :idx ] ] ):
                        flag = True;
                        break;
                
                ddit[ ch ] = 1;

        if( flag ):
            print( "NO" );
        else:
            print( "YES" );
            
        
t3()   