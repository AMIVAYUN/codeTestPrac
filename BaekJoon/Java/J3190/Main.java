package J3190;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static boolean isEnd = false;
    static int n;

    static int[][] graph;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt( bf.readLine() );
        int k = Integer.parseInt( bf.readLine() );
        graph = new int[ n ][ n ];
        for( int i = 0; i < k; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            int x = Integer.parseInt(token.nextToken() );
            int y = Integer.parseInt( token.nextToken( ));
            x--; y--;
            graph[ x ][ y ] = 1;

        }
        int l = Integer.parseInt( bf.readLine() );
        Snake snake = new Snake( l );
        graph[ 0 ][ 0 ] = 2;

        for( int i = 0; i < l; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            int time = Integer.parseInt(token.nextToken() );
            char pos = token.nextToken().charAt( 0 );

            if( pos == 'D' ){
                snake.addCommand( new int[]{ time, 1 } );
            }else{
                snake.addCommand( new int[]{ time, 0 } );
            }
        }
        int t = 0;
        while( true ){
            snake.move( ++t );
//            print();
            if( isEnd ){
//                System.out.println( t );
                break;
            }

        }



    }
    static void print(){
        for( int[] row : graph ){
            System.out.println( Arrays.toString( row ) );
        }
    }

    static class Snake{
        int head_x = 0;
        int head_y = 0;

        int tail_x = 0;
        int tail_y = 0;
        Queue< int[] > commands = new ArrayDeque<>();
        int dir = 0;
        int[] direction_next = { -1, 1 };
        int[][] dxy = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };
        int ate = 0;

        int c_idx = 0;

        Queue< int[] > movelst = new ArrayDeque<>();
        public Snake( int l ){
        }

        public void addCommand( int[] command ){
            this.commands.add( command );
        }

        public void move( int t ) {
            head_x += dxy[ dir ][ 0 ];
            head_y += dxy[ dir ][ 1 ];
            movelst.add( new int[]{ head_x, head_y } );
            if( isEnd( head_x, head_y ) ){

                isEnd = true;
                System.out.println( t );
                return;
            }

            if( graph[ head_x ][ head_y ] == 1 ){
                graph[ head_x ][ head_y ] = 2;
            }else{
                graph[ head_x ][ head_y ] = 2;
                graph[ tail_x ][ tail_y ] = 0;
                int[] next = movelst.poll();

                tail_x = next[ 0 ];
                tail_y = next[ 1 ];


            }

            if( !commands.isEmpty() && commands.peek()[ 0 ] == t ){
                int[] ch = commands.poll();
                this.dir = ( this.dir + direction_next[ ch[ 1 ] ] ) % 4;
                if( this.dir < 0 ){
                    this.dir = 3;
                }
            }


        }
        public int[] findBody( int x, int y ){
            for( int i = 0; i < 4; i ++ ){
                int nx = x + dxy[ i ][ 0 ]; int ny = y + dxy[ i ][ 1 ];
                if( isRight( nx, ny ) && graph[ nx ][ ny ] == 2 ){
                    return new int[]{ nx, ny };
                }
            }
            return null;
        }

        public boolean isRight( int x, int y ){
            return ( x >= 0 && x < n && y >= 0 && y < n );
        }
        public boolean isEnd( int x , int y ){
//            print();
            if( isRight( x, y ) ){
                return graph[ x ][ y ] == 2;
            }else{
                return !( x >= 0 && x < n && y >= 0 && y < n );
            }




        }
    }
}
