import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main{
	
	static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer token;
	static Result[] arr;
	static int Mx;
	public static void main( String[] args ) throws IOException {
		int tc = Integer.parseInt( bf.readLine() );
		
		for( int t = 1; t <= tc; t ++ ) {
			int n = Integer.parseInt( bf.readLine() );
			Mx =0;
			arr = new Result[ n ];
			for( int i = 0; i < n; i ++ ) {
				token = new StringTokenizer( bf.readLine() );
				arr[ i ]= new Result( Integer.parseInt( token.nextToken() ), Integer.parseInt( token.nextToken() ) );
				
			}
			
			Arrays.sort( arr, ( r1, r2 ) -> {
				return Integer.compare( r1.first, r2.first );
			});
			
			 int answer = 1;
	         Result start = arr[ 0 ];
	         int Mn = start.second;
	         for( int i = 1; i < n; i ++ ) {
	        	 if( Mn == 1 ) {
	        		 break;
	        	 }
	        	 if( Mn > arr[ i ].second ){
	        		 Mn = arr[ i ].second;
	        		 answer++;
	        	 }
	         }
             sb.append( answer + "\n" );
	    

			
			
//			int s_first = lst.get( 0 ).first; int s_second = lst.get( 0 ).second; 
//			int cnt = 1;
//			for( int i = 1; i < lst.size(); i ++ ) {
//				if( s_first < lst.get( i ).first && s_second < lst.get( i ).second ) {
//					Mx = Math.max( cnt, Mx );
//					s_first = lst.get( i ).first;
//					s_second = lst.get( i ).second;
//					cnt = 1;
//				}else if( s_first < lst.get( i ).first ) {
//					cnt++;
//					s_first = lst.get( i ).first;
//					
//				}else if( s_second < lst.get( i ).second ) {
//					cnt++;
//					s_second = lst.get( i ).second;
//				}
//				
//				
//			}
//			Mx = Math.max( cnt, Mx );
//			System.out.println( Mx );
			
		}
		System.out.println( sb );
	}
	
	
	
	public static class Result{
		int first;
		int second;
		public Result(int first, int second) {
			
			this.first = first;
			this.second = second;
		}
		@Override
		public String toString() {
			return "Result [first=" + first + ", second=" + second + "]";
		}
		
		
	}
}