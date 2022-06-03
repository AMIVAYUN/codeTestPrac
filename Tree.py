# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:31:49 2022
@FileName: Tree.py
@author: YUNJUSEOK
"""
'''
Tree에 대한 기본 정리.
높이가 h인 트리는 최소 h개의 노드와 2ⁿ-1 노드를 가짐.

전위 순회: 자손보다 루트를 먼저 

중위 순회: 왼쪽 자손 루트 우측 자손 순으로

후위 순회: 루트보다 자손을 먼저

'''
class Node:
    def __init__( self, data ):
        self.data = data;
        self.left = None;
        self.right = None;
        
    
        
class BinaryTree:
    def __init__( self ):
        self.root = None;
        
    def preOrder( self, root ):
        if( root == None ):
            return;
        else:
            print( root.data );
            
            self.preOrder( root.left );
            self.preOrder( root.right );
    
    def inOrder( self, root ):
        if ( root == None ):
            return;
        else:
            self.inOrder( root.left );
            print( root.data );
            self.inOrder( root.right );
        
    def postOrder( self, root ):
        if( root == None ):
            return;
        else:
            self.postOrder( root.left );
            self.postOrder( root.right );
            print( root.data );
def initialize():
    list01 = [];
    for i in range( 1, 11 ):
        list01.append( Node( i ) );
    
    tree = BinaryTree();
    tree.root = list01[ 0 ];
    tree.root.left = list01[ 1 ];
    tree.root.right = list01[ 2 ];
    tree.root.left.left = list01[ 3 ];
    tree.root.left.right = list01[ 4 ];
    tree.root.right.left = list01[ 5 ];
    tree.root.right.right = list01[ 6 ];
    tree.root.left.left.left = list01[ 7 ];
    tree.root.left.left.right = list01[ 8 ];
    tree.root.left.right.left = list01[ 9 ];
    
    return tree;
        
def main():
    tree = initialize();
    print (" - " * 15 +" 전위 순회" + " - " * 15 )
    tree.preOrder( tree.root );
    print (" - " * 15 +" 중위 순회" + " - " * 15 )
    tree.inOrder( tree.root );
    print (" - " * 15 +" 후위 순회" + " - " * 15 )
    tree.postOrder( tree.root );

if( __name__ =="__main__"):
    main();

