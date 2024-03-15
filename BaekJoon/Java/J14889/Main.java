package J14889;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringTokenizer token;

    static int n;

    static int[][] graph;

    static boolean[] visit, visit2;
    static Integer Mn = Integer.MAX_VALUE;

    static ArrayList<int[]> arrayList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(bf.readLine());
        graph = new int[n][n];

        for (int i = 0; i < n; i++) {
            token = new StringTokenizer(bf.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = stoi(token.nextToken());
            }
        }
        visit = new boolean[n];
        getPair(0, 0, new int[2]);

//        for (int[] row : arrayList) {
//            System.out.println(Arrays.toString(row));
//        }

        getCombination( 0, 0 );
        System.out.println(Mn );
    }

    public static void getPair( int depth, int start, int[] now ){
        if( depth == 2 ){
            arrayList.add(Arrays.copyOf( now, 2 ) );
            return;
        }

        for( int i = start; i < n/2; i ++ ){
            now[ depth ]= i;
            getPair( depth + 1, i + 1, now  );
            }
    }

    public static void getCombination( int depth, int start ){
        if( depth == n / 2 ){
            getDiff();
            return;
        }

        for( int i = start; i < n; i++ ){
            if( !visit[ i ] ){
                visit[ i ] = true;
                getCombination( depth + 1, i + 1 );
                visit[ i ] = false;
            }
        }

    }

    private static void getDiff() {
        int sum1 = 0, sum2 = 0;
        int[] nums1 = new int[ n / 2 ], nums2 = new int[ n / 2 ];
        int idx1 = 0, idx2 = 0;
        for( int i = 0; i < n; i ++ ){
            if( visit[ i ] ){
                nums1[ idx1 ++ ] = i;
            }else{
                nums2[ idx2 ++ ] = i;
            }
        }

//        System.out.println("nums1: " + Arrays.toString(  nums1 ));
//        System.out.println("nums2: " +Arrays.toString(  nums2 ));
//;

        for( int[] row : arrayList ){
            sum1 += graph[ nums1[ row[ 0 ] ]][ nums1[ row[ 1 ] ] ] +  graph[ nums1[ row[ 1 ] ]][ nums1[ row[ 0 ] ] ];
            sum2 += graph[ nums2[ row[ 0 ] ] ][ nums2[ row[ 1 ] ] ] + graph[ nums2[ row[ 1 ] ] ][ nums2[ row[ 0 ] ] ];
        }

        Mn = Math.min( Mn, Math.abs( sum1 - sum2 ));


    }

    static Integer stoi( String token ){
        return Integer.parseInt( token );
    }
}
