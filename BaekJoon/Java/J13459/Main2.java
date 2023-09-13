import java.io.*;
import java.util.ArrayDeque;
import java.util.StringTokenizer;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main2 {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in  ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    static int n, m;
    static char[][] graph;
    static int[] r, b, e;
    static boolean flag = false;
    public static void main( String[] args ) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = Integer.parseInt(token.nextToken() ); m = Integer.parseInt( token.nextToken() );

        graph = new char[ n ][ m ];
        for( int i = 0; i < n; i ++ ){
            String row = bf.readLine();
            for( int j = 0; j < m; j ++ ){
                graph[ i ][ j ] = row.charAt( j );

                if( graph[ i ][ j ] == 'R' ){
                    r = new int[]{ i, j };
                }else if( graph[ i ][ j ] == 'B' ){
                    b = new int[]{ i, j };
                }else if( graph[ i ][ j ] == 'O' ){
                    e = new int[]{ i, j };
                }
            }
        }



//        dfs( 0 );
        bfs();
        System.out.println( flag ? 1 : 0 );





    }
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };

    private static void bfs(){
        ArrayDeque< int[] > dq = new ArrayDeque<>();
        boolean[][][][] visit = new boolean[ n ][ m ][ n ][ m ];
        dq.add( new int[]{ r[ 0 ], r[ 1 ], b[ 0 ], b[ 1 ], 0 } );
        while( !dq.isEmpty() && !flag ){
            int size = dq.size();

            while( size-- > 0 && !flag ){
                int[] now = dq.poll();
                int rx = now[ 0 ];
                int ry = now[ 1 ];
                int bx = now[ 2 ];
                int by = now[ 3 ];
                int cnt = now[ 4 ];
                if( isEnd2( rx, ry, bx, by ) ){
                    if( isRightEnd2( rx, ry, bx, by ) ){
                        flag = true;
                        break;
                    }
                }

                if( cnt == 10 ){
                    continue;
                }

                for( int i = 0; i < 4; i ++ ){
                    int nextR[] = move( rx, ry, i );
                    int nextB[] = move( bx, by, i );

                    if( nextR[ 0 ] == nextB[ 0 ] && nextR[ 1 ] == nextB[ 1 ] && graph[ nextR[ 0 ] ][ nextR[ 1 ] ] != 'O' ){
                        if( nextR[ 2 ] > nextB[ 2 ] ){
                            if( visit[ nextR[ 0 ] - dx[ i ] ][ nextR[ 1 ] - dy[ i ] ][ nextB[ 0 ] ][ nextB[ 1 ] ] == false ){
                                visit[ nextR[ 0 ] - dx[ i ] ][ nextR[ 1 ] - dy[ i ] ][ nextB[ 0 ] ][ nextB[ 1 ] ] = true;
                                dq.add( new int[]{ nextR[ 0 ] - dx[ i ] ,nextR[ 1 ] - dy[ i ], nextB[ 0 ],  nextB[ 1 ], cnt + 1 } );
                            }

                        }else{
                            if( visit[ nextR[ 0 ] ][ nextR[ 1 ] ][ nextB[ 0 ] - dx[ i ]][ nextB[ 1 ] - dy[ i ] ] == false ){
                                visit[ nextR[ 0 ] ][ nextR[ 1 ] ][ nextB[ 0 ] - dx[ i ]][ nextB[ 1 ] - dy[ i ] ] = true;
                                dq.add( new int[] { nextR[ 0 ], nextR[ 1 ], nextB[ 0 ] - dx[ i ], nextR[ 1 ] - dy[ i ], cnt + 1 } );
                            }

                        }
                    }else{
                        if( visit[ nextR[ 0 ] ][ nextR[ 1 ] ][ nextB[ 0 ] ][ nextB[ 1 ] ] == false ){
                            visit[ nextR[ 0 ] ][ nextR[ 1 ] ][ nextB[ 0 ] ][ nextB[ 1 ] ] = true;
                            dq.add( new int[]{ nextR[ 0 ], nextR[ 1 ], nextB[ 0 ], nextB[ 1 ], cnt + 1  } );
                        }


                    }



                }


            }
        }
    }


    private static void dfs( int depth ) {

        if( isEnd() ){
            if( isRightEnd() ){
                flag = true;
            }
            return;
        }
        if( depth == 10 ){
            return;
        }

        int r_x = r[ 0 ]; int r_y = r[ 1 ];
        int b_x = b[ 0 ]; int b_y = b[ 1 ];


        for( int i = 0; i < 4; i ++ ){
            if( flag ) return;
            int[] nextR = move( r_x, r_y , i);
            int[] nextB = move( b_x, b_y, i );
            if( nextR[ 0 ] == nextB[ 0 ] && nextR[ 1 ] == nextB[ 1 ] && graph[ nextR[ 0 ] ][ nextR[ 1 ] ] != 'O' ){
                if( nextR[ 2 ] > nextB[ 2 ] ){
                    r[ 0 ] = nextR[ 0 ] - dx[ i ]; r[ 1 ] = nextR[ 1 ] - dy[ i ];
                    b[ 0 ] = nextB[ 0 ]; b[ 1 ] = nextB[ 1 ];
                }else{
                    r[ 0 ] = nextR[ 0 ]; r[ 1 ] = nextR[ 1 ];
                    b[ 0 ] = nextB[ 0 ] - dx[ i ]; b[ 1 ] = nextR[ 1 ] - dy[ i ];
                }
            }else{
                r[ 0 ] = nextR[ 0 ]; r[ 1 ] = nextR[ 1 ];
                b[ 0 ] = nextB[ 0 ]; b[ 1 ] = nextB[ 1 ];

            }

            dfs( depth + 1 );
            r[ 0 ] = r_x;
            r[ 1 ] = r_y;
            b[ 0 ] = b_x;
            b[ 1 ] = b_y;

        }

    }

    static int[] move( int i, int j, int dir){
        int x = i; int y = j; int cnt = 0;
        while( graph[ x + dx[ dir ] ][ y + dy[ dir ] ] != '#' && graph[ x ][ y ] != 'O' ){
            x += dx[ dir ];
            y += dy[ dir ];
            cnt++;
        }

        return new int[] { x, y, cnt };
    }

    private static boolean isRightEnd() {
        return ( r[ 0 ] == e[ 0 ] && r[ 1 ] == e[ 1 ] ) && !( b[ 0 ] == e[ 0 ] && b[ 1 ] == e[ 1 ] );
    }

    private static boolean isEnd() {
        return ( r[ 0 ] == e[ 0 ] && r[ 1 ] == e[ 1 ] ) || ( b[ 0 ] == e[ 0 ] && b[ 1 ] == e[ 1 ] );
    }


    private static boolean isRightEnd2( int rx, int ry, int bx, int by ) {
        return ( rx == e[ 0 ] && ry == e[ 1 ] ) && !( bx == e[ 0 ] && by == e[ 1 ] );
    }

    private static boolean isEnd2( int rx, int ry, int bx, int by ) {
        return ( rx == e[ 0 ] && ry == e[ 1 ] ) || ( bx == e[ 0 ] && by == e[ 1 ] );
    }
}