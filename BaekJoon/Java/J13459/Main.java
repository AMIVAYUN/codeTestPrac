package J13459;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n, m, graph[][], dx[] = { -1, 1, 0, 0 }, dy[] = { 0, 0, -1, 1 }, red[], blue[], goal[];

    static int MnCnt = 11;



    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());

        graph = new int[ n ][ m ];

        for( int i = 0; i < n; i++ ){
            String row = bf.readLine();
            for( int j = 0; j < m; j ++ ){
                char c = row.charAt( j );
                if( c == '#' ){
                    graph[ i ][ j ] = -1;
                }else if( c == '.'){
                    graph[ i ][ j ] = 0;
                }else if( c == 'R' ){
                    red = new int[]{ i, j };
                }else if( c == 'B' ){
                    blue = new int[]{ i, j };
                }else{
                    graph[ i ][ j ] = 1;
                    goal = new int[] { i, j };
                }
            }
        }

        bfs();

//        int[][] next = move( graph, 2, red, blue );
//
//        System.out.println( "red: " + Arrays.toString( red ));
//        System.out.println( "blue: " + Arrays.toString( blue ) );
//
//        print( next );
//        bfs();
//        move( 3, red, blue );
//        System.out.println("red " + Arrays.toString( red ));
//        System.out.println("blue " + Arrays.toString( blue ) );
//        System.out.println( "goal " + Arrays.toString( goal ));
        System.out.println( MnCnt < 11 ? 1 : 0 );


    }

    static void bfs(){
        ArrayDeque< Object[] > dq = new ArrayDeque<>();
        int[] tmpr = { red[ 0 ], red[ 1 ] };
        int[] tmpb = { blue[ 0 ], blue[ 1 ] };
        dq.add( new Object[]{ 0, tmpr, tmpb } );

        while( !dq.isEmpty() ){

            Object[] now = dq.poll();
//            int[][] subGraph = ( int[][] ) now[ 0 ];
            int cnt = ( int ) now[ 0 ];
            int[] r = ( int[] ) now[ 1 ];
            int[] b = ( int[] ) now[ 2 ];


            for( int i = 0; i < 4; i ++ ){
                move( i, r, b );
//                System.out.println( cnt + " dir:" + i );
//                System.out.println( "red " + Arrays.toString( red ) );
//                    System.out.println( "blue " + Arrays.toString( blue ) );
//                print( next );
                if( blue[ 0 ] == goal[ 0 ] && blue[ 1 ] == goal[ 1 ] ){
                    continue;
                }else if( red[ 0 ] == goal[ 0 ] && red[ 1 ] == goal[ 1 ]){
//                    System.out.println( i );
//                    System.out.println( "red " + Arrays.toString( red ) );
//                    System.out.println( "blue " + Arrays.toString( blue ) );
//                    print( next );
//
//                    System.out.println( "origin : ");
//                    print( graph );
//                    System.out.println( "red " + Arrays.toString( r ) );
//                    System.out.println( "blue " + Arrays.toString( b ) );
                    MnCnt = Math.min( MnCnt, cnt + 1 );
                    return;
                }else{
                    if( cnt + 1 < 11 ){
                        tmpr = new int[] { red[ 0 ], red[ 1 ] };
                        tmpb = new int[] { blue[ 0 ], blue[ 1 ] };
                        dq.add( new Object[]{ cnt + 1, tmpr, tmpb });
                    }

                }
            }
        }

    }

    static void print ( int[][] graph ){
        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
                System.out.print( graph[ i ][ j ] + " ");
            }
            System.out.println();
        }
    }

    static void move( int dir, int[] r, int[] b ){
//        System.out.println("dir: " + dir);
//        System.out.println( "red : " + Arrays.toString( red ));
//        System.out.println( "blue : " + Arrays.toString( blue ));
        /**
         * 각 방향에서 좀 더 그 방향에 가까운 친구가 먼저 움직여야 된다.
         */


        boolean isRed = isRedFirst( dir, r, b );
        int[] xys = isRed ? new int[]{ r[ 0 ], r[ 1 ], b[ 0 ], b[ 1 ] } : new int[] { b[ 0 ], b[ 1 ], r[ 0 ], r[ 1 ] };

        int fx, fy, lx, ly;
        fx = xys[ 0 ]; fy = xys[ 1 ]; lx = xys[ 2 ]; ly = xys[ 3 ];

        while( graph[ fx ][ fy ] >= 0 ){
//            System.out.println( fx + " " + fy + " : " + dir );
            if( fx == goal[ 0 ] && fy == goal[ 1 ] ){
                break;
            }

            int nx = fx + dx[ dir ]; int ny = fy + dy[ dir ];

            if( isIn( nx, ny ) ){
                if( graph[ nx ][ ny ] < 0 ){
                    break;
                }else{
                    fx = nx;
                    fy = ny;
                }
            }

        }

        if( !( goal[ 0 ] == fx && goal[ 1 ] == fy ) ){
            graph[ fx ][ fy ] = ( isRed ) ? -2 : -3;
        }

//        print( newGraph );
        while( graph[ lx ][ ly ] >= 0 ){
            if( lx == goal[ 0 ] && ly == goal[ 1 ] ){

                break;
            }

            int nx = lx + dx[ dir ]; int ny = ly + dy[ dir ];

            if( isIn( nx, ny ) ){
                if( graph[ nx ][ ny ] < 0 ){
                    break;
                }else{
                    lx = nx;
                    ly = ny;
                }
            }

        }

        graph[ fx ][ fy ] = 0;
        graph[ lx ][ ly ] = 0;

        if( isRed ){
            red = new int[] { fx, fy };
            blue = new int[]{ lx, ly };
        }else{
            red = new int[] { lx, ly };
            blue = new int[] { fx, fy };
        }


//        System.out.println( "after :" + Arrays.toString( red ) );
//        System.out.println( "after :" + Arrays.toString( blue ) );

    }

    static boolean isIn( int x, int y ){
        return x >=0 && x < n && y >= 0 && y < m;
    }

    static boolean isRedFirst( int dir, int[] red, int[] blue ){
        if( dir == 0 ){
            return red[ 0 ] <= blue[ 0 ];
        }else if( dir == 1 ){
            return red[ 0 ] >= blue[ 0 ];
        }else if( dir == 2 ){
            return red[ 1 ] <= blue[ 1 ];
        }else{
            return red[ 1 ] >= blue[ 1 ];
        }
    }
}