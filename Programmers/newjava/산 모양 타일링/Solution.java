import java.util.*;
class Solution {
    public int solution(int n, int[] tops) {
        int answer = 0;

        //top 이 없으면 그냥 f(n) = f( n - 1 ) + f( n - 2 );
        //top 이 있다면? f(n) = f( n - 1 ) * 2 + f( n - 2 );

        int[] dp = new int[ ( n * 2 ) + 2 ];
        dp[ 0 ] = 1;
        dp[ 1 ] = 1;
        for( int i = 2; i <= n * 2 + 1; i ++ ){
            if( ( i % 2 == 0 ) && ( tops[ i / 2 - 1 ] == 1 ) ){
                dp[ i ] =  ( dp[ i - 1 ] * 2 + dp[ i - 2 ] ) % 10007;
            }else{
                dp[ i ] = ( dp[ i - 1 ] + dp[ i - 2 ] ) % 10007;
            }
        }

        return dp[ n * 2 + 1 ];
    }
}