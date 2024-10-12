import java.util.*;
class Solution {
    /**

     1개씩 300개가 1000분에 100분 요청하면?

     1000 + 100 * 300

     20c10 = 184756

     */
    int mn = Integer.MAX_VALUE;
    boolean[] visit;
    int[] counters;
    int k, n;
    ArrayList<int[]>[] procreqs;
    public int solution(int k, int n, int[][] reqs) {
        int answer = 0;
        counters = new int[ k ];
        this.n = n;
        this.k = k;
        procreqs= new ArrayList[ k ];



        for( int i = 0; i < k; i ++ ){
            procreqs[ i ] = new ArrayList<>();
        }

        for( int[] req: reqs ){
            int c = req[ 2 ] - 1;
            procreqs[ c ].add( req );
        }

        comb( 0, n );
        return mn;
    }

    public void comb( int depth, int remain ){
        if( depth == k ){
            System.out.println( Arrays.toString( counters ) );
            getResult();
            return;
        }

        if( depth < k && remain < 1 ) return;

        if( depth + 1 == k ){
            counters[ depth ] = remain;
            comb( depth + 1, 0 );
            counters[ depth ] = 0;
            return;
        }

        for( int i = 1; i < remain; i ++){

            counters[ depth ] = i;
            comb( depth + 1, remain - i );
            counters[ depth ] = 0;
        }
    }
    public void getResult(){
        int mx = 0;
        for( int i = 0; i < k; i ++ ){

            int idx = 0;
            ArrayList<int[]>reqs = procreqs[ i ];
            PriorityQueue< int[] > pq = new PriorityQueue<>( ( p1, p2 ) -> {

                return Integer.compare( p1[ 0 ] + p1[ 1 ], p2[ 0 ] + p2[ 1 ] );

            });
            if( reqs.size() <= counters[ i ] ) continue;

            for( idx = 0; idx < counters[ i ]; idx++ ){
                int[] now = reqs.get( idx );
                pq.add( now );
            }

            while( idx < reqs.size() ){

                int[] next = reqs.get( idx );
                int[] newNext = new int[ 3 ];
                newNext[ 0 ] = next[ 0 ]; newNext[ 1 ] = next[ 1 ]; newNext[ 2 ] = next[ 2 ];
                int[] now = pq.poll();
                if( now[ 0 ] + now[ 1 ] > next[ 0 ] ){
                    mx += now[ 0 ] + now[ 1 ] - next[ 0 ];
                    newNext[ 0 ] = now[ 0 ] + now[ 1 ];
                }
                pq.add( newNext );
                idx++;
            }

        }

        this.mn = Math.min( mn, mx );
    }

}