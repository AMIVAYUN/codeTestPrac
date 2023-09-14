package J13460;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringTokenizer token;
    static char[][] graph;
    static int n,m;
    static int[] r,b,e;
    static boolean[][][][] visit;
    static int Mn = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub

        token = new StringTokenizer( bf.readLine() );
        n = Integer.parseInt( token.nextToken() ); m = Integer.parseInt( token.nextToken() );
        graph = new char[ n ][ m ];
        visit = new boolean[ n ][ m ][ n ][ m ];

        for( int x = 0; x < n ; x ++ ) {
            String row = bf.readLine();
            for( int y = 0; y< m; y ++ ) {
                graph[ x ][ y ] = row.charAt( y );
                if( graph[ x ][ y ] == 'R' ) {
                    r = new int[] { x, y };
                    graph[ x ][ y ] = '.';

                }else if( graph[ x ][ y ] == 'B' ) {
                    b = new int[] { x, y };
                    graph[ x ][ y ] = '.';
                }else if( graph[ x ][ y ] == 'O' ) {
                    e = new int[] { x, y };
                }
            }
        }


        bfs();
        System.out.println( Mn == Integer.MAX_VALUE ? -1 : Mn );
    }
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };
    private static void bfs() {
        Queue< int[] > dq = new ArrayDeque<int[]>();

        dq.add( new int[] { r[ 0 ], r[ 1 ], b[ 0 ], b[ 1 ] , 0 } );
        visit[ r[ 0 ] ][ r[ 1 ] ][ b[ 0 ] ][ b[ 1 ] ] = true;
        while( !dq.isEmpty() ) {
            int size = dq.size();
//			for( int[] row: dq ) {
//				System.out.print( Arrays.toString( row ) );
//			}
//			System.out.println();
            while( size-- > 0 ) {
                int pos[] = dq.poll();

                int rx= pos[ 0 ]; int ry = pos[ 1 ];
                int bx = pos[ 2 ]; int by = pos[ 3 ];
                int cnt = pos[ 4 ];
                if( cnt > 10 ) {
                    continue;
                }

                if( isEnd( rx,ry,bx,by ) ) {
                    if( isRightEnd( rx,ry,bx,by ) ) {
                        Mn = Math.min( Mn, cnt );
                    }
                    continue;
                }
                if( Mn < cnt ) {
                    continue;
                }

                for( int i = 0; i < 4; i ++ ) {
                    int[] nr = move( rx, ry, i );
                    int[] nb = move( bx, by, i );

                    int nrx = nr[ 0 ]; int nry = nr[ 1 ];
                    int nbx = nb[ 0 ]; int nby = nb[ 1 ];

                    if( nrx == nbx && nry == nby && graph[ nbx ][ nby ] != 'O') {
                        if( nr[ 2 ] > nb[ 2 ] ) {
                            nrx -= dx[ i ];
                            nry -= dy[ i ];
                        }else {
                            nbx -= dx[ i ];
                            nby -= dy[ i ];
                        }

                    }

                    if( visit[ nrx ][ nry ][ nbx ][ nby ] == false ) {
                        visit[ nrx ][ nry ][ nbx ][ nby ] = true;
                        dq.add( new int[] { nrx, nry, nbx, nby, cnt + 1 } );
                    }


                }






            }
        }





    }
    private static int[] move(int x, int y, int i) {
        int nx = x;
        int ny = y;
        int cnt = 0;
        while( graph[ nx + dx[ i ] ][ ny + dy[ i ] ] != '#' && graph[ nx ][ ny ] != 'O' ) {
            nx += dx[ i ];
            ny += dy[ i ];
            cnt++;
        }
        return new int[] { nx, ny, cnt };
    }
    private static boolean isRightEnd(int rx, int ry, int bx, int by) {
        // TODO Auto-generated method stub
        return ( rx == e[ 0 ] && ry == e[ 1 ] ) || ( bx == e[ 0 ] && by == e[ 1 ] );
    }
    private static boolean isEnd(int rx, int ry, int bx, int by) {
        // TODO Auto-generated method stub
        return ( rx == e[ 0 ] && ry == e[ 1 ] ) && !( bx == e[ 0 ] && by == e[ 1 ] );
    }




}
