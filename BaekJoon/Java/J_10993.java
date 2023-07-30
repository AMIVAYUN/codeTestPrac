import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class J_10993{
    public static char[][] graph;
    public static int N;
    public static void main( String[] args ) throws IOException {

        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );

        N = Integer.parseInt( bf.readLine() );

        int ls = 1;
        int bias = 2;
        for( int i = 0; i < N - 1; i++ ){
            ls += bias;
            bias *= 2;
        }

        int size = ls * 2 - 1;

        graph = new char[ size ][ size ];

        for( int i = 0; i < size; i ++  ){
            Arrays.fill( graph[ i ], ' ' );
        }
        int startX;
        if( N % 2 == 0 ){
            int x = 0;
            int y = 0;
            startX = 0;
            printStar2k( ls, x, y, bias / 2 );
        }else{
            int x = size - 1;
            int y = 0;
            startX = size / 2;
            printStark( ls, x, y, bias / 2 );
        }
        StringBuilder builder = new StringBuilder();
        for( int i = startX; i < startX + size / 2 + 1; i ++ ){
            String srow = "";
            for( char c : graph[ i ] ){
                srow += c;
            }

            for( int k = srow.length() - 1 ; k > -1; k -- ){
                if( srow.charAt( k ) != ' ' ){
                    String result = srow.substring( 0, k + 1);
                    builder.append( result + "\n" );
                    break;
                }

            }


        }

        System.out.println( builder );



        /**
         *
         * 1, 5, 13
         *  1, 3, 7, 15,
         *  변 길이
         *  2 4 8 16
         */


    }



    public static void printStark( int ls, int x, int y, int nbias ){

        if( ls == 0 ) return;
        //변
        for( int i = y; i < y + ( ls * 2 ) - 1; i++ ){

            graph[ x ][ i ] = '*';
        }

        int bias = 0;
        //위에
        for( int i = x; i >= x - ls + 1; i -- ){
            graph[ i ][ y + bias ] = '*';
            graph[ i ][ y + ( ls * 2 ) - 2 - bias ] = '*';

            bias += 1;
        }
        int half = ls / 2;

        printStar2k( ls - nbias , x - half, y + half + 1, nbias / 2 );
    }


    public static void printStar2k( int ls , int x, int y, int nbias ){

        if( ls == 0 ) return;

        //변
        for( int i = y; i < y + ( ls * 2 ) - 1; i ++ ){

            graph[ x ][ i ] = '*';
        }


        int bias = 0;
        //아래
        for( int i = x; i < x + ls ; i ++ ){
            graph[ i ][ y + bias ] = '*';

            graph[ i ][ y + ( ls * 2 ) - 2 - bias ] = '*';
            bias += 1;
        }


        int half = ls / 2;

        printStark( ls - nbias, x + half , y + half + 1  , nbias / 2);
    }
}