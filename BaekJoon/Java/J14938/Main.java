import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static PriorityQueue< Node > pq;

    static int n,m,r;

    static int[] items;

    static ArrayList<Node>[] graph;

    static int Mx = 0;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = stoi( token.nextToken() ); m = stoi( token.nextToken() ); r = stoi(token.nextToken() );
        items = new int[ n + 1 ];
        graph = new ArrayList[ n + 1 ];
        graph[ 0 ] = new ArrayList<>();
        token = new StringTokenizer( bf.readLine() );
        for( int i = 1; i < n + 1; i ++ ){
            items[ i ] = stoi( token.nextToken() );
            graph[ i ] = new ArrayList<>();
        }

        for( int i = 0; i < r; i ++ ){
            token = new StringTokenizer(bf.readLine());
            int x = stoi( token.nextToken() ); int y = stoi( token.nextToken() ); int cost = stoi( token.nextToken() );
            graph[ x ].add( new Node( y, cost ) );
            graph[ y ].add( new Node( x, cost ) );
        }
        if( n == 1 ){
            System.out.println( items[ 1 ] );
            return;
        }

        for( int i = 1; i < n + 1; i ++ ){
            dijkstra( i );
        }
        System.out.println( Mx );




    }

    static void dijkstra( int start ){
        int dists[] = new int[ n + 1 ];
        Arrays.fill( dists, Integer.MAX_VALUE );
        pq = new PriorityQueue<>( new NodeComparator() );
        int cnt = items[ start ];
        boolean visit[] = new boolean[ n + 1 ];
        visit[ start ] = true;
        dists[ start ] = 0;
        pq.add( new Node( start, 0 ) );

        while( !pq.isEmpty() ){
            Node now = pq.poll();
//            System.out.println( now );
            if( dists[ now.idx ] < now.cost ){
                continue;
            }

            for( Node next: graph[ now.idx ] ){
                int cost = next.cost + now.cost;
                if( cost <= m ){
                    dists[ next.idx ] = cost;
                    pq.add( new Node( next.idx, cost ) );
                    if( !visit[ next.idx ] ){
                        visit[ next.idx ] = true;
                        cnt += items[ next.idx ];
                    }
                }
            }

        }


        Mx = Math.max( Mx, cnt );

    }
    static Integer stoi( String token ){
        return Integer.parseInt( token );
    }
    static class NodeComparator implements Comparator< Node >{

        @Override
        public int compare(Node o1, Node o2) {
            return Integer.compare( o1.cost, o2.cost );
        }
    }

    static class Node{
        int idx;
        int cost;

        public Node(int idx, int cost) {
            this.idx = idx;
            this.cost = cost;
        }
        @Override
        public String toString() {
            return "Node{" +
                    "idx=" + idx +
                    ", cost=" + cost +
                    '}';
        }
    }
}