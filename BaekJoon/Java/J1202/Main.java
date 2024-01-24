package J1202;

import CallbyRefTest.A;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {


    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringTokenizer token;

    static int n, k;

//    static Jewerly[] jewerlies;
    static ArrayList< Jewerly > arr = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );

        n = Integer.parseInt( token.nextToken() );
        k = Integer.parseInt( token.nextToken() );
//        jewerlies = new Jewerly[ n ];
        arr = new ArrayList<>();
        int[] bagpacks = new int[ k ];
        for( int i = 0; i < n; i ++ ){
            token = new StringTokenizer(bf.readLine() );
            arr.add(  new Jewerly( Integer.parseInt( token.nextToken() ), Integer.parseInt( token.nextToken() ) ) );
//            jewerlies[ i ] = new Jewerly( Integer.parseInt( token.nextToken() ), Integer.parseInt( token.nextToken() ) );
        }

        for( int j = 0; j < k; j ++ ){
            bagpacks[ j ] = Integer.parseInt( bf.readLine() );
        }
//
//        Arrays.sort( jewerlies, (o1, o2) -> {
//            if( o1.m == o2.m ){
//                return Double.compare( (double) o1.v / o1.m, (double) o2.v / o2.m );
//            }
//            return Integer.compare( o1.m, o2.m );
//        });
//
//        Arrays.sort( bagpacks );
//
//        long cnt = 0;
//
//        for( int i = 0; i < k; i ++ ){
//            cnt += BinarySearch( bagpacks[ i ] );
//        }
//
//        System.out.println( cnt );

        Collections.sort( arr, ((o1, o2) -> Integer.compare( o1.m, o2.m ) ) );
        Arrays.sort( bagpacks );

        PriorityQueue< Integer > pq = new PriorityQueue<>( ( (o1, o2) -> {
            return Integer.compare( o2, o1 );
        }));
        long cnt = 0;
        int index = 0;
//        System.out.println( arr );
        outer:for( int bag: bagpacks ){

//            while( arr.size() > 0 && arr.get( 0 ).m <= bag ){
//
//                Jewerly k = arr.remove( 0 );
//                pq.add( k.v );
//            }
//            System.out.println( bag + " " + pq );
            while( index < n && arr.get( index ).m <= bag ){
                pq.add( arr.get( index++ ).v );
            }
            
            cnt += pq.size() > 0 ? pq.poll() : 0l;
        }
        System.out.println(cnt);
        //SOL2 OUT
//        long cnt = 0;
//        outer:for( int bag: bagpacks ){
//            for( int j = 0; j < arr.size(); j ++){
//                if( bag >= arr.get(j).m ){
//                    cnt += (long)arr.remove( j ).v;
//                    continue outer;
//                }
//            }
//        }

    }

    /*
        반례
        3 2
        1 65
        5 23
        2 99
        10
        2
     */
   /* private static long BinarySearch(int bagpack) {

        int lt = 0; int rt = n - 1;
        long ans = 0;
        while( lt <= rt ){
            int mid = ( lt + rt ) / 2;
//            System.out.println( mid + " " + jewerlies[ mid ].toString() + " " + bagpack );
            if( jewerlies[ mid ].m <= bagpack ){
                ans = jewerlies[ mid ].v;
                lt = mid + 1;
            }else{
                rt = mid - 1;
            }
        }
        return ans;
    }*/
}


class Jewerly{
    int m,v;

    public Jewerly(int m, int v) {
        this.m = m;
        this.v = v;
    }

    @Override
    public String toString() {
        return "Jewerly{" +
                "m=" + m +
                ", v=" + v +
                '}';
    }
}
