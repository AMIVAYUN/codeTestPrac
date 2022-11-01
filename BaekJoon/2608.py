# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 12:03:19 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

Maximum = {	'I':3	,'V':1,	'X':3,	'L':1,	'C':3,	'D':1,	'M':3 ,
           'IV' : 1, 'IX' : 1, 'XL' : 1, 'XC' : 1, 'CD' : 1, 'CM' : 1}

num = {	'I':1	,'V':5,	'X':10,	'L':50,	'C':100,	'D':500,	'M':1000 ,
       'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90, 'CD' : 400, 'CM' : 900}

special = [ 'IV', 'IX', 'XL', 'XC', 'CD', 'CM' ]
def fromRoman( str0 ):
    global Maximum,num;
    from collections import deque;
    idx = 0;
    
    dq = deque( str0 );
    answer = [];
    
    while dq:
        if( len( dq ) > 1 and num [ dq[ 0 ] ] < num [ dq[ 1 ] ] ):
            first = dq.popleft();
            second = dq.popleft();
            answer.append( first +second );
        
        else:
            answer.append( dq.popleft() );
    
    ans = 0;
    
    for ch in answer:
        ans += num[ ch ];
    
    return ans;


def toRoman( number ):
    global Maximum,num;
    
    keys = list( sorted( num.items(), key = lambda x: -x[ 1 ] ) );
    ans = '';
    idx = 0;
    Mx = len( keys );
    
    while idx < Mx and number != 0:

        div,mod = divmod( number, keys[ idx ][ 1 ] );

        if( div > Maximum[ keys[ idx ][ 0 ] ] ):
            
            while div != Maximum[ keys[ idx ][ 0 ] ]:
                
                div -= 1;
                mod += keys[ idx ][ 1 ];
       
            
   
        ans += keys[ idx ][ 0 ] * div;
        number = mod;
        

        idx += 1;
        
    return ans;
        
sum_ = 0;              
for i in range( 2 ):
    sum_ += fromRoman( input() );
print( sum_ );
print( toRoman( sum_ ) );
