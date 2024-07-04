package PM.가장많이받은선물;

import java.util.*;
import java.io.*;
class Solution {
    int idx = 0;
    Map< String, Integer > map = new HashMap<>();
    int n, graph[][];
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        n = friends.length;
        graph = new int[ n ][ n ];
        int[][] total = new int[ n ][ 2 ];
        for( String friend: friends ){
            map.put( friend, idx++ );
        }

        for( String gift : gifts ){
            String[] sr = gift.split(" ");
            int senderIdx = map.get( sr[ 0 ] );
            int receiverIdx = map.get( sr[ 1 ] );

            graph[ senderIdx ][ receiverIdx ]++;
            total[ senderIdx ][ 0 ] ++;
            total[ receiverIdx ][ 1 ] ++;
        }
        // graph 는 [ sender ][ receiver ] 구조;
        // i 가 j에게
        //각자가 받는 갯수
        int[] result = new int[ n ];
        for( int i = 0; i < n; i ++ ){
            for( int j = i + 1; j < n; j ++ ){

                if( graph[ i ][ j ] > graph[ j ][ i ] ){
                    result[ i ]++;
                }else if( graph[ i ][ j ] < graph[ j ][ i ] ){
                    result[ j ]++;
                }else{
                    int iPresent = total[ i ][ 0 ] - total[ i ][ 1 ];
                    int jPresent = total[ j ][ 0 ] - total[ j ][ 1 ];
                    System.out.println( i + " " + j + "[" + iPresent + "," + jPresent +"]");
                    if( iPresent > jPresent ){
                        result[ i ]++;
                    }else if( iPresent < jPresent ){
                        result[ j ]++;
                    }else{
                        continue;
                    }
                }

            }
        }

//         for( int i = 0; i < n; i ++ ){
//             System.out.println( Arrays.toString( graph[ i ] ) );
//         }
//         System.out.println("---- total -----");
//         for( int i = 0; i < n; i ++ ){
//             System.out.println( Arrays.toString(total[i] ) ) ;
//         }

//         System.out.println( "res: " + Arrays.toString( result ) );

        for( int i = 0; i < n; i ++ ){
            answer = Math.max( answer, result[ i ] );
        }

        return answer;
    }
}