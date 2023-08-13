package J2042;

import java.io.*;
import java.util.*;
public class Main {
	
	static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) ) ;
	static StringTokenizer token;
	static int n, m, k;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		StringTokenizer token = new StringTokenizer( bf.readLine() );
		n = Integer.parseInt( token.nextToken() ); m = Integer.parseInt( token.nextToken() ); k = Integer.parseInt( token.nextToken() );
		long[] lst = new long[ n ];
		for( int i = 0; i < n; i ++ ) {
			lst[ i ] = Long.parseLong( bf.readLine() );
		}
		
		
		SegmentTree tree = new SegmentTree( lst );
		StringBuilder sb = new StringBuilder();
		for( int i = 0; i < m + k; i ++ ) {
			token = new StringTokenizer( bf.readLine() );
			int c = Integer.parseInt( token.nextToken() ); long start = Long.parseLong( token.nextToken() ); long end = Long.parseLong( token.nextToken() );
//			System.out.println( Arrays.toString( tree.nodes ) );
			if( c == 1 ) {
				tree.update( ( int )start, end );
			}else {
				sb.append( tree.getSum( ( int )start, ( int )end ) + "\n" );

			}
			
		}
		

//		System.out.println( a );
//		System.out.println( Arrays.toString( tree.nodes ) );
		System.out.println( sb );
		
	}
	
	
	
	
	
	static class SegmentTree{
		int k;
		long[] nodes;
		int bk;
		
		public SegmentTree( long[] lst ) {
			// TODO Auto-generated constructor stub
			this.k = getK( lst.length );
			this.nodes = new long[ (int) Math.pow( 2, k + 1 ) ];
			
			bk = (int) Math.pow( 2, k );
			for( int i = 0; i < lst.length; i ++ ) {
				nodes[ i + bk ] = lst[ i ];
			}
			
			
			for( int i = nodes.length - 1; i > 0; i-- ) {
				nodes[ i / 2 ] += nodes[ i ];
			}
		
		}
		
		public int getK( int length ) {
			return (int) ( Math.ceil( Math.log( length ) / Math.log( 2 ) ) );
		}
		
		public void update( int idx, long value ) {
			idx -= 1;
			int start = bk + idx;
			long diff = (long)value - nodes[ start ];
			while( start > 0 ) {
				
				nodes[ start ] += diff;
				
				start /= 2;
			}
			
		}
		
		public long getSum( int start, int end ) {
			
			start -= 1; end -= 1;
			long sum = 0;
			start += bk; end += bk;
			
			while( start <= end ) {
				if( start % 2 == 1 ) {
					sum += nodes[ start ];
					start = ( start + 1 ) / 2;
					
				}else {
					start /= 2;
				}
				
				if( end % 2 == 0 ) {
					sum += nodes[ end ];
					end = ( end - 1 ) / 2;
				}else {
					end /= 2;
				}
				
				
			}
			
			return sum;
			
			
		}
		
		
		
		
		
		
	}

}
