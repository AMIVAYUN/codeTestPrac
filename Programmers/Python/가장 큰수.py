# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:07:20 2022
@FileName: 가장 큰수.py
@author: YUNJUSEOK
@Link:
"""


def solution( numbers ):
    numbers = [  str(i) for i in numbers ];
    
    numbers = sorted( numbers , key = lambda x: ( x * 3 ),reverse = True);
    while( numbers[ 0 ] == '0' and len( numbers ) > 1 ):
        numbers.pop( 0 );
    str0 = "".join( i for i in numbers );
    
    
    return str0 
def solution_2( numbers ):
    numbers = [  str(i) for i in numbers ];
    lst = [];
    for i in numbers:
        num_ = i;
        min_ = min( i );
        num_= num_.ljust( 4, min_);
        lst.append( ( num_, i ) );
    
    lst = sorted( lst, key = lambda x: x[ 0 ] ,reverse = True );
    
    answer = ''
    for i in lst:
        answer += i[ 1 ]
    
        
        
    
                
                
            
        
    return answer;

def solution_1(numbers):
    import itertools
    numbers = [ str( i ) for i in numbers ]
    lst = list( itertools.permutations( numbers,len( numbers ) ) )
    answer = [];
    for i in lst:
        str0 = ''.join( j for j in i );
        answer.append( int( str0 ) )
    
    return str( max( answer ) )