package J1374;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n;
    static ArrayList< Class > classes = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        n = stoi( bf.readLine());

        for( int i = 0; i < n; i ++ ){
            token = new StringTokenizer( bf.readLine());
            classes.add( new Class( stoi( token.nextToken() ),stoi( token.nextToken() ),stoi( token.nextToken() ) ) );
        }

        Collections.sort( classes );

        PriorityQueue< Integer > pq = new PriorityQueue<Integer>();

        for( Class lec : classes ){
            if( !pq.isEmpty() && pq.peek() > lec.start ){
                pq.add( lec.end );
            }else{
                if( !pq.isEmpty() ){
                    pq.poll();
                }

                pq.add( lec.end );
            }
        }

        System.out.println( pq.size() );

    }

    public static int stoi(String token){
        return Integer.parseInt( token );
    }

    static class Class implements Comparable< Class >{
        int start;
        int end;
        int idx;

        public Class(int idx, int start, int end) {
            this.start = start;
            this.end = end;
            this.idx = idx;
        }

        @Override
        public int compareTo(Class o) {
            if( this.start == o.start ){
                return Integer.compare( this.end, o.end );
            }
            return Integer.compare( this.start, o.start );
        }
    }
}
