package PM.블록_이동하기;

import java.util.*;
class Solution {
    /**
     로봇이 움직일 때, 현재 놓여있는 상태를 유지하면서 이동

     회전의 조건
     축이되는 칸이 비어있는 경우

     n 5 ~ 100
     board = 0 or 1

     robot (0,0) (0,1) -> 0, 0 기준으로 가자

     dir 0 1 2 3 우 하 좌 상

     시계로 90도 돌기 반시계로 90도 돌기

     * 왼쪽 날개가 도냐 오른쪽 날개가 도냐 -> 볼 필요 없다 그냥 한점을 기준으로 가면 된다.

     */

    int Mn = 100001, board[][];

    int[] dx = { 0, 1, 0, -1 }, dy = { 1, 0, -1, 0 };

    int n;

    boolean[][][] visited;

    int[][][] dr = { { { -1, 0 }, { 0, 0 }, { -1, 1 }, { 0, 1 } }, { {0, -1}, {1, -1}, {0, 0}, {1, 0} } };

    int[][][] drwall = { { {-1, 1}, {1, 1}, {-1, 0}, {1, 0} }, { {1, -1}, {0, -1}, {1, 1}, {0, 1} } };


    public int solution(int[][] board) {
        int answer = 0;
        this.board = board;
        n = board.length;
        visited = new boolean[ n ][ n ][ 2 ];
        visited[ 0 ][ 0 ][ 0 ] = true;

        ArrayDeque< int[] > dq = new ArrayDeque<>();

        int[] start = new int[]{ 0, 0, 0, 0 };
        dq.add( start );

        while( !dq.isEmpty() ){
            int[] now = dq.poll();

            int x = now[ 0 ];
            int y = now[ 1 ];
            int cnt = now[ 2 ];
            int vertical = now[ 3 ];

            int x2 = vertical == 0 ? x : x + 1;
            int y2 = vertical == 0 ? y + 1 : y;

            if( isEnd( x, y ) || isEnd( x2, y2 ) ){
                answer = cnt;
                break;
            }

            //이동
            for( int i = 0; i < 4; i ++ ){
                int nx = x + dx[ i ];
                int ny = y + dy[ i ];
                int nx2 = vertical == 0 ? nx : nx + 1;
                int ny2 = vertical == 0 ? ny + 1 : ny;
                if( isRight( nx, ny ) && isRight( nx2, ny2 ) ){
                    if( !visited[ nx ][ ny ][ vertical ] ){
                        visited[ nx ][ ny ][ vertical ] = true;
                        dq.add( new int[]{ nx, ny, cnt + 1, vertical } );
                    }
                }
            }

            //회전
            for( int i = 0; i < 4; i++ ){

                if( isRotatable( x, y, vertical, i ) ){
                    int nv = vertical == 0 ? 1 : 0;
                    int nx = x + dr[ vertical ][ i ][ 0 ];
                    int ny = y + dr[ vertical ][ i ][ 1 ];
                    int nx2 = nv == 0 ? nx : nx + 1;
                    int ny2 = nv == 0 ? ny + 1 : ny;
                    if( isRight( nx, ny ) && isRight( nx2, ny2 ) ){
                        if( !visited[ nx ][ ny ][ nv ] ){
                            visited[ nx ][ ny ][ nv ] = true;
                            dq.add( new int[]{ nx, ny, cnt + 1, nv } );
                        }
                    }
                }


            }
        }


        return answer;
    }



    public boolean isEnd( int x, int y ){
        return x == n - 1 && y == n - 1;
    }


    public boolean isRight( int x, int y ){
        return x >= 0 && x < n && y >= 0 && y < n && board[ x ][ y ] != 1;
    }

    public boolean isRotatable( int x, int y, int vertical ,int i ){
        int wx = x + drwall[ vertical ][ i ][ 0 ];
        int wy = y + drwall [ vertical ][ i ][ 1 ];

        if( isRight( wx, wy ) ){
            return board[ wx ][ wy ] != 1;
        }

        return false;
    }


}