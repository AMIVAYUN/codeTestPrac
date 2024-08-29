package J2251;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    /**
     * 0 1, 0 2, 1 0, 1 2, 2 0, 2 1
     */

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static boolean[][][] visit = new boolean[ 201 ][ 201 ][ 201 ];

    static int dx[][] = { {0,0},{ 1, 2 },{ 2, 1 },{ 0, 2 },{ 2, 0 },{ 0, 1 },{ 1, 0 } };
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        int[] Mxb = new int[ 3 ];


        for( int i = 0; i < 3; i ++ ){
            Mxb[ i ] = stoi( token.nextToken() );
        }

        Bottles Mx = new Bottles( Mxb[ 0 ], Mxb[ 1 ], Mxb[ 2 ] );

        Bottles bottles = new Bottles( 0, 0, Mx.c );
        ArrayDeque< Bottles > dq = new ArrayDeque<>();
        dq.add( bottles );

        visit[ bottles.a ][ bottles.b ][ bottles.c ] = true;
        HashSet< Integer > set = new HashSet<>();

        while( !dq.isEmpty() ) {
            Bottles now = dq.poll();

            int a = now.a;
            int b = now.b;
            int c = now.c;
            if( now.a == 0 ) set.add( now.c );
//            set.add( now.c );
//            System.out.println( now.a + " " + now.b +" " + now.c );

            if( a + b >= Mx.a ){
                if( !visit[ Mx.a ][ a + b - Mx.a ][ c ] ){
                    visit[ Mx.a ][ a + b - Mx.a ][ c ] = true;
                    dq.add( new Bottles( Mx.a, a + b - Mx.a, c ) );
                }
            }else{
                if( !visit[ a + b ][ 0 ][ c ] ){
                    visit[ a + b ][ 0 ][ c ] = true;
                    dq.add( new Bottles( a + b, 0, c ) );
                }
            }

            if( a + c >= Mx.a ){
                if( !visit[ Mx.a ][ b ][ a + c - Mx.a ] ){
                    visit[ Mx.a ][ b ][ a + c - Mx.a ] = true;
                    dq.add( new Bottles( Mx.a, b, a + c - Mx.a ) );
                }
            }else{
                if( !visit[ a + c ][ b ][ 0 ] ){
                    visit[ a + c ][ b ][ 0 ] = true;
                    dq.add( new Bottles( a + c, b, 0 ) );
                }
            }

            if( b + a >= Mx.b ){
                if( !visit[ a + b - Mx.b ][ Mx.b ][ c ] ){
                    visit[ a + b - Mx.b ][ Mx.b ][ c ] = true;
                    dq.add( new Bottles( a + b - Mx.b, Mx.b , c  ) );
                }
            }else{
                if( !visit[ 0 ][ b + a ][ c ] ){
                    visit[ 0 ][ b + a ][ c ] = true;
                    dq.add( new Bottles( 0, b + a, c ) );
                }
            }

            if( b + c >= Mx.b ){
                if( !visit[ a ][ Mx.b ][ b + c - Mx.b ] ){
                    visit[ a ][ Mx.b ][ b + c - Mx.b ] = true;
                    dq.add( new Bottles( a, Mx.b, b + c - Mx.b ) );
                }
            }else{
                if( !visit[ a ][ b + c ][ 0 ] ){
                    visit[ a ][ b + c ][ 0 ] = true;
                    dq.add( new Bottles( a, b + c, 0 ) );
                }
            }

            if( c + a >= Mx.c ){
                if( !visit[ a + c - Mx.c ][ b ][ Mx.c ] ){
                    visit[ a + c - Mx.c ][ b ][ Mx.c ] = true;
                    dq.add( new Bottles( a + c - Mx.c, b ,Mx.c ) );
                }
            }else{
                if( !visit[ 0 ][ b ][ c + a ] ){
                    visit[ 0 ][ b ][ c + a ] = true;
                    dq.add( new Bottles( 0, b, c + a ) );
                }
            }

            if( c + b >= Mx.c ){
                if( !visit[ a ][ c + b - Mx.c ][ Mx.c ] ){
                    visit[ a ][ c + b - Mx.c ][ Mx.c ] = true;
                    dq.add( new Bottles(  a , c + b - Mx.c ,Mx.c  ) );
                }
            }else{
                if( !visit[ a ][ 0 ][ c + b ] ){
                    visit[ a ][ 0 ][ c + b ] = true;
                    dq.add( new Bottles( a, 0, c + b ) );
                }
            }

        }
        List<Integer> result = set.stream().collect(Collectors.toList());
        Collections.sort( result );
        for( int key : result ){
            System.out.print( key + " " );
        }


    }

    public static Integer stoi( String token ){
        return Integer.parseInt( token );
    }

    static class Bottles{
        int a, b, c;

       public Bottles( int a, int b, int c ){
           this.a = a;
           this.b = b;
           this.c = c;
       }

    }




}
