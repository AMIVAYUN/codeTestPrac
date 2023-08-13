package J2635;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int f = 1;
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static ArrayList< Integer > ans = new ArrayList<>();
    static int Mx, n;
//    static int[] visit = new int[ 30000 ];
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(bf.readLine() );

        for( int i = 1; i < n + 1; i ++ ){
            dfs( 1, i, n, new ArrayList<>() );

        }
        System.out.println( Mx + 1 );
        StringBuilder builder = new StringBuilder();
        builder.append( n + " ");
        for( int i : ans ){
            builder.append( i + " " );
        }
        System.out.println( builder );
    }

    public static void dfs( int depth, int num, int prev, ArrayList< Integer > lst ){

        if( num < 0 ){
            if( Mx < depth - 1 ){
                ans = (ArrayList<Integer>) lst.clone();
            }
            Mx = Math.max( Mx, depth - 1 );

            return;
        }

        lst.add( num );
        dfs( depth + 1, prev - num, num, lst );
        lst.remove( lst.size() -1 );
    }
}
