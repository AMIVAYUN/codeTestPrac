# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 15:17:10 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


N = int( input() );

lst = list( map( int, input().split() ) );

lst.sort();
answer = 0;
for idx in range( 0, N ):
    case = lst[ idx ];
    
    left = 0; right = N - 2;
    
    tmp = lst[ :idx ] + lst[ idx + 1 : ]
    
    while left <= right:

        
        sum_ = tmp[ left ] + tmp[ right ];
        
        
        if( sum_ == case and left != right ):

            answer += 1 ;
            break;
        if( sum_ > case ):
            right -= 1;
        
        else:
            left += 1;

print( answer )