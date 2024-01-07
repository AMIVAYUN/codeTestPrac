package J14501;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer token;
	static int n;
	public static void main(String[] args) throws IOException {
		
		// TODO Auto-generated method stub
		n = Integer.parseInt( bf.readLine() );
		
		int[][] lst = new int[ n ][ 3 ];
		
		for( int i = 0; i < n; i ++ ) {
			token = new StringTokenizer( bf.readLine() );
			
			int a = Integer.parseInt( token.nextToken() );
			int b = Integer.parseInt( token.nextToken() );
			
			lst[ i ][ 0 ] = a;
			lst[ i ][ 1 ] = b;
			lst[ i ][ 2 ] = i + 1 ;
		}
		
		
		int[][] field = new int[ n + 1 ][ n + 1 ];
		
		
		for( int i = 1 ;i < n + 1; i ++ ) {
			int[] now = lst[ i - 1 ];
			int pos = now[ 2 ];
			System.out.println( Arrays.toString( now ));
			for( int j = 1; j < n + 1; j ++ ) {
				
//				System.out.println( j + now[ 0 ] );
				if( j >= pos && j - now[ 0 ] >= 0 && j + now[ 0 ] <= n + 1 ) {
					field[ i ][ j ] = Math.max( field[ i - 1 ][ j ], field[ i - 1 ][ j - now[ 0 ] ] + now[ 1 ] );
				}else {
					field[ i ][ j ] =  Math.max(field[ i - 1 ][ j ],field[ i ][ j - 1 ] );
				}
				
			}
			System.out.println( Arrays.toString( field[ i ] ));
		}
		
		
		for( int i = 0; i < n + 1; i ++ ) {
			System.out.println( Arrays.toString( field[ i ] ));
		}
		

		
		
	}

}
