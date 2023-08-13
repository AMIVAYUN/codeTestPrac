package J2304;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int[] field;

    static ArrayList< int[] > nodes = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt( bf.readLine() );
        int pMx = 0; int vMx = 0; int vIdx = -1;
//        int pMn = Integer.MAX_VALUE;
        for( int i = 0; i < n; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            int p = Integer.parseInt( token.nextToken() );
            int v = Integer.parseInt(token.nextToken() );

            nodes.add( new int[]{ p, v } );
            pMx = Math.max( p, pMx );
            if( vMx < v ){
                vIdx = p;
                vMx = v;
            }
        }

        field = new int[ pMx + 1 ];
        for( int[] node: nodes ){
            field[ node[ 0 ] ] = node[ 1 ];
        }

        int[] roofs = new int[ pMx + 1 ];
        roofs[ vIdx ] = vMx ;
        roofs[ 0 ] = field[ 0 ];
        roofs[field.length - 1 ] = field[field.length -1 ];
        for( int i = 1; i < vIdx; i ++ ){
            roofs[ i ] = Math.max( roofs[ i - 1 ], field[ i ] );
        }

        for( int i = field.length - 2; i > vIdx; i -- ){
            roofs[ i ] = Math.max( roofs[ i + 1 ], field[ i ] );
        }

//        System.out.println( Arrays.toString( roofs ));
        int sum = 0;
        for( int i = 0; i < field.length; i ++ ){
            sum += roofs[ i ];
        }

        System.out.println( sum );
    }
}