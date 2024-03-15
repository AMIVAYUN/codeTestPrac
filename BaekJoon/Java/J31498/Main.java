package J31498;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

//걍 가니깐 작살남

public class Main {
    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringTokenizer token;

    static long a, b, c, d, k;

    static int tstart = 0, dstart = 0;
    static ArrayList<Long>[] memo;

    static long Mx = 0;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        a = stol( token.nextToken() );
        b = stol( token.nextToken() );

        token = new StringTokenizer( bf.readLine() );
        c = stol( token.nextToken() );
        d = stol( token.nextToken() );

        k = stol( bf.readLine() );


//        memo = new ArrayList[ 2 ];
//        for( int i = 0; i < 2; i ++ ){
//            memo[ i ] = new ArrayList<>();
//        }
//
//
//        memo[ 0 ].add( 0l );
//        memo[ 1 ].add( -1 * c );

        Mx = (a / k + 1);
        long cnt = BinarySearch();

        System.out.println( cnt );



    }



    private static long BinarySearch() {

        long cnt = -1;

        long lt = 0; long rt = Mx;

        while( lt <= rt ){
//            System.out.println( lt + " " + rt );
            long mid = ( lt + rt ) / 2;

            long toka = getSum2( 0, mid );
            long dd = getSum2( 1, mid );

            if( dd >= toka ){
                rt = mid - 1;
                continue;
            }

            if( toka >= a ){
                cnt = mid;
                rt = mid - 1;
            }else{
                lt = mid + 1;
            }

        }

        return cnt;

    }

    static long getSum2( int toka0doll1, long idx ){
        if( toka0doll1 == 1 ){
            return d * idx - c;
        }else{
            return ( idx * ( ( 2 * b ) - ( k * ( idx - 1 ) ) ) ) / 2;
        }
    }

    static long getSum( int toka0doll1, int idx ){

        int startIdx = toka0doll1 == 0 ? tstart : dstart;
        long sum = toka0doll1 == 0 ? memo[toka0doll1].get(tstart): memo[toka0doll1].get( dstart );

        for( int i = startIdx + 1; i <= idx; i ++){
            if( toka0doll1 == 1 ){
                sum += d;
                memo[ toka0doll1 ].add( sum );
            }else{
                long speed = b - ( i - 1 ) * k;
                if( speed < 0 ){
                    speed = 0;
                }
                sum += speed;
                memo[ toka0doll1 ].add( sum );
            }
        }

        if( toka0doll1 == 1 ){
            dstart = idx;
        }else{
            tstart = idx;
        }

        return memo[ toka0doll1 ].get(idx);
    }

    static Long stol( String token ){
        return Long.parseLong( token );
    }

    static Integer stoi( String token ){
        return Integer.parseInt( token );
    }

    static class Person{
        long speed;
        long pos;
        long bias;

        public Person(long speed, long pos, long bias) {
            this.speed = speed;
            this.pos = pos;
            this.bias = bias;
        }

        public Person(long speed, long pos) {
            this.speed = speed;
            this.pos = pos;
        }

        void move(){
            pos -= speed;
            speed -= bias;
            if( speed <= 0 ) speed = 0;
        }
    }
}
