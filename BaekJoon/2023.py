# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:26:14 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

prime = [ '2', '3', '5', '7' ];


regular = [ str( i ) for i in range( 10 ) ]



def getNum( depth, start ):
    global prime, regular, N;
    
    if( depth == N ):
        ans.append( start );
        return
    else:
        for num in regular:
            if( isPrime( int( start + num ) ) ):
                getNum( depth + 1, start + num );    
            
        
        return
    
def isPrime( num ): 
    for i in range( 2, int( num ** 0.5 ) + 1 ):
        if( num % i == 0 ):
            return False;
    
    return True;

ans = [];

N = int( input() );
for num in prime:
    getNum( 1, num );
    
    

for num in sorted( ans ):
    print( num )
    
