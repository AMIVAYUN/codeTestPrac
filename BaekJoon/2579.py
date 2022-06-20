# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 14:16:51 2022
@FileName: 2579.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2579
"""

def main():
    N = int( input( ) )# <=300 score <=10000

    lst = [ 0 ] * ( N + 1 );

    for i in range( N ):
        lst[ i ] = int( input() );
        
        
    print( lst )
    
    
    
if(__name__ == "__main__" ):
    main();
    



