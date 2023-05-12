# -*- coding: utf-8 -*-
"""
Created on Fri May 12 23:04:10 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


now = 0;
answer = [];
arr = [];
stack = [];
class node:
    def __init__( self, val ):
        self.prev = None;
        self.next = None;
        self.val = val;
    
class LinkedList:
    def __init__( self, head ):
        self.head = head;
        self.tail = head;
    
    def add( self, val ):
        newnode = node( val );
        self.tail.next = newnode;
        self.tail = newnode;
    
    def delete( self, node ):
        global stack;
        stack.append( node );

        #head
        if( node.prev == None ):
            self.head = node.next;
            node.next.prev = None;
            
        #tail
        elif( node.next == None ):
            
            self.tail = node.prev;
            node.prev.next = None;
            
        
        else:
        
            node.prev.next = node.next;
            node.next.prev = node.prev;
            
        return;
    
    def recover( self ):
        global stack;

        node = stack.pop();

        if( node.prev == None ):
            node.next = self.head;
            self.head = node;
            node.next.prev = node;
            
        elif( node.next == None ):
            self.tail.next = node;
            self.tail = node;
            
        else:
            node.prev.next = node;    
            node.next.prev = node;
        
        return;
    
    def toString( self, answer ):
        pos = self.head;
        
        while pos != None:
            answer[ pos.val ] = 'O';
            
            pos = pos.next;
        
        return ''.join( answer );
    
    def toString2( self ):
        pos = self.head;
        
        while pos != None:
            print( pos.val, end = " " );
            
            pos = pos.next;
        print( );
    
def solution(n, k, cmd):
    global stack;
    head = node( 0 );
    Llst = LinkedList( head );
    pos = Llst.head;
    for i in range( 1, n ):
        newnode = node( i );
        pos.next = newnode;
        newnode.prev = pos;
        pos = pos.next;
        
    pos = Llst.head;

    while pos.val != k:
        pos = pos.next;
    
    
    for c in cmd:
        str0 = c.split( " " );
        if( len( str0 ) > 1 ):
            val = int( str0[ 1 ] );
            
            if( str0[ 0 ] == 'U' ):
                for i in range( val ):
                    if( pos.prev == None ):
                        break;
                    
                    pos = pos.prev;
                
            else:
                for i in range( val ):
                    if( pos.next == None ):
                        break;
                    
                    pos = pos.next;
        else:
            if( str0[ 0 ] == 'C' ):
                if( pos.next != None ):
                    nextnode = pos.next;
                    
                else:
                    nextnode = pos.prev;
                Llst.delete( pos );
                pos = nextnode;
            else:
                Llst.recover();
    
    answer = [ 'X' ] * n;
    
    return Llst.toString( answer );
    
    
    
''' 
    
def U( x ):
    global now; 
    now -= x;
    
    now = 0 if now < 0 else now;
    
    return;

def D( x ):
    global arr, now; 
    
    now += x;
    
    now = len( arr ) - 1 if now >= len( arr ) else now;
    
    return;


def C():
    global arr,now,stack,answer;
    val = arr[ now ];
    
    arr = arr[ :now ] + arr[ now + 1 : ];
    answer[ val ] = 'X';
    
    stack.append( ( now, val ) );
    if( now == len( arr ) ):
        now -= 1;
    return;

def Z():
    global arr,now,stack;
    
    val = stack.pop();
    answer[ val[ 1 ] ] = 'O' 
    prev, val = val;
    if( now >= prev ):
        now += 1;
    arr = arr[ :prev ] + [ val ] + arr[ prev: ];
    
    return;
#SOL1 T.O
def solution(n, k, cmd):
    global now, arr, stack,answer;
    mapper = { 'D': D, 'C': C, 'U': U, 'Z': Z };
    now = k;
    arr = [ i for i in range( n ) ];
    answer = [ 'O' ] * n;
    
    for c in cmd:

        commands = c.split();
        command = commands[ 0 ];
        if( len( commands ) > 1 ):
            x = commands[ 1 ];
            mapper[ command ]( int( x ) );
        else:
            mapper[ command ]();
    
    
    
    
    return ''.join( answer );



#SOL2 RE
def solution2(n, k, cmd):
    global now, arr, stack;
    mapper = { 'D': D, 'C': C, 'U': U, 'Z': Z };
    now = k;
    arr = [ i for i in range( n ) ];
    from collections import deque;
    dq = deque( cmd );
    cases = [ 'D', 'U' ];
    while dq:
        bias = 0;
        while dq and dq[ 0 ][ 0 ] in cases:
            val = dq.popleft();
            val = val.split( " " );
            mul = -1 if val[ 0 ] == 'U' else 1;
            bias += int ( val[ 1 ] ) * mul;
        
        now += bias ;
        task = dq.popleft();
        
        mapper[ task ]();
            
    
    answer = [ 'O' ] * n;
    

    return ''.join( answer );

#SOL1 T.O
def solution1(n, k, cmd):
    global now, arr, stack;
    mapper = { 'D': D, 'C': C, 'U': U, 'Z': Z };
    now = k;
    arr = [ i for i in range( n ) ];
    
    for c in cmd:

        commands = c.split();
        command = commands[ 0 ];
        if( len( commands ) > 1 ):
            x = commands[ 1 ];
            mapper[ command ]( int( x ) );
        else:
            mapper[ command ]();
    
    
    answer = [ 'O' ] * n;
    
    for prev, val in stack:
        answer[ val ] = 'X';
    return ''.join( answer );
    
'''
    
    
    
solution( 8,	2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"] )