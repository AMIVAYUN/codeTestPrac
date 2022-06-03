# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:58:28 2022
@FileName: 1038.py
@author: YUNJUSEOK
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
생각 정리: 맨 처음 로직은 아래와 같다. 단순 로직으로 중위 순회를 통한 배열 추출과 합 연산 후 해당 인덱스 별로 찾아서 바꾸는
알고리즘을 생각해보았지만 결과는 시간초과가 났다. 그 후 다른 분의 코드를 확인해보니 간단하게 생각해서 우측 큰값 부터 값을
합하여 매 위치에 더 해주면 되는 것이었다.....
다음에 다시 풀 수 있도록 메모해두자.
"""
#Time limit Exceeded

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        lst = [];
        
        self.inOrder( root, lst );
        
        lst_1 = [0] * len( lst );
        for i in range( len( lst ) ):
            sumi = 0;
            for j in range( len( lst ) ):
                if( lst[ i ] <= lst[ j ] ):
                    sumi += lst[ j ];
            
            lst_1[ i ] = sumi;
        
        print( lst_1);
        for i in range( len( lst ) ):
            self.SearchAndChange( root, lst[ i ], lst_1[ i ] );
        
        return root;
            
        
                
    def inOrder( self,root, lst ):
        if( root == None ):
            return;
        self.inOrder( root.left, lst );
        lst.append( root.val );
        self.inOrder( root.right, lst );
        
    def SearchAndChange( self, root, val, cgval ):
        while True:
            pos = root;
            if( pos.val == val ):
                pos.val = cgval;
                break;
            if( pos.val > val ):
                pos = pos.left;
            if( pos.val < val ):
                pos = pos.right;
                
    
    def levOrder( self, root , lvlQ, lst ):
        lvlQ.append( root );
        while lvlQ:
            pos = lvlQ.pop( 0 );
            if pos == None:
                lst.append( None );
                continue;
            if( pos is not None ):
                lst.append( pos.val );
                if pos.left:
                    lvlQ.append( pos.left );
                else:
                    lvlQ.append( None );
                if pos.right:
                    lvlQ.append( pos.right );
                else:
                    lvlQ.append( None );
                    
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.val = 0;
        self.inOrder( root, self.val );
        return root;
        
        
        
            
        
                
    def inOrder( self,root, val ):
        if( root == None ):
            return;
        self.inOrder( root.right, val );
        self.val += root.val;
        root.val = self.val;
        self.inOrder( root.left, val );
        
            
        
        
        
        