# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:59:03 2022
@FileName: 9251.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/9251
"""

"""
AACGGAACACGCTTTAAGGGCGATGGAATACCGTGGGTTTACCTAAAACTA
AATCTGGCCTATTCTGGGTCAAATGGCGTGAGCAAACATCGTACA
"""
# Fail
def f1():
    
    N = input();
    M = input();
    
    leng = len( N );
    leng2 = len( M );
    rs = [ 0 ] * leng;
    
    
    for i in M:
        temp = rs[:]
        for j in range( leng ):
            if( N[ j ] == i ):
                rs[ j ] = temp[ j ] + 1 if rs[ j ] < leng and rs[ j ] < leng2  else rs[ j ]
                for k in range( j + 1 , leng ):
                    rs[ k ] = rs[ j ] if rs[ k ] < rs[ j ] else rs[ k ];
                
    print( rs )
    print( max( rs ) if len( rs ) else 0 )

dict.

def f2():
    
    N = input();
    M = input();
    
    leng = len( N );
    leng2 = len( M );
    rs = [ 0 ] * ( leng + 1 );
    
    
    for i in range( 1, leng2 + 1 ):
        temp = rs[:];
        for j in range( 1, leng + 1 ):
            if( N[ j - 1 ] == M[ i - 1 ] ):
                rs[ j ] = temp[ j - 1 ] + 1;
            
            else:
                rs[ j ] = max( temp[ j ], rs[ j - 1 ] )
                
    
    print( max( rs ) )
    
    
        
    
    
if( __name__ == "__main__" ):
    f2();