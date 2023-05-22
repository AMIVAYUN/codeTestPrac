package PM.모두0으로만들기;



import java.util.*;
import java.io.*;
class Solution {
    public static int[] depths;
    public static int[] parents;
    ArrayList< ArrayList< Integer > > graph = new ArrayList<>();
    public void bfs(){



        Queue< Integer[] > q = new LinkedList<>();

        Integer[] start = new Integer[ 2 ];
        start[ 0 ] = 0; start[ 1 ] = 0;
        q.add( start );
        int[] visit = new int[ graph.size() ];
        Arrays.fill( visit, 1 );
        visit[ 0 ] = 0;

        while ( !( q.isEmpty() ) ){
            Integer[] pos = q.remove();

            int now = pos[ 0 ]; int depth = pos[ 1 ];

            ArrayList< Integer > nexts = graph.get( now );

            for( Integer next : nexts ){
                if( visit[ next ] == 1 ){
                    visit[ next ] = 0;
                    parents[ next ] = now;
                    depths[ next ] = depth + 1;
                    Integer[] nextpos = new Integer[ 2 ];
                    nextpos[ 0 ] = next; nextpos[ 1 ] = depth + 1;
                    q.add( nextpos );
                }

            }



        }

    }

    public long solution(int[] a, int[][] edges) {
        long answer = -2;
        parents = new int[ a.length ];
        depths = new int[ a.length ];

        int length = a.length;
        for( int i = 0; i < length; i ++ ){
            graph.add( new ArrayList< Integer >() );
        }
        for( int[] edge : edges ){
            int x, y;
            x = edge[ 0 ]; y = edge[ 1 ];
            ArrayList< Integer > xlst = graph.get( x );
            ArrayList< Integer > ylst = graph.get( y );
            xlst.add( y );
            ylst.add( x );
        }

        // depth 정렬 완료
        bfs();

        ArrayList< int[] > lst = new ArrayList<>();

        for( int i = 0; i < length; i++ ){
            int[] c = new int[ 2 ];
            c[ 0 ] = i; c[ 1 ] = depths[ i ];

            lst.add( c );
        }
        lst.sort( Comparator.comparing( o -> -1 * o[ 1 ] ) );
        answer = 0;
        long[] a_ = new long[ length ]; // 없으면 테케 7 11 OUT ;

        for( int i = 0; i < length; i ++ ){
            a_[ i ] = a[ i ];
        }

        for( int[] now: lst ){
            if( now[ 0 ] == 0 ){
                continue;
            }
            int node = now[ 0 ];

            answer += Math.abs( a_[ node ] );
            a_[ parents[ node ] ] += a_[ node ];
            a_[ node ] = 0;

        }




        if( a_[ 0 ] != 0 ){
            return -1;
        }
        return answer;
    }
}