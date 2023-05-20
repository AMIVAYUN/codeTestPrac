# -*- coding: utf-8 -*-
"""
Created on Sun May 21 00:43:51 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

#SOL1 WA 2%
def getLCS( s1, s2 ):
    leng1, leng2 = len( s1 ), len( s2 );
    
    dp = [ [ ( 0, "" ) for _ in range( leng2 + 1 ) ]  for _ in range( leng1 + 1 ) ];
    
    for x in range( 1, leng1 + 1 ):
        for y in range( 1, leng2 + 1 ):
            
            if( s1[ x - 1 ] == s2[ y - 1 ] ):
                dp[ x ][ y ] = ( dp[ x - 1 ][ y - 1 ][ 0 ] + 1, dp[ x - 1 ][ y - 1 ][ 1 ] + s1[ x - 1 ] );
            
            else:
                if( dp[ x - 1 ][ y ][ 0 ] > dp[ x ][ y - 1 ][ 0 ] ):
                    dp[ x ][ y ] = dp[ x - 1 ][ y ];    
                else:
                    dp[ x ][ y ] = dp[ x ][ y - 1 ];


    return dp[ leng1 ][ leng2 ];
'''
case

abcdefghijklmn
bdefg
efg

runcell(0, 'C:/Users/wntjr/PCODETEST/BaekJoon/untitled0.py')
abcde
cde
ade
2

runcell(0, 'C:/Users/wntjr/PCODETEST/BaekJoon/untitled0.py')
abcdefghi
abcde
fghi
0

runcell(0, 'C:/Users/wntjr/PCODETEST/BaekJoon/untitled0.py')
abcde
abc
c
1

runcell(0, 'C:/Users/wntjr/PCODETEST/BaekJoon/untitled0.py')
acb
acb
ab
2

runcell(0, 'C:/Users/wntjr/PCODETEST/BaekJoon/untitled0.py')
dababcf
ababdef
df
2

runcell(0, 'C:/Users/wntjr/PCODETEST/BaekJoon/untitled0.py')
axbyc
aibjc
ambnc
3

runcell(0, 'C:/Users/wntjr/PCODETEST/BaekJoon/untitled0.py')
aaaab
abc
ab
2

runcell(0, 'C:/Users/wntjr/PCODETEST/BaekJoon/untitled0.py')
abcdefghi
abcde
abc
'''
'''
LCS를 하나라고 단정 짓지 말것.

'''
def getLCS2( s1, s2, s3 ):
    leng1, leng2, leng3 = len( s1 ), len( s2 ), len( s3 );
    
    dp = [ [ [ 0 for _ in range( leng3 + 1) ] for _ in range( leng2 + 1) ] for _ in range( leng1 + 1) ];
    
    for x in range( 1,leng1 + 1 ):
        for y in range( 1, leng2 + 1 ):
            for z in range( 1, leng3 + 1 ):
                if( s1[ x - 1 ] == s2[ y - 1 ] == s3[ z - 1 ] ):
                    dp[ x ][ y ][ z ] = dp[ x - 1 ][ y - 1 ][ z - 1 ] + 1;
                else:
            
                    dp[ x ][ y ][ z ] = max( dp[ x - 1 ][ y ][ z ], dp[ x ][ y - 1 ][ z ], dp[ x ][ y ][ z - 1 ] );
    
    return dp[ leng1 ][ leng2 ][ leng3 ];
lst = [];
for i in range( 3 ):
    lst.append( input() );
    
    
lst = list( sorted( lst, key = lambda x: len( x ) ) );

answer = getLCS2( lst[ 0 ], lst[ 1 ], lst[ 2 ] );

'''#sol1
first = getLCS( lst[ 0 ], lst[ 1 ] );

answer = getLCS( first[ 1 ], lst[ 2 ] );
'''

print( answer );    