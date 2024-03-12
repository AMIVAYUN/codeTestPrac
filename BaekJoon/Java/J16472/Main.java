package J16472;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    static int n, Mx;
    static String str;

    static int cnt;
    static int len;
    static Map< Character , Integer > map = new HashMap();
    static PriorityQueue< Pos > pq = new PriorityQueue<>(new Comparator<Pos>() {
        @Override
        public int compare(Pos o1, Pos o2) {
            return Integer.compare( o1.idx, o2.idx );
        }
    });
//    public static void main(String[] args) throws IOException {
//        n = stoi(bf.readLine());
//        str = bf.readLine();
//
//
//
//    }

    public static void main(String[] args) throws IOException {
        n = stoi( bf.readLine() );
        str = bf.readLine();

        if( str.length() <= n ){
            System.out.println( str.length() );
            return;
        }




        for( int i = 0; i < str.length(); i ++ ){
            int value = map.getOrDefault( str.charAt( i ), 0 );
            Mx = Math.max( Mx, len );
//            System.out.println("len:" + len + " cnt: " + cnt );
//            System.out.println( map.toString());
//            System.out.println(pq.toString());
//            System.out.println("----------");
            if( value != 0 ){
                len++;
                map.put( str.charAt( i ), i + 1 );
                Pos newPos = new Pos( str.charAt( i ), i + 1 );
                pq.remove( newPos );
                pq.add( newPos );
            }else{
                if( cnt + 1 <= n ){
                    cnt++;
                    len++;
                    map.put( str.charAt( i ), i + 1 );
                    Pos newPos = new Pos( str.charAt( i ), i + 1 );
                    pq.remove( newPos );
                    pq.add( newPos );
                }else{
                    Pos pos = pq.poll();
                    len = ( i + 1 ) - pos.idx;
                    map.remove( pos.chr );
                    Pos newPos = new Pos( str.charAt( i ), i + 1 );
                    map.put( str.charAt( i ), i + 1 );
                    pq.add( newPos );

                }
            }

        }

        Mx = Math.max( Mx, len );

        System.out.println(Mx);

    }

    public static class Pos{
        @Override
        public String toString() {
            return "Pos{" +
                    "chr=" + chr +
                    ", idx=" + idx +
                    '}';
        }

        Character chr;
        int idx;

        public Pos(Character chr, int idx) {
            this.chr = chr;
            this.idx = idx;
        }

        public Pos(Character chr) {
            this.chr = chr;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Pos pos = (Pos) o;
            return Objects.equals(chr, pos.chr);
        }

        @Override
        public int hashCode() {
            return Objects.hash(chr);
        }
    }

    public static Integer stoi(String s){
        return Integer.parseInt( s );
    }




}
