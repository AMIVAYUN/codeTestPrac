package J1300;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer token;
	static int n;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		n = Integer.parseInt( bf.readLine() );
		
		long k = Integer.parseInt(bf.readLine()) ;
		long Mx = 100_000_000;
		long ans = 0, lt = 1, rt = Mx * Mx;
		
//		System.out.println( "Rt: " + rt );
		
		if( k == 1 ) {
			System.out.println( 1 );
			return;
		}
		
		
		while( lt <= rt ) {
			long mid = ( lt + rt ) / 2;
//			System.out.println( mid + " " + getCnt( mid ));
			if( getCnt( mid ) <= k ) {
				ans = mid;
				lt = mid + 1;
			}else {
				rt = mid - 1;
			}
			
		}
		
		
		System.out.println( ans );
		
	}
	
	
	
	public static long getCnt( long k ) {
		long result = 0;
		for( long cnt = 1; cnt <= n; cnt ++ ) {
			if( k < cnt ) {
				break;
			}
			long val = ( k / cnt );
			if( k % cnt == 0 ) val--;
			
//			System.out.println( k + " :: " + result );
			result += ( val <= n ? val : n );
		}
		
		return result + 1;
	}
	

}

