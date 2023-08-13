package J2578;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int graph[][] = new int[ 5 ][ 5 ];
    static boolean[][] visit = new boolean[ 5 ][ 5 ];

    static int globalCnt = 0;
    static boolean[][] globalCheck = new boolean[ 5 ][ 5 ];

    static HashMap< Integer, int[] > map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        for( int i = 0; i < 5; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            for( int j = 0; j < 5; j ++ ){
                graph[ i ][ j ] = Integer.parseInt(token.nextToken() );
                map.put( graph[ i ][ j ], new int[]{ i, j } );
            }

        }
        int cnt = 0;
        for( int i = 0; i < 5; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            for( int j = 0; j < 5; j ++ ){
                int[] pos = map.get( Integer.parseInt(token.nextToken() ) );
                visit[ pos[ 0 ] ][ pos[ 1 ] ] = true;
                cnt += 1;
                allOver();
//                System.out.println( "---------");
//                for( boolean[] row: visit ){
//                    System.out.println( Arrays.toString(row ) );
//                }
//                System.out.println( "---------");
//                for( boolean[] row: globalCheck ){
//                    System.out.println( Arrays.toString(row ) );
//                }
//                System.out.println( "---------");
                if( globalCnt >= 3 ){


                    System.out.println( cnt );
                    return;
                }

            }

        }






    }
    static void allOver(){
        for( int x = 0; x < 5; x ++ ){
            for( int y = 0; y < 5; y ++ ){
                if( visit[ x ][ y ] ){
                    isEnd( x, y );
                }

            }
        }
    }
    private static void isEnd(int x, int y) {
        int[][] dxy0 = { { 1, -1 }, { -1, 1 } };
        int[][] dxy1 = { { -1, -1 }, { 1, 1 } };
        int[][] dxy2 = { { 1, 0 }, { -1, 0 } };
        int[][] dxy3 = { {0, 1 }, { 0, -1 } };

        int[][][] dxys = new int[ 4 ][][];
        dxys[ 0 ] = dxy0;
        dxys[ 1 ] = dxy1;
        dxys[ 2 ] = dxy2;
        dxys[ 3 ] = dxy3;
        int cnt = 0;
        for( int[][] dxy: dxys ){
            if( Bingo( dxy, x, y )  ){
                globalCnt++;
            }

        }


    }

    private static boolean Bingo( int[][] dxy, int x, int y ){
        int cnt = 1;
        if( globalCheck[ x ][ y ] ){
            return false;
        }
        boolean[][] check = new boolean[ 5 ][ 5 ];

        Deque< int[]> dq = new ArrayDeque();
        check[ x ][ y ] = true;
        dq.add( new int[]{ x, y } );

        while ( ! dq.isEmpty() ){
            int[] pos = dq.poll();
            int nowx = pos[ 0 ]; int nowy = pos[ 1 ];

            for( int[] dxdy : dxy ){
                int nx = nowx + dxdy[ 0 ];
                int ny = nowy + dxdy[ 1 ];

                if( isRight( nx, ny ) ){
                    if( visit[ nx ][ ny ] && !check[ nx ][ ny ] ){
                        check[ nx ][ ny ] = true;
                        dq.add( new int[]{ nx, ny } );
                        cnt++;
                    }
                }
            }

        }

        if( cnt == 5 ){
            union( check );

            return true;
        }
        return false;
    }
    static void union( boolean[][] check ){
        for( int x = 0; x < 5; x ++ ){
            for( int y = 0 ;y < 5; y ++ ){
                globalCheck[ x ][ y ] = globalCheck[ x ][ y ] | check[ x ][ y ];
            }
        }
    }
    static boolean isRight( int x, int y ){
        return x >= 0 && x < 5 && y >= 0 && y < 5;
    }
}