package J16236;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int dx[] = { -1, 0, 1, 0, }, dy[] = { 0, -1, 0, 1 };

    static int n, graph[][];

    static Shark shark;

    /*

        더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
        먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
        먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
        -> bfs 돌며 탐색

        거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
        -> 거리 재기
        거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
        -> 우선순위 좌상단 상먼저

        이동 즉시 물고기 먹음.


     */

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt( bf.readLine() );
        graph = new int[ n ][ n ];

        for( int i = 0; i < n; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            for( int j = 0; j < n; j ++ ){
                graph[ i ][ j ] = Integer.parseInt( token.nextToken() );
                if( graph[ i ][ j ] == 9 ){
                    shark = new Shark( i, j );
                    graph[ i ][ j ] = 0;
                }
            }
        }

        int time = 0;
        while( true ){
            int[] now = shark.find();
            if( now[ 0 ] == Integer.MAX_VALUE ){
                break;
            }

            time += now[ 0 ];
            shark.x = now[ 1 ]; shark.y = now[ 2 ];
            shark.exp ++;

            //레벨 업
            if( shark.size == shark.exp ){
                shark.size ++;
                shark.exp = 0;
            }
        }

        System.out.println( time );






    }


    static class Shark{

        int x, y;
        int size = 2;
        int exp = 0;

        public Shark(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int[] find(){
            ArrayDeque< int[] > dq = new ArrayDeque<>();
            int[] ans = new int[]{ Integer.MAX_VALUE, Integer.MAX_VALUE, Integer.MAX_VALUE };
            int[] start = new int[]{ this.x, this.y, 0 };
            boolean[][] visit = new boolean[ n ][ n ];
            visit[ this.x ][ this.y ] = true;
            dq.add( start );
            while( !dq.isEmpty() ){
                int[] now = dq.poll();
                int x = now[ 0 ];
                int y = now[ 1 ];
                int cnt = now[ 2 ];
                for( int i =0; i< 4; i ++ ){
                    int nx = x + dx[ i ];
                    int ny = y + dy[ i ];

                    if( nx >= 0 && nx < n && ny >= 0 && ny < n ){
                        if( !visit[ nx ][ ny ] && graph[ nx ][ ny ] <= this.size ){
                            if( graph[ nx ][ ny ] > 0 && graph[ nx ][ ny ] < this.size && cnt + 1 <= ans[ 0 ] ){
                                if( nx < ans[ 1 ] ) {
                                    ans = new int[]{cnt + 1, nx, ny};
                                }else if( nx == ans[ 1 ] ){
                                    if( ny < ans[ 2 ] ){
                                        ans = new int[]{ cnt + 1, nx, ny };
                                    }
                                }

                            }
                            visit[ nx ][ ny ] = true;
                            dq.add( new int[]{ nx, ny, cnt + 1 } );
                        }
                    }
                }
            }

            if( ans[ 0 ] != Integer.MAX_VALUE ){
                graph[ ans[ 1 ] ][ ans[ 2 ] ] = 0;
            }
            return ans;
        }

    }
}