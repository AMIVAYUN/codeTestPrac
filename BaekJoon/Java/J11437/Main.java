package J11437;

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

	public static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	public static StringTokenizer token;
	public static StringBuilder builder = new StringBuilder();
	public static int n;
	public static Node[] arr;

	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(bf.readLine());
		arr = new Node[n];

		for (int i = 0; i < n; i++) {
			arr[i] = new Node(i);

		}

		for (int i = 0; i < n - 1; i++) {
			token = new StringTokenizer(bf.readLine());
			int a = Integer.parseInt(token.nextToken()) - 1;
			int b = Integer.parseInt(token.nextToken()) - 1;

			arr[a].lst.add(b);
			arr[b].lst.add( a );
		}
		Queue<int[]> q = new ArrayDeque<>();

		q.add(new int[] { 0, 0 });
		boolean visit[] = new boolean[n];
		visit[0] = true;
		while (!q.isEmpty()) {
			int[] now = q.poll();

			int pos = now[0];
			int val = now[1];
			Node node = arr[pos];
			node.depth = val;
			for (int next : node.lst) {
				if (!visit[next]) {
					visit[next] = true;
					arr[next].parent = pos;
					q.add(new int[] { next, val + 1 });
				}

			}

		}

		int m = Integer.parseInt(bf.readLine());

		for (int i = 0; i < m; i++) {
			token = new StringTokenizer(bf.readLine());
			int a = Integer.parseInt(token.nextToken()) - 1;
			int b = Integer.parseInt(token.nextToken()) - 1;
			if (a > b) {
				int tmp = a;
				a = b;
				b = tmp;
			}

			find(a, b);
		}
	}

	private static void find(int a, int b) {
		while( !(a == b) ) {
//			System.out.println("origin : " + oa + "::" + ob  + " " + a + " " + b + " " + arr[ a ].depth + " " + arr[ b ].depth ); 
			if( arr[ a ].depth > arr[ b ].depth ) {

				a = arr[ a ].parent;
			}else if( arr[ a ].depth < arr[ b ].depth ) {

				b = arr[ b ].parent;
			}else {

				a = arr[ a ].parent;

				b = arr[ b ].parent;
			}
			
		}
		


//		System.out.println( oa + " : " + ob + "=" + a + "::" + b);

		System.out.println( a + 1 ); 
		
	}

	static class Node {

		int idx;
		int depth;
		List<Integer> lst;
		int parent;

		public Node(int i) {
			// TODO Auto-generated constructor stub
			this.idx = i;
			this.lst = new ArrayList<>();
		}

		public Node() {
			// TODO Auto-generated constructor stub
		}

		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * result + idx;
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
			Node other = (Node) obj;
			if (idx != other.idx)
				return false;
			return true;
		}

	}

}
