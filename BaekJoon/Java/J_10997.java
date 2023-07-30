import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.Arrays;

class J_10997{
    static char[][] graph;
    static int[][] visit;
    static int N;


    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );

        N = Integer.parseInt( bf.readLine() );
        graph = new char[ 4*( N - 1 ) + 3 ][ 4*( N - 1 ) + 1 ];
        for( int i = 0; i < 4*( N - 1 ) + 3; i ++ ){
            Arrays.fill( graph[ i ], ' ' );
        }
        visit = new int[ 4*( N - 1 ) + 3 ][ 4*( N - 1 ) + 1 ];
        if( N == 1 ){
            System.out.println( '*' );
            return;
        }
        printStar( N );

        /**
         *
         * 1 1
         * 2    ㄱㅏ로 5 세로 7
         * 3 가로 9 11
         *
         * 4 가로 13 15
         *
         */
        for( int i = 0; i < 4*( N -1 ) +3; i ++){
            if( i == 1 ){
                System.out.println( '*');
                continue;
            }
            char[] row = graph[ i ];
            String srow = "";
            for( char c : row ){
                srow += c;
            }
            System.out.println( srow );
        }

    }

    public static void printStar( int N ){
        int[][] dxy = { { 0, 1 }, { -1, 0 }, { 0, -1 }, { 1, 0 } };
        int[] pos = { 0, 4*( N - 1 )  };

        int direction = 2;
        graph[ pos[ 0 ] ][  pos[ 1 ] ] = '*';
        visit[ pos[ 0 ] ][ pos[ 1 ] ] = 1;
        int cnt = 3;
        int rows = 4*( N - 1 );
        int cols = 4 * (N - 1 ) + 2;
        while( rows > 1 || cols > 1 ){

            if( visit[ pos[ 0 ] ][ pos[ 1 ] ] > 2 ){
                break;
            }
            visit[ pos[ 0 ] ][ pos[ 1 ] ] += 1;
            if( cnt == 0 ) {
                cnt = 2;
                cols -= 2;
                rows -= 2;
            }
            int temps = direction % 2 == 1 ? cols : rows;
            for( int i = 0; i < temps; i ++ ){
                int[] next = { pos[ 0 ] + dxy[ direction ][ 0 ], pos[ 1 ] + dxy[ direction ][ 1 ]  };
                if( isRight( next[ 0 ], next[ 1 ] ) ){
                    pos = next;
                    graph[ pos[ 0 ] ][  pos[ 1 ] ] = '*';
                    visit[ pos[ 0 ] ][ pos[ 1 ] ] += 1;



                }
            }
            cnt -= 1;


            direction = (direction + 1) % 4;






        }



    }

    public static boolean isRight( int x, int y ){
        return x < 4*( N - 1 ) + 3 && x >=0  && y < 4*( N - 1 ) + 1 && y >= 0;
    }






}