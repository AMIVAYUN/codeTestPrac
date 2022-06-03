# -*- coding: utf-8 -*-
#https://leetcode.com/problems/greatest-sum-divisible-by-three/
"""
Created on Tue May 17 12:29:06 2022
@FileName: 1262. Greatest Sum Divisible by Three.py
@author: YUNJUSEOK
"""
# dfs로 풀어보았지만 시간 초과가 났다.
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        self.result = [];
        
        self.sum0 = sum( nums );
        
        for i in range( len( nums ) ):
            
            self.dfs( ( nums[ :i ] + nums[ i + 1: ] ), nums[ i ] );
            
        return max( self.result ) if ( len( self.result ) > 0 ) else 0;
    def dfs( self, nums , sum0 ):
       
        if( sum0 % 3 == 0 ):
            self.result.append( sum0 );
        
        if( len( nums ) == 0 or self.result.__contains__( sum0 ) ):
            return;
        
        
        for i in range( len( nums ) ):
            self.dfs( nums[ :i ] + nums[ i + 1: ] , sum0 + nums[ i ] );
 
        
# 3에 속하는 수는 미리다 빼놓고 1 남는 수와 2 남는 수가 같은 만큼 더해주는 방식이다. 이는 반례가 있다.
# [ 1, 2, 3, 4, 4]
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        sum0 = 0;
        pos1 = [];
        pos2 = [];
        for i in range( len( nums ) ):
            if( nums[ i ] % 3 ==0 ):
                sum0 += nums[ i ];
            elif( nums[ i ] % 3 == 1 ):
                pos1.append( nums[ i ] );
            else:
                pos2.append( nums[ i ] );
        
        min0 = min( len( pos1 ), len( pos2 ) );
        
        return getsumAtpos( pos1, min0 )+ getsumAtpos( pos2, min0 ) + sum0; 
    
        
        
           
            
    

def getsumAtpos( pos , min0 ):
            cnt = 0;
            sum1 = 0;
            while( min0 > cnt ):
                idx = len( pos ) - 1;
                sum1 += pos[ idx ];
                idx -= 1;
                cnt += 1;
            
            return sum1;        
        
class Solution:
    def dfs( self, nums , sum0 ):
      
        if( sum0 % 3 == 0 ):
            self.result.append( sum0 );
        
        if( len( nums ) == 0 ):
            return;
        
        
        for i in range( len( nums ) ):
            self.dfs( nums[ :i ] + nums[ i + 1: ] , sum0 + nums[ i ] );   
    def maxSumDivThree(self, nums: List[int]) -> int:
        self.result = [];
        sum0 = 0;
        sum1 = 0;
        pos1 = [];
        for i in range( len( nums ) ):
            if( nums[ i ] % 3 ==0 ):
                sum0 += nums[ i ];
            else:
                pos1.append( nums[ i ] );
        
        self.dfs( pos1, sum1 );
        print( pos1 );
        print( sum0 , max( self.result ) );
        return sum0 + max( self.result );
        
     
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sum0 = 0;

        pos1 = [];
        pos2 = [];
        for i in range( len( nums ) ):
            if( nums[ i ] % 3 ==0 ):
                sum0 += nums[ i ];
            elif( nums[ i ] % 3 == 1 ):
                pos1.append( nums[ i ] );
            else:
                pos2.append( nums[ i ] );
            
        sum1, sum2 = sum( pos1 ), sum( pos2 );
        sum3 = sum1 + sum2;
        
        if( sum3 % 3 == 0 ):
            return sum0 + sum3;
        
        if( sum3 % 3 == 1 ):
            if pos1:
                return sum3 + sum0 - pos1[ 0 ];
        
        if( sum3 % 3 == 2 ):
            if pos2:
                return sum3 + sum0 - pos2[ 0 ];
        
        return 0;
# 3의 나머지는 언제나 항상 0 , 1 , 2 이 세가지 뿐이다.그렇기에 1이 남는 pos1 2가 남는 pos2 와 3으로 나눠지는
# 수들의 합 sum0로 분리 후에 pos1 과 pos2 의 전체 합을 구한다. 이 값을 3으로 나눈 값 또한 나머지가 0~2 이므로
# 1이 남으면 pos1의 값 첫번째 // 2가 남으면 pos2의 값 첫번째를 빼주거나, pos1 기준 pos2의 최솟값 두개, pos2
# 기준 pos1의  최솟값 두개를 더한 값 이 두가지 pos1 예시: ( pos1[ 0 ], pos2[ 0 ] + pos[ 1 ] ) 중 최솟값을
# 빼주는 것이 맥시멈 값이 된다.  
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sum0 = 0;

        pos1 = [];
        pos2 = [];
        for i in range( len( nums ) ):
            if( nums[ i ] % 3 ==0 ):
                sum0 += nums[ i ];
            elif( nums[ i ] % 3 == 1 ):
                pos1.append( nums[ i ] );
            else:
                pos2.append( nums[ i ] );
        pos1 , pos2 = sorted( pos1 ), sorted( pos2 );
        sum1, sum2 = sum( pos1 ), sum( pos2 );
        sum3 = sum1 + sum2;
        
        if( sum3 % 3 == 0 ):
            return sum0 + sum3;
        
        if( sum3 % 3 == 1 ):
            if pos1:
                if len( pos2 ) > 1:
                    return sum3 + sum0 - min( pos1[ 0 ] , pos2[0] + pos2[ 1 ] ) ;
                    
                return sum3 + sum0 - pos1[ 0 ];
        
        if( sum3 % 3 == 2 ):
            if pos2:
                if len( pos1 ) > 1:
                    return sum3 + sum0 - min( pos2[ 0 ], pos1[ 0 ] + pos1[ 1 ] ) ;
                return sum3 + sum0 -pos2[ 0 ] ;
        
        return 0;
        
      
        

     
           
            
    


            
