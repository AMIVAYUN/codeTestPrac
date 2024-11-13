package J2957;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main3 {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int[] memo = new int[ 300001 ];

    public static void main(String[] args) throws IOException {
        TreeSet<Integer> set = new TreeSet();
        int cnt = 0;
        int n = Integer.parseInt( bf.readLine() );
        StringBuilder sb = new StringBuilder();
        for( int i = 0; i < n; i ++ ){
            int k = Integer.parseInt( bf.readLine() );
            set.add(k);

            if( set.size() != 1 ){
                Integer rt = set.higher( k );
                Integer lt = set.lower( k );

                memo[ k ] = Math.max( lt != null ? memo[ lt ] : 0 , rt != null ? memo[ rt ] : 0 ) + 1;
                cnt += memo[ k ];

            }
            sb.append( cnt );
            if( i != n - 1 ){
                sb.append("\n");
            }
        }
        System.out.print(sb);

    }

}