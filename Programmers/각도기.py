# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 23:34:51 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(angle):
    
    div, mod = divmod( angle , 90 );
    
    if( div < 1 and mod != 0 ):
        return 1;
    elif( div == 1 and mod == 0 ):
        return 2;
    
    elif( 2 > div >= 1 ):
        return 3;
    
    else:
        return 4 
