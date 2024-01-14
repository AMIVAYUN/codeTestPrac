package J1561;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	// SOL1 Time out
	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer token;
	static long n, m;
	static int[] parts;

	public static void main(String[] args) throws IOException {

		token = new StringTokenizer(bf.readLine());
		n = Long.parseLong(token.nextToken());
		m = Long.parseLong(token.nextToken());

		if( n <= m ){
			System.out.println( n );
			return;
		}

		parts = new int[(int) m];
		token = new StringTokenizer(bf.readLine());
		for (int i = 0; i < m; i++) {
			parts[i] = Integer.parseInt(token.nextToken());
		}

		long[] start = getStartTimeByBST();


		long time = start[ 0 ] + 1;
		long remain = n - start[ 1 ];
//		System.out.println("time: " + start[0]);
//		System.out.println("start: " + Arrays.toString( start ));
		long ans = -1;
//		System.out.println( "re: " + remain);
		outer: while( remain > 0 ){

			for( int i = 0; i < (int) m; i ++ ){
				// 1인 경우는 따로 세줘야됨 ㅂㄷㅂㄷ
				if( time % parts[ i ] == 1 || parts[ i ] == 1 ){

					remain--;
					if( remain == 0 ){
						ans = i + 1;
						break outer;
					}
				}
			}

			time++;
		}

		System.out.println( ans );
//
//		for( int i = 0; i < (int) m; i ++ ){
//				if( parts[ i ]  ){
//					remain--;
//					if( remain == 0 ){
//						ans = i;
//						break;
//					}
//				}
//			}
//		}


//		System.out.println(Arrays.toString( start ));


//		PriorityQueue< int[] > pq = new PriorityQueue<>( ( o1, o2 ) -> {
//			if( o1[ 0 ] == o2[ 0 ] ) {
//				return Integer.compare( o1[ 1 ], o2[ 1 ] );
//			}
//			return Integer.compare( o1[ 0 ], o2[ 0 ] );
//		});
//
//
//		token = new StringTokenizer( bf.readLine() );
//
//		int n = Integer.parseInt( token.nextToken() );
//		int m = Integer.parseInt( token.nextToken() );
//		token = new StringTokenizer( bf.readLine() );
//		for( int i = 0; i < m; i ++ ) {
//			pq.offer( new int[] { 0, i ,Integer.parseInt( token.nextToken() ) } );
//		}
//
//
//		int turn = 0;
//		int last = 0;
//		while( turn < n ) {
//
//			int[] next = pq.poll();
//
//			int nexttime = next[ 0 ] + next[ 2 ];
//
//			last = next[ 1 ];
//
//			next[ 0 ] = nexttime;
//
//			pq.offer( next );
//
//			turn++;
//		}
//
//		System.out.println( last + 1 );


	}
	private static long[] getStartTimeByBST() {

		long lt = 0,rt =  60000000001l;
		long ans = 0, anscnt = 0;

		while( lt <= rt ){
			long mid = ( lt + rt ) / 2;
			long cnt = 0;
			for( int i = 0; i < m; i ++ ){
				cnt += mid % parts[ i ] == 0 ? mid / parts[ i ]: mid / parts[ i ] + 1;
			}

			if( cnt >= n ){
				rt = mid - 1;

			}else{
				lt = mid + 1;
				ans = mid;
				anscnt = cnt;

			}

		}

		return new long[]{ ans, anscnt };

	}

}

