# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:03:27 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
def findLength( num ):
    leng = len( num );
    
    idx = 1;
    
    while 2**idx - 1 < leng:
        idx += 1;
    
    return 2**idx - 1 - leng;

    
def solution(numbers):
    answer = [];
    
    for number in numbers:
        num = bin( number )[ 2: ];
        bias = findLength( num );
        num = '0' * bias + num;
        answer.append(        int( Can( num, len( num ) ) )        );
        
    return answer 
'''
def Can( number, leng ):
    next = leng // 2;
    if( leng == 1 ):
        return True;
    
    if( number[ next ] == '0' ):
        return ( Can( number[ :next ], next ) == False ) and ( Can( number[ next + 1 : ], next ) == False ); 
    
    else:
        
        return Can( number[ :next ], next ) and Can( number[ next + 1 : ], next );
'''    
'''
#SOL 2-2
def Can( number, leng ):
    
    next = leng // 2;
    print( number, leng, next )
    if( leng == 1 ):
        return bool( int( number[ 0 ] ) );
    
    if( number[ next ] == '0' ):
        print( "neg: ", number[ :next ],": " ,Can( number[ :next ], next ) == False ,",",number[ next + 1 : ],": ", ( Can( number[ next + 1 : ], next ) == False) )
        return ( Can( number[ :next ], next ) == False ) and ( Can( number[ next + 1 : ], next ) == False ); 
    
    else:
        print( "pos: ", number[ :next ],": " ,Can( number[ :next ], next ) ,",",number[ next + 1 : ],": ", ( Can( number[ next + 1 : ], next ) ) )
        return Can( number[ :next ], next ) and Can( number[ next + 1 : ], next );
'''
'''
#SOL2-3
def Can( number, leng ):
    
    next = leng // 2;
    print( number, leng, next )
    if( leng == 1 ):
        return bool( int( number[ 0 ] ) );
    
    if( leng > 1 and number[ next ] =='0' ):
        return False;
    
    
    if( number[ next ] == '0' ):
        print( "neg: ", number[ :next ],": " ,Can( number[ :next ], next ) == False ,",",number[ next + 1 : ],": ", ( Can( number[ next + 1 : ], next ) == False) )
        return ( Can( number[ :next ], next ) == False ) and ( Can( number[ next + 1 : ], next ) == False ); 
    
    else:
        print( "pos: ", number[ :next ],": " ,Can( number[ :next ], next ) == False ,",",number[ next + 1 : ],": ", ( Can( number[ next + 1 : ], next ) == False) )
        return Can( number[ :next ], next ) or Can( number[ next + 1 : ], next );
'''    

    
    
def Can( number, leng ):
    '''
    0 이면 아래에도 전부 0 이어야함
    1 이면 아래가 만족하는지 봐야함
    
    
    '''
    next = leng // 2;
    
    if( leng == 1 ):
        return True
    
    if( leng > 1 and number[ next ] =='0' ):
        return '1' not in number;
    
    else:
        
        return Can( number[ :next ], next ) and Can( number[ next + 1 : ], next );
    
    
    
   
        
        
    
        
'''
def Can( number, leng ):
    

    if( leng == 1 ):
        return True; 
        
    if( leng % 2 == 0 ):
        number = '0' + number;
        
        second = number + '0';
    
    next = ( leng ) // 2;
    
    if( number[ next ] == '0' ):
        return False;
    
    
    return ( Can( number[ : next ], next ) and Can( number[ next + 1: ], next ) ) or ( Can( second[ : next ], next ) and Can( second[ next + 1: ], next ) if leng % 2 == 0 else True )


def solution(numbers):
    answer = [];
    
    for number in numbers:
        num = bin( number )[ 2: ]

        answer.append( int( Can( num, len( num ) ) ) );

    return answer
    
    
'''


print( solution( [423,15] ) )