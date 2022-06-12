# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 21:42:20 2022
@FileName: 14503.py
@author: YUNJUSEOK
@Link:http://acmicpc.net/problem/14503


문제에서 7,4 를 6,3로 이해해서 헤맸다. 문제 내용을 세밀하게 읽어보자.

"""


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

class Robot:
    def __init__( self,pos, direc ):
        global visit;
        self.pos = pos;
        self.dir = direc;
        visit[ pos[ 0 ] ][ pos[ 1 ] ] = 1;
    def move(self):
        global dx, dy, field,visit;
        x, y = self.pos[ 0 ], self.pos[ 1 ]
        for i in range( 4 ):
            self.dir = ( self.dir + 3 ) % 4
            nx = x + dx[ self.dir ];
            ny = y + dy[ self.dir ];
            
            
            if( field[ nx ][ ny ] != 1 and visit[ nx ][ ny ] != 1):
                self.pos = ( nx, ny );
                visit[ nx ][ ny ] = 1;
                return True;
        
        back = ( self.dir + 2 ) % 4;
        bx , by = self.pos[ 0 ] + dx[ back ] , self.pos[ 1 ] + dy[ back ]
        if( field[ bx ][ by ] == 1 ):
            return False;
        else:
            self.pos = ( bx, by );
            return True;

m,n = map( int, input().split() );
field = [];
x,y, direc = map( int, input().split() );
visit = [ [0] * n for i in range( m ) ];
R = Robot( ( x , y ), direc );
cnt = 1;
for _ in range( m ):
    field.append( list( map( int, input().split() ) ) )
cnt = 0;
while R.move():
    cnt+=1 # 필요는 없지만 총 연산수.
sum0 = 0;
for i in visit:
    sum0 += sum( i ) 
print( sum0 )