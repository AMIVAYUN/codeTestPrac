package J1874;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;



    public static void main(String[] args) throws IOException {

        Stack< Integer > stack = new Stack<>();

        int n = Integer.parseInt( bf.readLine() );

        int num = 1;
        StringBuilder builder = new StringBuilder();



        for( int i = 0; i < n; i ++ ){
            int k = Integer.parseInt( bf.readLine() );


            while( num <= k ){
//                System.out.println( stack + " numL " +num + " " + k);
                stack.push( num++ );
                builder.append( "+\n");

            }
            if( !stack.isEmpty() && stack.peek() == k ){
                stack.pop();
                builder.append( "-\n" );
                continue;
            }

        }
        if( stack.isEmpty() && num == n + 1){
            System.out.println( builder );
        }else{
            System.out.println( "NO" );
        }


    }
}