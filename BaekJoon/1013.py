# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:12:03 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

def t1():
    for i in range( n ):
        ch = input();
        idx = 0;
        flag = False;
        while idx < len( ch ):

            if( flag ):
                break;
            if( ch[ idx ] == "0" ):
                idx, flag = chkOne( ch, idx );
            
            else:
                idx, flag = chkTwo( ch, idx );
        
        print("NO" if flag else "YES" ) 
        

def chkOne( ch, idx ):
    return idx + 2, ch[ idx: idx + 2 ] != "01"
        
'''
10011001
'''
def chkTwo( ch, idx ):
    tmp = idx + 3;
    if( ch[ idx : idx + 3 ] == "100" ):
        while tmp < len( ch ) and ch[ tmp ] == "0":
            tmp += 1;
        if( tmp == len( ch ) - 1 and ch[ tmp ] != "1" ):
            return tmp, True;
        while tmp < len( ch ) and ch[ tmp ] == "1":
            tmp += 1;
    
        return tmp, False;

    else:
        return tmp, True;

from collections import deque;
res = 0;
n = int( input() );
for i in range( n ):
        
    ch = list( input() );
    
    res = True;
    
    
    while ch:
        
        if( ch[ :2 ] == ['0','1'] ):
            for i in range( 2 ):
                ch.pop( 0 );
        elif( ch[ :3 ] == ['1','0','0'] ):
            for i in range( 3 ):
                ch.pop( 0 );
            while ch and ch[ 0 ] == "0":
                ch.pop( 0 );
            
            if( len( ch ) == 0 ):
                res = False;
                break;
            
            while ch and ch[ 0 ] == '1':
                if( len( ch ) > 3 and ch[ :3 ] == ['1','0','0'] ):
                    break
                
                ch.pop( 0 )
                
            
        else:
            res = False
            break;
    
    
    
    print( res )