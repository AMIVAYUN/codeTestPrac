package J2805;

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
	static long m;
	static long trees[];
	public static void main(String[] args) throws IOException {
		token = new StringTokenizer( bf.readLine() );
		n = Integer.parseInt( token.nextToken() );
		m = Long.parseLong( token.nextToken() );
		
		token = new StringTokenizer( bf.readLine() );
		
		trees = new long[ n ];
		
		for( int i = 0; i < n; i ++ ) {
			trees[ i ] = Long.parseLong( token.nextToken()  );
		}
		
		Arrays.sort( trees );

		
		long lt = 0; long rt = 1_000_000_000;
		long ans = 0;
		while( lt <= rt ) {
//			System.out.println( lt + " " + rt );
			long mid = ( lt + rt ) / 2;
			int idx = Arrays.binarySearch( trees, mid );
			
			long sum = 0;
			
			for( int i = 0; i < n; i ++ ) {
				if( trees[ i ] < mid ) continue;
				sum += trees[ i ] - mid;
			}
			
			
			if( sum >= m ) {
				ans = mid;
				lt = mid + 1;
			}else {
				rt = mid - 1;
			}
			
		}
		
		System.out.println( ans );
		

	}	

}
