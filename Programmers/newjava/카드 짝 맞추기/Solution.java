import java.util.*;
import java.io.*;
class Solution {
    public int r, c, board[][], n;
    public boolean[] visited;
    public int mn = Integer.MAX_VALUE;
    public boolean[] nums = new boolean[ 7 ];
    public int solution(int[][] board, int r, int c) {
        int answer = 0;
        this.r = r;
        this.c = c;
        this.board = board;


        for( int i = 0; i < 4; i ++ ){
            for( int j = 0; j < 4; j ++ ){
                if( board[ i ][ j ] != 0 ){
                    n++;
                    nums[ board[ i ][ j ] ] = true;
                }
            }
        }
        n/=2;
        visited = new boolean[ 7 ];
        permutation( 0, new ArrayList<>() );

        return mn;
    }

    public void permutation( int depth, ArrayList<Integer> order ){
        if( depth == n ){
            // System.out.println( order );
            getResult( r, c, order );
            return;
        }

        for( int i = 1; i < 7; i ++ ){
            if( !visited[ i ] && nums[ i ] ){
                visited[ i ] = true;
                order.add( i );
                permutation( depth + 1, order );
                order.remove( order.size() - 1 );
                visited[ i ] = false;
            }
        }
    }
    public void getResult( int r, int c, ArrayList<Integer> order ){
        int[] now = new int[]{ r, c };

        int cnt = 0;
        int[][] graph = new int[ 4 ][ 4 ];
        for( int i = 0; i < 4; i ++ ){
            for( int j = 0; j < 4; j ++ ){
                graph[ i ][ j ] = board[ i ][ j ];
            }
        }
        for( int i = 0; i < order.size(); i ++ ){
            int target = order.get( i );
            // System.out.println("now = " + Arrays.toString( now ) );
            cnt += move( graph, now, target  );
// System.out.println( "target = " + target + " cnt = " + cnt + "now = " + Arrays.toString( now )  );
            cnt += 1;
// System.out.println( "target = " + target + " cnt = " + cnt + "now = " + Arrays.toString( now )  );
            cnt += move( graph, now, target );
// System.out.println( "target = " + target + " cnt = " + cnt + "now = " + Arrays.toString( now )  );
            cnt += 1;
            // System.out.println( "target = " + target + " cnt = " + cnt + "now = " + Arrays.toString( now )  );

        }

        mn = Math.min( cnt, mn );
    }
    public int[] dx = { -1, 1, 0, 0 };
    public int[] dy = { 0, 0, -1, 1 };

    public boolean isRight( int x, int y ){
        return x >= 0 && x < 4 && y >= 0 && y < 4;
    }
    public int move( int[][] graph, int[] pos, int target ){

        int[][] visited = new int[ 4 ][ 4 ];
        for( int i = 0; i < 4; i ++ ) Arrays.fill( visited[ i ], Integer.MAX_VALUE );
        visited[ pos[ 0 ] ][ pos[ 1 ] ] = 0;
        ArrayDeque< int[] > dq = new ArrayDeque<>();
        dq.add( new int[]{ pos[ 0 ], pos[ 1 ], 0 } );

        while( !dq.isEmpty() ){
            int[] now = dq.poll();
            int x = now[ 0 ];
            int y = now[ 1 ];
            int c = now[ 2 ];

            if( graph[ x ][ y ] == target ){
                pos[ 0 ] = x;
                pos[ 1 ] = y;
                graph[ x ][ y ] = 0;
                return c;
            }

            for( int i = 0; i < 4; i ++ ){
                int nx = x + dx[ i ];
                int ny = y + dy[ i ];

                if( isRight( nx, ny ) ){
                    if( visited[ nx ][ ny ] > c + 1 ){
                        dq.add( new int[]{ nx, ny, c + 1 } );
                        visited[ nx ][ ny ] = c + 1;
                    }
                }
            }


            for( int i = 0; i < 4; i ++ ){
                int[] nextCtrl = getCtrl( graph, x, y, i );
                int nx = nextCtrl[ 0 ];
                int ny = nextCtrl[ 1 ];
                if( visited[ nx ][ ny ] > c + 1 ){
                    dq.add( new int[]{ nx, ny, c + 1 } );
                    visited[ nx ][ ny ] = c + 1;
                }

            }
        }

        return Integer.MAX_VALUE;

    }
    public int[] getCtrl( int[][] graph, int x, int y, int dir ){




        x = x + dx[ dir ];
        y = y + dy[ dir ];

        while( isRight( x, y ) ){
            if( graph[ x ][ y ] != 0 ){
                return new int[]{ x, y };
            }
            x = x + dx[ dir ];
            y = y + dy[ dir ];
        }


        return new int[]{ x - dx[ dir ], y - dy[ dir ] };


    }


}