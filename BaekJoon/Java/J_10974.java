
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.*;

public class J_10974 {
	public static StringBuilder builder = new StringBuilder();
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
		int N =  Integer.parseInt( bf.readLine() );


		permutations( N );

		System.out.println( builder );

	}


	public static ArrayList< Integer > permutations( int n ) {

		ArrayList< Integer > numlst = new ArrayList<>();

		for( int i = 1; i < n + 1; i++ ) {
			numlst.add( i );
		}

		Queue< Stack< Integer > > q = new LinkedList<Stack<Integer>>();

		for( int i = 1; i < n + 1; i ++ ) {
			Stack< Integer > row = new Stack<>();
			row.add( i );
			q.add( row );
		}
		while( !q.isEmpty() ) {

			Stack< Integer > row = q.poll();

			if( row.size() == n ) {
				for( int r : row ) {
					builder.append( r + " " );
				}
				builder.append( "\n" );
				continue;
			}

			for( int i = 1; i < n + 1; i ++ ) {
				if( row.contains( i ) ) {
					continue;
				}

				Stack< Integer > temp = (Stack<Integer>) row.clone();
				temp.add( i );
				q.add( temp );


			}



		}



		return null;

	}

}
