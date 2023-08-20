package J17136;


import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in  ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    static int[][] graph = new int[ 10 ][ 10 ];
    static int[] Mxs = { 0, 5, 5, 5, 5, 5 };
    static boolean[][] visit;
    static int Mn = Integer.MAX_VALUE;
    public static void main( String[] args ) throws IOException {
        int tot = 0;
        for( int i = 0; i < 10; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            for( int j = 0; j < 10; j ++ ){
                graph[ i ][ j ] =  Integer.parseInt( token.nextToken() );
                if( graph[ i ][ j ] > 0 ){
                    tot++;
                }
            }


        }

        visit = new boolean[ 10 ][ 10 ];



        dfs2( tot, 0, 0, 0 );


        System.out.println( Mn == Integer.MAX_VALUE ? -1 : Mn );
    }
    static void dfs2( int tot, int x, int y, int cnt ){

        if( cnt > Mn ){
            return;
        }
        if( tot == 0 || y >= 10 ){
            Mn = Math.min( cnt, Mn );
//            System.out.println( Mn );
            return;
        }

        if( x >= 10 ){
            dfs2( tot, 0, y + 1, cnt );
            return;
        }


        if( graph[ x ][ y ]== 1 ){
            if( visit[ x ][ y ] == false ){
                for( int k = 5; k > 0; k -- ){
                    if( x + k > 10 || y + k > 10 ){
                        continue;
                    }
                    if( canBe( x, y, k ) ){

                        if( Mxs[ k ] - 1 >= 0 && cnt + 1 < Mn ){
                            Mxs[ k ]--;
                            fill( x, y, k );
                            dfs2( tot - k * k, x + k, y, cnt + 1 );
                            erase( x, y, k );
                            Mxs[ k ]++;
                        }

                    }

                }
            }
        }else{
            dfs2( tot, x + 1, y , cnt );
        }

    }
    static void dfs( int tot, int x, int y, int cnt ){
//        System.out.println( x + " " + y );
        if( cnt > Mn ){
            return;
        }
        if( tot == 0 ){
            /*for( boolean[] row: visit ){
                System.out.println(Arrays.toString( row ));
            }*/
            Mn = Math.min( cnt, Mn );
            System.out.println( Mn );
            return;
        }


        for( int i = 0; i < 10; i ++ ){
            for( int j = 0; j < 10; j ++ ){
                if( visit[ i ][ j ] == false ){
                    for( int k = 5; k > 0; k -- ){
                        if( i + k > 10 || j + k > 10 ){
                            continue;
                        }
                        if( canBe( i, j, k ) ){

                            if( Mxs[ k ] - 1 >= 0 && cnt + 1 < Mn ){
                                Mxs[ k ]--;
                                fill( i, j, k );
                                dfs( tot - k * k, i, j, cnt + 1 );
                                erase( i, j, k );
                                Mxs[ k ]++;
                            }

                        }

                    }
                }
            }
        }

    }
    static void fill( int x, int y, int width ){
        for( int i = x; i < x + width; i ++ ){
            for( int j = y; j < y + width; j ++ ){
                visit[ i ][ j ] = true;
                graph[ i ][ j ] = 0;
            }
        }
    }

    static void erase( int x, int y, int width ){
        for( int i = x; i < x + width; i ++ ){
            for( int j = y; j < y + width; j ++ ){
                visit[ i ][ j ] = false;
                graph[ i ][ j ] = 1;
            }
        }
    }

    static boolean canBe( int x, int y, int width ){
        for( int i = x;  i < x + width; i++ ){
            for( int j = y; j < y + width; j ++ ){
                if( graph[ i ][ j ] == 0 ){
                    return false;
                }
            }
        }

        return true;
    }



}