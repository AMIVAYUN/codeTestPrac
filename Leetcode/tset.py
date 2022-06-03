# -*- coding: utf-8 -*-
"""
Created on Tue May 17 13:39:49 2022
@FileName: tset.py
@author: YUNJUSEOK
"""


class Solution(object):
    def maxSumDivThree(self, nums):
        dp = [0,0,0]
        for num in nums:
            ndp = dp[::]#[dp[0],dp[1],dp[2]]
            print( "start [ndp] : ", ndp,"idx: ", num );
            if num % 3 == 0:
                ndp[0] = max(ndp[0], dp[0] + num)
                ndp[1] = max(ndp[1], (dp[1] + num) if dp[1] else 0)
                ndp[2] = max(ndp[2], (dp[2] + num) if dp[2] else 0)
                print( "ndp%0 : ", ndp )
            elif num % 3 == 1:
                ndp[0] = max(ndp[0], (dp[2] + num) if dp[2] else 0)
                ndp[1] = max(ndp[1], (dp[0] + num))
                ndp[2] = max(ndp[2], (dp[1] + num) if dp[1] else 0)
                print( "ndp%1 : ", ndp )
            elif num % 3 == 2:
                ndp[0] = max(ndp[0], (dp[1] + num) if dp[1] else 0)
                ndp[1] = max(ndp[1], (dp[2] + num) if dp[2] else 0)
                ndp[2] = max(ndp[2], (dp[0] + num))
                print( "ndp%2 : ", ndp )
            print( "end[ ndp ]: ", ndp[ :: ] )
            dp = ndp[::] #[ndp[0],ndp[1],ndp[2]]
            
            print( "dp: ",dp );
        return dp[0]
    
class Solution2:
    def maxSumDivThree(self, nums) :
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
            
    
    
a = Solution()
b = Solution2()
a.maxSumDivThree([3,5,1,4,8]);
print( b.maxSumDivThree([3,5,1,4,8]))