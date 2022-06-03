# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:19:12 2022
@FileName: .py
@author: YUNJUSEOK
"""
import gc;

class Node:
    def __init__( self, data ):
        self.data = data;
        self.parent = None;
        self.left = None;
        self.right = None;
        
class BST:
    def __init__( self, root ):
        self.head = Node( root );
        
    def insert( self, data ):
        pos = self.head;
        while( True ):
            if( pos.data > data ):
                if( pos.left != None ):
                    pos = pos.left;
                    continue;
                pos.left = Node( data );
                pos.left.parent = pos;
                break;
                
                
            else:
                if( pos.right != None ):
                    pos = pos.right;
                    continue;
                pos.right = Node( data );
                pos.right.parent = pos
                break;
            
    def search( self, data ):
        pos = self.head;
        while( True ):
            if(  pos == None or pos.data == data ):
                return pos
            elif( pos.data > data ):
                pos = pos.left;
            
            elif( pos.data < data ):
                pos = pos.right;
    

    def delete( self, data ):
        pos = self.search( data );
        if( pos == None ):
            print("삭제하시려는 값이 Tree에 존재하지 않습니다. ");
            return
        if( self.getLeaf( pos )== 0 ):
            idx = self.getChildPath( pos.parent, pos.data );
            if( idx == 1 ):
                pos.parent.left = None;
                print(" 삭제 완료: {0}", pos.data );
                
            elif( idx == 2 ):
                pos.parent.right = None;
                print(" 삭제 완료: {0}", pos.data );
            else:
                raise Exception(" Error 발생 ");
                    
        elif( self.getLeaf( pos )== 1 ):
            idx = self.getChildPath( pos.parent, pos.data );
            if( pos.right == None ):
                if( idx == 1 ):
                    pos.parent.left = pos.left;
                    print(" 삭제 완료: {0}", pos.data );
                    
                elif( idx == 2 ):
                    pos.parent.right = pos.left;
                    print(" 삭제 완료: {0}", pos.data );
                else:
                    raise Exception(" Error 발생 ");
            else:
                if( idx == 1 ):
                    pos.parent.left = pos.right;
                    print(" 삭제 완료: {0}", pos.data );
                    
                elif( idx == 2 ):
                    pos.parent.right = pos.right;
                    print(" 삭제 완료: {0}", pos.data );
                else:
                    raise Exception(" Error 발생 ");
        else:
            
            
    def inOrder( self, node ):
        if( node == None ):
            return ;
        self.inOrder( node.left );
        print( node.data );
        self.inOrder( node.right );
    def getChildPath( pos, value ):
        if( pos.left == value ):
            return 1;
        elif( pos.right == value ):
            return 2;
        else:
            return 0;
    #inOrder
    def toString( self ):
        self.inOrder( self.head );
           
    def getMin( self, subTree):
        while( self.getLeaf( subTree) == 0 ):
            if()
        
        
    def getLeaf( Node ):
        idx = 0;
        if( Node.left != None ):
            idx += 1;
        if( Node.right != None ):
            idx += 1;
        return idx;
        
                

def main():
    Bst = BST( 50 );
    Bst.insert( 30 );
    Bst.insert( 20 );
    Bst.insert( 40 );
    Bst.insert( 70 );
    Bst.insert( 90 );
    
    Bst.search( 15 );
    if( Bst.search( 20 ) == None ):
        print(" 찾으시는 게 없습니다. ");
    else:
        print(" 찾으시는 게 있습니다. 부모:", end= str( Bst.search( 20 ).parent.data ) );
    print( "\n" );
        
    Bst.toString();

if( __name__ == "__main__"):
    main();        
            