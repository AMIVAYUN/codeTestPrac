# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:50:07 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
    
    1.plus 큰수 끼리 곱해준다.
    2.minus 큰수 끼리 곱해준다.
    
    3. 남는수를 zero와 최대한 곱해준다.
    
    4. 더한다.
    
    
"""


N = int( input() );

lst = [];

minus = [];

plus = [];

zero = [];

for i in range( N ):
    target = int( input() )
    lst.append( target );
    if( target > 0 ):
        plus.append( target );
    elif( target < 0 ):
        minus.append( target );
        
    else:
        zero.append( target );

srplus = list( sorted( plus ) );
res_plus = [];
for idx in range( len( srplus ) // 2 ):
    if( srplus[ -2 ] == 1 ):
        
        break;
    res_plus.append( srplus[ -1 ] * srplus[ -2 ] );
    
    for i in range( 2 ):
        srplus.pop();
    

res_plus = res_plus + srplus;

srminus = list( sorted( minus, reverse = True ) );

res_minus = [];

for idx in range( len( srminus ) // 2 ):
    res_minus.append( srminus[ -1 ] * srminus[ -2 ] );
    
    for i in range( 2 ):
        srminus.pop();
        
        
minus_remain = srminus;


Mn = min( len( zero ), len( minus_remain ) );

res_zero = [];

for i in range( Mn ):
    minus_remain.pop();
    


print( max( sum( res_plus + res_minus + minus_remain ), sum( lst ) ) );
