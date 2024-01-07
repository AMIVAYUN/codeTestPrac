package J2110;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer token;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		// TODO Auto-generated method stub
/**
 * 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 
한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
 * 
 */
		token = new StringTokenizer( bf.readLine() );
		
		int n = Integer.parseInt( token.nextToken() );
		int m = Integer.parseInt( token.nextToken() );
		int Mx = 0;
		int[] nums = new int[ n ];
		
		for( int i = 0; i < n; i ++ ) {
			nums[ i ] = Integer.parseInt( bf.readLine() );
			Mx = Math.max( nums[ i ], Mx );
		}
		
		
		
		
		Arrays.sort( nums );
		
		int ans = 1;
		
		int lt = 1, rt = Mx;
		
		while( lt <= rt ) {
			
			int mid = ( lt + rt ) / 2;
			
			int cnt = get( nums, mid, m );
			
			if( cnt >= m ) {
				ans = mid;
				lt = mid + 1;
			}else {
				rt = mid - 1;
			}
			
		}
		
		System.out.println( ans ); 
		
		
	}
	
	static int get( int[] nums, int bias, int m ) {
		
		int idx = 1;
		int now = nums[ 0 ];
		int cnt = 1;
		while( idx < nums.length ) {
			
			if( nums[ idx ] - now >= bias ) {
				now = nums[ idx ];
				cnt++;
			}
			idx++;
			
		}
		
		return cnt;
		
	}

}

