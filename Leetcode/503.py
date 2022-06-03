# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:07:11 2022
@FileName: 503.py
@author: YUNJUSEOK
"""


# 시간 초과               현재 내 로직은  < ------ a -------->의 형식임
# 그렇다면 a --------> 진행한 후에 없으면 그냥 max아닌가? 아니다 바로 다음. 에 집중하여야 한다.
# 즉 a -------> 후 0 ---------> a까지의 연산을 진행하면 되지 않을까?
class CircleList:
        def __init__( self, element ):
            self.element = element;
            self.max1 = len( element ) ;
            self.result = [ -1 ] * len( element );
        def getNextGreater( self, element, idx ):
            
            MxPidx = 0;
            MxMidx = 0;
            for i in range( idx + 1, self.max1 ):
                if( element < self.element[ i ] ):
                    MxPidx = i - idx;
                    break;
    
                
            for j in range( idx - 1, -1, -1):
                if( element < self.element[ j ] ):
                    MxMidx = idx - j;
            
            if( MxPidx != 0 ):
                self.result[ idx ] = self.element[ idx + MxPidx ];
            else:
                if( MxMidx != 0 ):
                    self.result[ idx ] = self.element[ idx - MxMidx ];
            
# 문제를 보고 바로 풀려하다보니 쓸데없는 변수 할당과 문제가 길어졌다. 단순화 시킨 클래스이다.
class CircleList:
        def __init__( self, element ):
            self.element = element;
            self.max1 = len( element );
            self.Rmax = max( element );
            self.result = [ -1 ] * len( element );
        def getNextGreater( self, element, idx ):
            if( self.Rmax == element ):
                return;
        
            Mxcond = True;
            for i in range( idx + 1, self.max1 ):
                if( element < self.element[ i ] ):
                    self.result[ idx ] = self.element[ i ];
                    Mxcond = False;
                    break;
            if( Mxcond ):
                for j in range( 0 , idx ):
                    if( element < self.element[ j ] ):
                        self.result[ idx ] = self.element[ j ];
                        break;
                        
    class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = deque()
        sz = len(nums)
        res = [-1] * sz
        # 2바퀴를 돌기 위해서
        for i in range(sz * 2): 
            while stack and nums[stack[-1]] < nums[i%sz] : 
                res[stack.pop()] = nums[i % sz]
            stack.append(i%sz)
        return res        
                        
            
        
class Solution:
    
            
        
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        a = CircleList( nums );
        for i in range( a.max1 ):
            a.getNextGreater(a.element[ i ], i);
        
        return a.result;            
    
## discuss의 stack에 힌트를 얻어 구현한 로직.
## 아직 컴퓨터적 사고가 부족하다. 대상의 특성을 찾아 거기에 맞는 자료구조를 대입할 수 있도록 노력하자.
## list는 기본적으로 stack의 구조이다.
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        lst = [];


        lenx = len( nums );
        result = [ -1 ] * lenx;

        for i in range( 0, lenx*2 ):
            while( lst and nums[ lst[ -1 ] ] < nums[ i % lenx ] ):
                result[ lst.pop() ] = nums[ i % lenx ] ;
            lst.append( i % lenx );
        
        return result;
    
        