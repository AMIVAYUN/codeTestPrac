package PM.스티커_모으기2;

import java.util.*;
import java.io.*;
class Solution {
    /**

     최대한 많이 뜯는다.

     n은 100000 이하

     즉 감소 형식이 안되기에 백트래킹 + 가지치기는 어렵다. 그렇다면 전체 합에서 빼는 구조로 가볼까? 시간 초과

     dp로 가자

     100000 **2은 메모리가 너무 소모된다.

     순환 사이클이기에 첫 스티커를 채택하냐? 마냐? 두 경우로 나눠서 1차원 배열을 두번 돌리자.

     */

    int Mx = 0;
    int[] sticker;

    int[] dp;
    public int solution(int sticker[]) {
        int n = sticker.length;
        int answer = 0;
        this.sticker = sticker;
        if( n == 1 ) return sticker[ 0 ];
        dp = new int[ n ];
        // int sum = 0;
        // for( int i = 0; i < sticker.length; i ++ ){
        //     sum += sticker[ i ];
        // }

        // dfs( sticker.length, sticker.length, new boolean[ sticker.length ], sum );


        dp[ 0 ] = sticker[ 0 ];
        dp[ 1 ] = sticker[ 0 ];

        for( int i = 2; i < n; i ++ ){
            if( i == n - 1 ){
                dp[ i ] = dp[ i - 1 ];
                continue;
            }
            dp[ i ] = Math.max( dp[ i - 2 ] + sticker[ i ], dp[ i - 1 ] );
        }
        Mx = Math.max( dp[ n - 1 ], Mx );

        dp = new int[ n ];
        dp[ 0 ] = 0;
        dp[ 1 ] = sticker[ 1 ];

        for( int i = 2; i < n; i ++ ){
            dp[ i ] = Math.max( dp[ i - 2 ] + sticker[ i ], dp[ i - 1 ] );
        }
        Mx = Math.max( dp[ n - 1 ], Mx );

        return Mx;
    }

    public void dfs( int n, int remain, boolean[] visited, int sum ){
        if( remain == 0 ){

            Mx = Math.max( Mx, sum );
            return;
        }

        if( Mx > sum ) return;

        for( int i = 0; i < n; i ++ ){
            if( !visited[ i ] ){
                visited[ i ] = true;
                remain--;

                int idx_before = i - 1;
                if( idx_before == -1 ){
                    idx_before = n - 1;
                }

                int idx_after = i + 1;
                if( idx_after == n ){
                    idx_after = 0;
                }

                boolean prev = visited[ idx_before ];
                boolean after = visited[ idx_after ];

                if( !prev ){
                    remain--;
                    sum -= sticker[ idx_before ];
                    visited[ idx_before ] = true;
                }

                if( !after ){
                    remain--;
                    sum -= sticker[ idx_after ];
                    visited[ idx_after ] = true;
                }
                // System.out.println(" selected: i = "+ i + " value = " + sticker[ i ] + " remain = " + remain + " sum = " + sum );
                // System.out.println( Arrays.toString( visited ) );
                dfs( n, remain, visited, sum );


                remain++;

                if( !prev ){
                    remain++;
                    sum += sticker[ idx_before ];
                    visited[ idx_before ] = false;
                }

                if( !after ){
                    remain++;
                    sum += sticker[ idx_after ];
                    visited[ idx_after ] = false;
                }
                visited[ i ] = false;

            }

        }
    }
}