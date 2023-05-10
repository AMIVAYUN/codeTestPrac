import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class J_1753  {
    public static void main( String[] args ) throws IOException {
        /*
        방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
         */


        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );


        List<Integer> lst = Arrays.stream(bf.readLine().split(" ")).map( Integer::parseInt ).collect( Collectors.toList() );
        int V = lst.get( 0 ); int E = lst.get( 1 );
        int K = Integer.parseInt( bf.readLine() );
        HashMap< Long, ArrayList< long[] > > map = new HashMap<>();
        ArrayList< ArrayList< long[] > > mapper = new ArrayList<>();
        for( int i = 0; i < V; i ++ ){
            mapper.add( new ArrayList<>() );
        }
        for( int i = 0; i < E; i++ ){
            List< Integer > s = Arrays.stream(bf.readLine().split(" ")).map( Integer::parseInt ).collect( Collectors.toList() );

            int u, v, w;
            u = s.get( 0 );
            v = s.get( 1 );
            w = s.get( 2 );

            long[] target = { w, v - 1 };

            ArrayList< long[] > tg = mapper.get( u - 1 );
            tg.add( target );
        }


        PriorityQueue< long[] > heap = new PriorityQueue<>(new Comparator<long[]>() {
            @Override
            public int compare(long[] o1, long[] o2) {
                if( o1[ 0 ] < o2[ 0 ] ){
                    return -1;
                }else if( o1[ 0 ] == o2[ 0 ] ){
                    return 0;
                }else{
                    return 1;
                }
            }
        });

        long[] dist = new long[ V ];
        Arrays.fill( dist, Long.MAX_VALUE );
        dist[ K - 1 ] = 0;
        long[] start = { 0, K - 1 };
        heap.add( start );

        while( !heap.isEmpty() ){
            long[] now = heap.remove();
            long cost, pos;
            cost = now[ 0 ]; pos = now[ 1 ];

            if( dist[ Long.valueOf( pos ).intValue() ] < cost ){
                continue;
            }


            for( long[] l : mapper.get( Long.valueOf( pos ).intValue() ) ){
                int next = Long.valueOf( l[ 1 ] ).intValue();
                if( cost + l[ 0 ] < dist[ next ] ){
                    dist[ next ] = cost + l[ 0 ];
                    long[] newpos = { cost + l[ 0 ], next };
                    heap.add( newpos );
                }
            }
        }


        Arrays.stream( dist ).forEach( i -> {
            if( i != Long.MAX_VALUE ){
                System.out.println( i );
            }else{
                System.out.println( "INF" );
            }


        } );







    }
}
