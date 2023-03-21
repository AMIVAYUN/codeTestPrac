# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:56:32 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


'''

1 = 1

2 = 2

3 = 3

4 = 1

5 = 2

6 = 3

7 = 3

8 = 2

9 = 1

10 = 2

11 = 3

12 = 4

13 = 2

14 = 3

15 = 4

16 = 1;

17 = 2;

18 = 3;

19 = 4;

20 = 2;

21 = 3

22 = 4;

23 = 5;

24 = 3;



a( i + 1 ) = min( a( k ) + a( i + 1 - k ) )


'''

#SOL3 

Mn = 100001;

n = int( input() );

dp = [ Mn ] * ( n + 1 );

dp[ 1 ] = 1;



for i in range( 3, n + 1 ):
    if( ( i **0.5 ).is_integer() ):
        dp[ i ] = 1;
        continue;
    for bias in range( 1, int( i ** 0.5 ) + 1 ):
        dp[ i ] = min( dp[ i ], dp[ bias ** 2 ] + dp[ i - bias ** 2 ]  if bias ** 2 <= i else dp[ i ]);

print( dp[ n ])


'''
""
#SOL2 Memory Out

Mn = 10000001;

from collections import deque;


dq = deque()


n = int( input() );


dq.append( ( n, 0 ) )

while dq:
    pos, cnt = dq.popleft();
    
    if( cnt > Mn ):
        continue;
    
    for i in range( int( pos ** 0.5 ) + 1, 0, -1 ):
        if( ( pos - ( i ** 2) ) > 0 and cnt + 1 < Mn ):
            dq.append( ( ( pos - ( i ** 2) ) , cnt + 1 ) )
        elif( ( pos - ( i ** 2) ) == 0 ):
            Mn = min( Mn, cnt + 1 )
    
print( Mn )


'''
'''
    


#Timeout
n = int( input() );
dp = [ 100001 ] * ( 100001 );
dp[ 0 ] = 1;
dp[ 1 ] = 1;
cons = 1;
for i in range( 2, n + 1 ):
    if( (i ** 0.5).is_integer() ):
        dp[ i ] = 1;
        cons += 1;
    else:
        dp[ i ] = min( [ dp[ i - k ] + dp[ k ] for k in range( int( i**0.5) , i ) ] )

print( dp[ n ] );

'''