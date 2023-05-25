import java.util.*;
import java.io.*;
public class J_1027 {
    public static double getInc( int[] pos1, int[] pos2 ){
        return ( ( double )pos2[ 1 ] - pos1[ 1 ] ) / ( pos2[ 0 ] - pos1[ 0 ] );
    }

    public static int getRight( int[] lst, int idx ){
        double Mx = -1 * Integer.MAX_VALUE;
        int[] stan = { idx, lst[ idx ] };

        int cnt = 0;

        for( int i = idx + 1; i < lst.length; i ++ ){
            int[] target = { i, lst[ i ] };
            double inc = getInc( stan, target );

            if( Mx < inc ){
                Mx = inc;
                cnt += 1;
            }
        }

        return cnt;

    }

    public static int getLeft( int[] lst, int idx ){
        double Mn = Integer.MAX_VALUE;
        int[] stan = { idx, lst[ idx ] };

        int cnt = 0;

        for( int i = idx - 1; i > -1; i -- ){
            int[] target = { i, lst[ i ] };
            double inc = getInc( stan, target );

            if( Mn > inc ){
                Mn = inc;
                cnt += 1;
            }
        }

        return cnt;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in) );
        String s1 = bf.readLine();
        int n = Integer.parseInt( s1 );

        String[] slst = bf.readLine().split(" " );

        int[] lst = Arrays.stream( slst ).mapToInt( Integer::parseInt ).toArray();

        int Mx = 0;

        for( int i = 0; i < lst.length; i++ ){
            int cnt = 0;

            cnt += getLeft( lst, i );
            cnt += getRight( lst, i );
            Mx = Math.max( cnt, Mx );
        }

        System.out.println( Mx );

    }




}
