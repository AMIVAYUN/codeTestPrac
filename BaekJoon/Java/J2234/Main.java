package J2234;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer token;
	static int n, m;
	static int[][] graph, mapper;
	static boolean[][] visit;
	static int cnt, Mx, Mxa;
	static int[] dx = { 0, -1, 0, 1 };
	static int[] dy = { -1, 0, 1, 0 };
	static int idx = 1;
	static int wh[];
	public static void main(String[] args) throws IOException {
		
		token = new StringTokenizer( bf.readLine() );
		
		m = Integer.parseInt( token.nextToken() );
		n = Integer.parseInt( token.nextToken() );
		
		graph = new int[ n ][ m ];
		visit = new boolean[ n ][ m ];
		mapper = new int[ n ][ m ];
		for( int i = 0; i < n ; i ++ ) {
			token = new StringTokenizer( bf.readLine() );
			for( int j = 0; j < m; j ++ ) {
				graph[ i ][ j ] = Integer.parseInt( token.nextToken() );
			}
		}
		wh= new int[ n * m ];
		
		for( int x = 0; x < n; x ++ ) {
			for( int y = 0; y < m; y ++ ) {
				if( visit[ x ][ y ] ) {
					continue;
				}
				bfs( x, y );
				
			}
		}
			

		for( int x = 0; x < n; x ++ ) {
			for( int y = 0; y < m; y ++ ) {
				for( int i = 0; i < 4; i ++ ) {
					int nx = x + dx[ i ];
					int ny = y + dy[ i ];
					if( isRight( nx, ny ) ) {
						if( mapper[ nx ][ ny ] != mapper[ x ][ y ] ) {
							Mxa = Math.max( Mxa, wh[ mapper[ x ][ y ] - 1 ] + wh[ mapper[ nx ][ ny ] - 1 ] );
						}
					}
				}
			}
		}
		
		System.out.println( cnt );
		System.out.println( Mx );
		System.out.println( Mxa );
		
		

	}
	private static void bfs(int sx, int sy) {
		Queue< Pos > q = new ArrayDeque< Pos >();
		int scnt = 0;
		
		
		visit[ sx ][ sy ] = true;
		q.add( new Pos( sx, sy ) );
		mapper[ sx ][ sy ] = idx;
		
		while( !q.isEmpty() ) {
//			System.out.println( q.toString() ); 
			Pos now = q.poll();
			
			int x = now.x;
			int y = now.y;
			
			scnt ++;
			
			for( int i = 0; i < 4; i ++ ) {
				if( isAvailable( graph[ x ][ y ], i ) ) {
					int nx = x + dx[ i ];
					int ny = y + dy[ i ];
					if( isRight( nx, ny ) ) {
						if( visit[ nx ][ ny ] == false ) {
							visit[ nx ][ ny ] = true;
							q.add( new Pos( nx, ny ) );
							mapper[ nx ][ ny ] = idx;
						}
					}
				}
			}	
		}

		cnt++;
		wh[ idx - 1 ] = scnt;
		
		idx++;
		Mx = Math.max( scnt , Mx );
		
		
	}
	private static boolean isRight(int nx, int ny) {

		return nx >= 0 && nx < n && ny >= 0 && ny < m;
	}
	private static boolean isAvailable(int target, int i ) {
		return !(( target & ( 1 << i ) ) > 0);
	}

	
	
	static class Pos{
		int x;
		int y;
		@Override
		public String toString() {
			return "Pos [x=" + x + ", y=" + y + "]";
		}
		public Pos(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * result + x;
			result = prime * result + y;
			return result;
		}
		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			Pos other = (Pos) obj;
			if (x != other.x)
				return false;
			if (y != other.y)
				return false;
			return true;
		}
		
		
	}

}
