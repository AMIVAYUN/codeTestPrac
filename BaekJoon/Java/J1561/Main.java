package J1561;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	// SOL1 Time out
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer token;

	public static void main(String[] args) throws IOException {
		
		PriorityQueue< int[] > pq = new PriorityQueue<>( ( o1, o2 ) -> {
			if( o1[ 0 ] == o2[ 0 ] ) {
				return Integer.compare( o1[ 1 ], o2[ 1 ] );
			}
			return Integer.compare( o1[ 0 ], o2[ 0 ] );
		});
		
		
		token = new StringTokenizer( bf.readLine() );
		
		int n = Integer.parseInt( token.nextToken() );
		int m = Integer.parseInt( token.nextToken() );
		token = new StringTokenizer( bf.readLine() );
		for( int i = 0; i < m; i ++ ) {
			pq.offer( new int[] { 0, i ,Integer.parseInt( token.nextToken() ) } );
		}
		
		
		int turn = 0;
		int last = 0;
		while( turn < n ) {
			
			int[] next = pq.poll();
			
			int nexttime = next[ 0 ] + next[ 2 ];
			
			last = next[ 1 ];
			
			next[ 0 ] = nexttime;
			
			pq.offer( next );
			
			turn++;
		}
		
		System.out.println( last + 1 );

	}

}

