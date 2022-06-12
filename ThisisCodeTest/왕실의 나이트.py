# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:53:49 2022
@FileName: 왕실의 나이트.py
@author: YUNJUSEOK
@Link: p.115
"""
def sub( x, y ):
    '''
    if( x > 8 or y > 8):
        return 0;
    '''
    return ( x >> 3 ) or ( y >> 3 ) 

def Night( x, y ):
    global dx,dy 
    x, y = x - 1 , y - 1 
    if( sub( x, y ) ):
        return 0;
    
    
    cnt = 0;
    dit = { 0 : True , 8 : False }

    for i in range( 8 ):
        nx = x + dx[ i ] 
        ny = y + dy[ i ] 
        
        cnt += dit[ nx & 8 ] & dit[ ny & 8 ]
        
    return cnt;


def main():
    for i in range( 1, 9 ):
        for j in range( 1, 9 ):
            print(  Night( i, j ), end = " ")
        
        print( "" )