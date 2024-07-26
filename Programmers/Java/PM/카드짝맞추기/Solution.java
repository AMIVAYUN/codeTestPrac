package PM.카드짝맞추기;

import java.util.*;
import java.io.*;
class Solution {

    /**
     * 커서를 이용한 카드 선택
     * ctrl + 방향키 -> 누른키 방향에 있는 가장 가까운 카드 -> 없으면 맨 마지막
     * enter 카드 뒤집기
     * 1장을 enter하면 2번째가 enter될 때 까지 앞면을 유지
     * 두 카드가 같은 카드로서 enter가 된다면, 화면ㅇ서사라진다.


     // 몇장 제거된 상태에서 카드 그림을 알고 있을 때 남은 카드를 모두 제거하는데 필요한 조작 횟수의 최솟값을 원한다.

     enter와 방향키 모두 1회로 계산


     그러면 주어진 필드에서 두 쌍이 사라지는 최솟 값들을 실시간으로 구하자. -> 미리 구하면 의미가 없다. 매 경우의 수는 필드가 유동적

     그리디하게 전부 최소로 가면 반례가 터질 수 있다. -> 최소란 지우는 시작 커서와 끝 커서의 위치가 다르기 때문이다.

     모든 경우의 수를 나열하고, 거기에 맞는 최소 거리를 찾자.


     */
    int totalMn = Integer.MAX_VALUE;
    int[] dx = { -1, 1, 0, 0 }, dy = { 0, 0, -1, 1 };
    boolean[] nums = new boolean[ 7 ];
    int[][] board;
    int cardCnt = 0;
    boolean[] orderVisit = new boolean[ 7 ];
    int[] cursor = new int[ 2 ];
    public int solution(int[][] board, int r, int c){
        this.board = board;
        //x로 먼저 맞추는 경우의 수 vs y를 맞추는 경우의 수.
        cursor[ 0 ] = r;
        cursor[ 1 ] = c;
        for( int x = 0; x < 4; x ++ ){
            for( int y = 0; y < 4; y ++ ){
                if( board[ x ][ y ] != 0 ){
                    if( !nums[ board[ x ][ y ] ] ) cardCnt++;
                    nums[ board[ x ][ y ] ] = true;


                }
            }
        }
        getOrder( 0, new ArrayList<Integer>() );

        return totalMn;
    }

    public void getOrder( int depth, ArrayList<Integer> orders ){
        if( depth == cardCnt ){

            int[] pos = new int[ 2 ];
            pos[ 0 ] = cursor[ 0 ]; pos[ 1 ] = cursor[ 1 ];
            int cnt = 0;
            int[][] graph = deepcopy( board );
            // System.out.println("--------- orders : " + orders + "--------" + " pos : " + Arrays.toString( pos ));
            for( int target: orders ){


                //총 두번 가야됨.
                cnt += getCount( graph, target, pos );
                graph[ pos[ 0 ] ][ pos[ 1 ] ] = 0;
                // System.out.println( "pos: " + Arrays.toString( pos ) + "cnt = " + cnt );
                cnt += getCount( graph, target, pos );
                graph[ pos[ 0 ] ][ pos[ 1 ] ] = 0;
                // System.out.println( "pos: " + Arrays.toString( pos ) + "cnt = " + cnt );
                // System.out.println("------");
                // System.out.println(" target = " + target + "cnt = " + cnt );
            }

            totalMn = Math.min( totalMn, cnt );
            // System.out.println( "orders: " + orders + " cnt = " + cnt );
            return;
        }

        for( int i = 1; i < 7; i ++ ){
            if( !nums[ i ] ) continue;
            if( !orderVisit[ i ]  ){
                orderVisit[ i ] = true;
                orders.add( i );
                getOrder( depth + 1, orders );
                orderVisit[ i ] = false;
                orders.remove( orders.size() - 1 );
            }
        }
    }

    public int getCount( int[][] graph, int target, int[] pos ){


        ArrayDeque< int[] > dq = new ArrayDeque<int[]>();
        dq.add( new int[]{ pos[ 0 ], pos[ 1 ], 0 } );
        boolean[][] visited = new boolean[ 4 ][ 4 ];
        visited[ pos[ 0 ] ][ pos[ 1 ] ] = true;

        while( !dq.isEmpty() ){
            int[] now = dq.poll();
            int x = now[ 0 ]; int y = now[ 1 ]; int cnt = now[ 2 ];

            if( graph[ x ][ y ] == target ){
                pos[ 0 ] = x; pos[ 1 ] = y;
                return cnt + 1; // enter값도 더 해줘야 한다.
            }

            for( int i = 0; i < 4; i ++ ){
                int nx = x + dx[ i ];
                int ny = y + dy[ i ];

                if( isRight( nx, ny ) ){
                    if( !visited[ nx ][ ny ] ){
                        visited[ nx ][ ny ] = true;
                        dq.add( new int[]{ nx, ny, cnt + 1 } );
                    }
                }
                int ctrlPos[] = getCtrlPos( x, y, i, graph );
                if( !visited[ ctrlPos[ 0 ] ][ ctrlPos[ 1 ] ] ){
                    visited[ ctrlPos[ 0 ] ][ ctrlPos[ 1 ] ] = true;
                    dq.add( new int[]{ ctrlPos[ 0 ], ctrlPos[ 1 ], cnt + 1 } );
                }
            }
        }

        return Integer.MAX_VALUE;
    }

    public int[] getCtrlPos( int x, int y, int i, int[][] graph ){

        x += dx[ i ];
        y += dy[ i ];

        while( isRight( x, y ) ){
            if( graph[ x ][ y ] != 0 ){
                return new int[]{ x, y };
            }

            x += dx[ i ];
            y += dy[ i ];
        }

        x -= dx[ i ];
        y -= dy[ i ];

        return new int[]{ x, y };
    }

    public int[][] deepcopy( int[][] target ){
        int[][] newGraph = new int[ 4 ][ 4 ];
        for( int x = 0; x < 4; x ++ ){
            for( int y = 0; y < 4; y ++ ){
                newGraph[ x ][ y ] = target[ x ][ y ];
            }
        }
        return newGraph;
    }

    public boolean isRight( int x, int y ){
        return x >= 0 && x < 4 && y >= 0 && y < 4;
    }


}