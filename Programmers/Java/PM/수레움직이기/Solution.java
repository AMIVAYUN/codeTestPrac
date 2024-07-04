package PM.수레움직이기;

import java.util.*;
import java.io.*;
class Solution {
    int Mn = Integer.MAX_VALUE;
    /**
     * 0 빈칸
     * 1 r 시작
     * 2 b 시작
     * 3 r 도착
     * 4 b 도착
     */
    int[] dx = { -1, 1, 0, 0 };
    int[] dy = { 0, 0, -1, 1 };
    int[] redPos = new int[ 2 ], bluePos = new int[ 2 ], redArrive = new int[ 2 ], blueArrive = new int[ 2 ];
    int[][] graph;
    int m, n;
    boolean[][] redVisit;
    boolean[][] blueVisit;
    int[] prevRed = new int[ 2 ];
    public int solution(int[][] maze) {
        int answer = 0;
        n = maze.length;
        m = maze[ 0 ].length;
        graph = new int[ n ][ m ];
        redVisit = new boolean[ n ][ m ];
        blueVisit = new boolean[ n ][ m ];

        for( int x = 0; x < n; x ++ ){
            for( int y = 0; y < m; y ++ ){
                if( maze[ x ][ y ] == 1 ){
                    redPos[ 0 ] = x;
                    redPos[ 1 ] = y;
                    prevRed[ 0 ] = x;
                    prevRed[ 1 ] = y;
                }else if( maze[ x ][ y ] == 2 ){
                    bluePos[ 0 ] = x;
                    bluePos[ 1 ] = y;
                }else if( maze[ x ][ y ] == 3 ){
                    redArrive[ 0 ] = x;
                    redArrive[ 1 ] = y;
                }else if( maze[ x ][ y ] == 4 ){
                    blueArrive[ 0 ] = x;
                    blueArrive[ 1 ] = y;
                }else if( maze[ x ][ y ] == 5 ){
                    graph[ x ][ y ] = 1;
                }
            }
        }

        redVisit[ redPos[ 0 ] ][ redPos[ 1 ] ] = true;
        blueVisit[ bluePos[ 0 ] ][ bluePos[ 1 ] ] = true;


        move( 0, redPos[ 0 ], redPos[ 1 ], bluePos[ 0 ], bluePos[ 1 ] );

        if( Mn == Integer.MAX_VALUE ) return 0;

        return Mn;
    }

    public boolean isRight( int x, int y ){
        return x >= 0 && x < n && y >= 0 && y < m && graph[ x ][ y ] != 1;
    }

    public boolean isRedEnd( int x, int y ){
        return x == redArrive[ 0 ] && y == redArrive[ 1 ];
    }
    public boolean isBlueEnd( int x, int y ){
        return x == blueArrive[ 0 ] && y == blueArrive[ 1 ];
    }

    public void move( int cnt, int redX, int redY, int blueX, int blueY ){
        if( cnt > Mn ) return;

        if( isRedEnd( redX, redY ) && isBlueEnd( blueX, blueY ) ){
            Mn = cnt;
            return;
        }

        if( isRedEnd( redX, redY ) ){
            for( int i = 0; i < 4; i ++ ){
                int nx = blueX + dx[ i ];
                int ny = blueY + dy[ i ];
                if( isRight( nx, ny ) ){
                    if( !blueVisit[ nx ][ ny ] ){
                        if( nx == redX && ny == redY ) continue;
                        blueVisit[ nx ][ ny ] = true;
                        move( cnt + 1, redX, redY, nx, ny );
                        blueVisit[ nx ][ ny ] = false;
                    }
                }
            }

        }else if( isBlueEnd( blueX, blueY ) ){
            for( int i = 0; i < 4; i ++ ){
                int nx = redX + dx[ i ];
                int ny = redY + dy[ i ];
                if( isRight( nx, ny ) ){
                    if( !redVisit[ nx ][ ny ] ){
                        if( nx == blueX && ny == blueY ) continue;
                        redVisit[ nx ][ ny ] = true;
                        move( cnt + 1, nx, ny, blueX, blueY );
                        redVisit[ nx ][ ny ] = false;
                    }
                }
            }
        }else{
            for( int i = 0; i < 4; i ++ ){
                int nrx = redX + dx[ i ];
                int nry = redY + dy[ i ];
                for( int j = 0; j < 4; j ++ ){
                    int nbx = blueX + dx[ j ];
                    int nby = blueY + dy[ j ];

                    if( isRight( nrx, nry ) && isRight( nbx, nby ) ){
                        if( !redVisit[ nrx ][ nry ] && !blueVisit[ nbx ][ nby ] ){
                            if( !( nrx == nbx && nry == nby ) ){
                                if( !( nrx == blueX && nry == blueY && nbx == redX && nby == redY ) ){
                                    redVisit[ nrx ][ nry ] = true;
                                    blueVisit[ nbx ][ nby ] = true;
                                    move( cnt + 1, nrx, nry, nbx, nby );
                                    redVisit[ nrx ][ nry ] = false;
                                    blueVisit[ nbx ][ nby ] = false;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}