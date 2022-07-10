# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 23:52:14 2022

@author: 주석
@Link: acmicpc.net/problem/1037
"""

N = int( input() );

lst = [ i for i in map (int , input().split() ) ];

print( max( lst ) * min( lst ) )