package notSolved.J14904;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static J1103.Main.isRight;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n, k, graph[], start, end, parent[], capacity[], flow[], dx[] = new int[]{ 0, 1 }, dy[] = new int[]{ 1, 0 };

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(bf.readLine());
        n = stoi( token.nextToken() );
        k = stoi( token.nextToken() );

        graph = new int[ n * n ];


        start = 0;
        end = n * n - 1;

        parent = new int[ n * n ];
        capacity = new int[ n * n ];
        flow = new int[ n * n ];

        int total = 0;
        int cnt = 0;
        ArrayDeque<Integer> dq;
        while( true ){
            dq = new ArrayDeque<Integer>();
            Arrays.fill( parent, - 1 );
            parent[ start ] = start;
            dq.add( start );

            while( !dq.isEmpty() && parent[ end ] == -1 ){
                int now = dq.poll();
                int x = now / n;
                int y = now % n;

                for( int i = 0; i < 2; i ++ ){
                    int nx = x + dx[ i ];
                    int ny = y + dy[ i ];

                    if( isRight( nx, ny ) ){

                    }
                }

            }

        }

    }

    public static Integer stoi( String token ){
        return Integer.parseInt( token );
    }

    public static int getIdx( int i, int j ){
        return -1;
    }

    static class Edge{
         int pos, reverse, capacity, next;

        public Edge(int pos, int reverse, int capacity, int next) {
            this.pos = pos;
            this.reverse = reverse;
            this.capacity = capacity;
            this.next = next;
        }
    }
}
