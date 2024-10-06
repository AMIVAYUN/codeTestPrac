import java.util.*;
class Solution {
    private int[][] graph;
    private int[] dx = { 0, 0, -1, 1 }, dy = { -1, 1, 0, 0 };
    private int n;
    public int[] solution(String[][] places) {
        //체크는 전방 다 봐야 함.
        n = places.length;
        int[] answer = new int[ n ];
        for( int k = 0; k < n; k ++ ){
            String[] place = places[ k ];
            graph = new int[ 5 ][ 5 ];
            // System.out.println( Arrays.toString( place ) );
            for( int i = 0; i < 5; i ++ ){

                for( int j = 0; j < 5; j ++ ){
                    int val = 0;

                    if( place[ i ].charAt( j ) == 'P'){
                        val = 2;
                    }else if( place[ i ].charAt( j ) == 'X' ){
                        val = 1;
                    }
                    graph[ i ][ j ] = val;
                }
            }
            // for( int i = 0; i < 5; i ++ ){
            //     System.out.println(Arrays.toString( graph[ i ] ) );
            // }
            boolean result = true;
            for( int i = 0; i < 5 && result; i ++ ){
                for( int j = 0; j < 5; j ++ ){
                    if( graph[ i ][ j ] == 2 ){
                        if( !check( i, j ) ){
                            // System.out.println("found!!" + i + ", " + j + " " + k );
                            result = false;
                            break;
                        }
                    }
                }
            }
            answer[ k ] = result ? 1 : 0;


        }


        return answer;
    }

    private boolean check( int sx, int sy ){
        ArrayDeque< int[] > dq = new ArrayDeque<>();

        dq.add( new int[]{ sx, sy, 0 } );
        ArrayList< int[] > res = new ArrayList<>();
        while( !dq.isEmpty() ){
            int[] now = dq.poll();

            int x = now [ 0 ];
            int y = now [ 1 ];
            int cnt = now[ 2 ];

            if( graph[ x ][ y ] == 2 ){
                if( !( sx == x && sy == y ) ) res.add( new int[]{ x, y } );
            }

            for( int i = 0; i < 4; i ++ ){
                int nx = x + dx[ i ];
                int ny = y + dy[ i ];

                if( isRight( nx, ny ) ){
                    if( cnt + 1 < 3 ){
                        dq.add( new int[]{ nx, ny, cnt + 1 } );
                    }
                }
            }
        }
        // System.out.println( sx + " , " + sy + " "  );
        // for( int[] f : res ){
        //     System.out.println( Arrays.toString( f ) );
        // }
        for( int[] p : res ){
            if( Math.abs( sy - p[ 1 ] ) + Math.abs( sx - p[ 0 ] ) == 1 ){
                return false;
            }

            if( ( Math.abs( p[ 1 ] - sy ) == 2 ) || ( Math.abs( p[ 0 ] - sx ) == 2 ) ){
                int mx = sx + p[ 0 ]; int my = sy + p[ 1 ];
                mx /= 2; my /= 2;
                if( graph[ mx ][ my ] != 1 ) return false;

            }else{
                int dfx = p[ 0 ] - sx; int dfy = p[ 1 ] - sy;

                if( !( (graph[ sx + dfx ][ sy ] == 1) && (graph[ sx ][ sy + dfy ] == 1) ) ){
                    return false;
                }
            }
        }

        return true;
    }
    private boolean isRight( int x, int y ){
        return x >= 0 && x < 5 && y >= 0 && y < 5;
    }
}