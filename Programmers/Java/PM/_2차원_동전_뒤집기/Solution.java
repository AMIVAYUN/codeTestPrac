package PM._2차원_동전_뒤집기;

import java.util.*;
import java.io.*;
class Solution {
    /**

     옛날에 코테에 나와서 풀다가 시간 부족해서 못 푼 문제였다.

     그때는 최적화를 찾기 위해 고민하다가 끝났는데 일단 뒤집어보자.

     전체로 돌리면 안된다.

     그림을 보면 행들을 다 뒤집고 열을 뒤집는데 잘 생각해보면 행에서 뒤집을 걸 다 뒤집고 열이 뒤집어야 될 경우 뒤집었을 때 안되면
     안되는거 아닌가? 그렇게 한번 짜보자.
     또한 bfs로 deque에 배열을 넣을 때 이를 최소화 하고자 boolean으로 바꿨지만 메모리 오버가 떳다.
     dfs backtracking으로 가보자.

     */
    int rowLen, colLen;
    int Mn = Integer.MAX_VALUE;
    int[][] graph, target;
    public int solution(int[][] beginning, int[][] target) {
        this.rowLen = beginning[ 0 ].length; this.colLen = beginning.length;
        this.graph = beginning;
        this.target = target;

        // for( int x = 0; x < colLen; x ++ ){
        //     System.out.println( Arrays.toString( graph[ x ] ) );
        // }
        dfs( 0, graph, 0 );
        if( Mn == Integer.MAX_VALUE ) return -1;
        return Mn;
    }

    public void dfs( int depth, int[][] graph, int cnt ){
        if( depth == colLen ){
            // print( graph );
            int colCnt = 0;
            for( int y = 0; y < rowLen; y ++ ){
                int colCheck = 0;
                for( int x = 0; x < colLen; x ++ ){
                    if( this.graph[ x ][ y ] == this.target[ x ][ y ] ) colCheck++;
                }
                // System.out.println(" colIdx :" + y + "colCheck :" + colCheck );
                if( colCheck != colLen && colCheck != 0 ) return;
                //다 다르면 뒤집어야됨.
                if( colCheck == 0 ) colCnt++;
            }
            // System.out.println("ho");
            Mn = Math.min( Mn, colCnt + cnt );
            return;
        }

        dfs( depth + 1, graph, cnt );
        rowReverse( graph, depth );
        dfs( depth + 1, graph, cnt + 1 );
        rowReverse( graph, depth );
    }
    public void print( int[][] graph ){
        System.out.println("-------------------");
        for( int x = 0; x < colLen; x++ ){
            System.out.println( Arrays.toString( graph[ x ] ) );
        }
    }
    public int[][] deepCopy( int[][] target ){
        int[][] result = new int[ colLen ][ rowLen ];

        for( int x = 0; x < colLen; x ++ ){
            for( int y = 0; y < rowLen; y ++ ){
                result[ x ][ y ] = target[ x ][ y ];
            }
        }
        return result;
    }


    public void rowReverse( int[][] graph, int idx ){
        for( int y = 0; y < rowLen; y ++ ){
            graph[ idx ][ y ] ^= 1;
        }
    }
//     int rowLen, colLen;
//     int Mn = Integer.MAX_VALUE;
//     boolean[][] obj;
//     public int solution(int[][] beginning, int[][] target) {
//         int answer = 0;

//         rowLen = beginning[ 0 ].length; colLen = beginning.length;

//         ArrayDeque<QContent> dq = new ArrayDeque<>();
//         boolean[][] graph = new boolean[ rowLen ][ colLen ];
//         for( int x = 0; x < colLen; x ++ ){
//             for( int y = 0; y < rowLen; y ++ ){
//                 graph[ x ][ y ] = beginning[ x ][ y ] == 1 ? true : false;
//             }
//         }
//         dq.add( new QContent( graph, 0, new boolean[ rowLen ], new boolean[ colLen ] ) );
//         obj = new boolean[ colLen ][ rowLen ];

//         for( int x = 0; x < colLen; x ++ ){
//             for( int y = 0; y < rowLen; y ++ ){
//                 obj[ x ][ y ] = target[ x ][ y ] == 1 ? true : false;
//             }
//         }

//         while( !dq.isEmpty() ){
//             QContent now = dq.poll();

//             if( now.cnt > Mn ) continue;


//             if( isSame( now.graph ) ){
//                 Mn = now.cnt;
//                 continue;
//             }


//             for( int i = 0; i < rowLen; i ++ ){
//                 if( now.visitR[ i ] ) continue;

//                 boolean[] nextVisit = deepCopyVisit( now.visitR );
//                 nextVisit[ i ] = true;
//                 boolean[][] nextGraph = deepCopy( now.graph );
//                 rowReverse( nextGraph, i );

//                 dq.add( new QContent( nextGraph, now.cnt + 1, nextVisit, now.visitC ) );
//             }

//             for( int i = 0; i < colLen; i ++ ){
//                 if( now.visitC[ i ] ) continue;

//                 boolean[] nextVisit = deepCopyVisit( now.visitC );
//                 nextVisit[ i ] = true;
//                 boolean[][] nextGraph = deepCopy( now.graph );
//                 colReverse( nextGraph, i );

//                 dq.add( new QContent( nextGraph, now.cnt + 1, now.visitR, nextVisit ) );
//             }
//         }
//         if( Mn == Integer.MAX_VALUE ) return -1;
//         return Mn;
//     }

//     public class QContent{
//         boolean[][] graph;
//         int cnt;
//         boolean[] visitR, visitC;

//         public QContent( boolean[][] graph, int cnt, boolean[] visitR, boolean[] visitC ){
//             this.graph = graph;
//             this.cnt = cnt;
//             this.visitR = visitR;
//             this.visitC = visitC;
//         }
//     }

//     public boolean[][] deepCopy( boolean[][] target ){
//         boolean[][] result = new boolean[ colLen ][ rowLen ];

//         for( int x = 0; x < colLen; x ++ ){
//             for( int y = 0; y < rowLen; y ++ ){
//                 result[ x ][ y ] = target[ x ][ y ];
//             }
//         }
//         return result;
//     }

//     public boolean isSame( boolean[][] target ){

//         for( int x = 0; x < colLen; x ++ ){
//             for( int y = 0; y < rowLen; y ++ ){
//                 if( obj[ x ][ y ] != target[ x ][ y ] ) return false;
//             }
//         }
//         return true;
//     }

//     public boolean[] deepCopyVisit( boolean[] visit ){
//         boolean[] result = new boolean[ visit.length ];
//         for( int i = 0; i < visit.length; i ++ ){
//             result[ i ] = visit[ i ];
//         }

//         return result;
//     }

//     public void rowReverse( boolean[][] graph, int idx ){
//         for( int y = 0; y < rowLen; y ++ ){
//             graph[ idx ][ y ] = !graph[ idx ][ y ];
//         }
//     }

//     public void colReverse( boolean[][] graph, int idx ){
//         for( int x = 0; x < colLen; x ++ ){
//             graph[ x ][ idx ] = !graph[ x ][ idx ];
//         }
//     }

}