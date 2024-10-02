import java.util.*;
import java.io.*;
class Solution {

    /**
     n == 1 -> 1 -> 1

     n == 2 -> 1 1 -> 5

     n == 3 -> 2 2 1 -> 8

     n == 4 -> 3 3 2 1   -> 11

     n == 5 -> 4 4 3 2 1 -> 14

     n == 6 -> 5 5 4 3 2 1  -> 17

     n == 7 -> 6 6 5 4 3 2 1 -> 20
     */

    int dx[] = { -1, 1, 0 }, dy[] = { -1, 0, 1 };

    public int[] solution(int n) {
        int[] answer = {};


        if( n == 1 ){
            return new int[]{ 1 };
        }else if( n == 2 ){
            return new int[]{ 1, 2, 3 };
        }else if ( n == 3 ){
            return new int[]{ 1, 2, 6, 3, 4, 5 };
        }

        int[][] graph = new int[ n ][ n ];
        int num = 1;

        int x = -1; int y = 0;
        int remain = ( n + 1 ) * n / 2;
        answer = new int[ remain ];
        int stan = n;
        int dir = 1;
        while( remain > 0 ){
            int row = stan;
            while( row > 0 ){

                x = x + dx[ dir ];
                y = y + dy[ dir ];
                graph[ x ][ y ] = num++;
                row--;
                remain--;
            }

            stan--;
            dir = ( dir + 1 ) % 3;
        }
        int Mx = 1;
        int idx = 0;
        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < Mx; j ++ ){
                answer[ idx++ ] = graph[ i ][ j ];
            }
            Mx++;
        }

        return answer;
    }
}