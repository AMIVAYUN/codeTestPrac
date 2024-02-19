package J18405;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int[] dx = { -1, 1, 0, 0 }, dy = { 0, 0, -1, 1 };

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );

        int n = Integer.parseInt( token.nextToken() ); int k = Integer.parseInt( token.nextToken() );

        int[][] graph = new int[ n ][ n ];

        List< Pos > lst = new ArrayList<>();

        for( int i = 0; i < n; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            for( int j = 0; j < n; j ++ ){
                graph[ i ][ j ] = Integer.parseInt( token.nextToken( ));
                if( graph[ i ][ j ] > 0 ){
                    lst.add( new Pos( i, j, graph[ i ][ j ] ) );
                }

            }
        }

        Collections.sort( lst );

        token = new StringTokenizer( bf.readLine() );

        int s = Integer.parseInt( token.nextToken() );
        int x = Integer.parseInt( token.nextToken() ) - 1;
        int y = Integer.parseInt( token.nextToken() ) - 1;

        int time = 0;
        ArrayDeque< Pos > dq = new ArrayDeque<>( lst );



        while( time < s ){
            int size = dq.size();
            int cnt = 0;
            while( cnt < size ){
                Pos pos  = dq.poll();
                if( pos.x == x && pos.y == y ){
                    graph[ x ][ y ] = pos.value;
                    time = s;
                    break;
                }
                for( int i = 0; i < 4; i ++ ){
                    int nx = pos.x + dx[ i ];
                    int ny = pos.y + dy[ i ];

                    if( nx >= 0 && nx < n && ny >= 0 && ny < n ){
                        if( graph[ nx ][ ny ] < 1 ){
                            graph[ nx ][ ny ] = pos.value;
                            dq.add( new Pos( nx, ny, pos.value ) );
                        }
                    }
                }

                cnt++;
            }

            time++;
        }

        System.out.println( graph[ x ][ y ] );




    }

    static class Pos implements Comparable<Pos>{
        int x;
        int y;
        int value;

        public Pos(int x, int y, int value) {
            this.x = x;
            this.y = y;
            this.value = value;
        }

        @Override
        public int compareTo(Pos o) {
            return Integer.compare( this.value, o.value );
        }
    }
}