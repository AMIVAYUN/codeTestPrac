package J2957;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static long cnt;


    public static void main(String[] args) throws IOException {

        Node root = new Node();
        int n = Integer.parseInt( bf.readLine() );
        StringBuilder sb = new StringBuilder();
        for( int i = 0; i < n; i ++ ){
            int k = Integer.parseInt( bf.readLine() );
            root.insert( k );
            sb.append( cnt );
            sb.append("\n");
        }

        System.out.println(sb);
    }

    static class Node{
        Node left, right;
        Integer value = null;

        void insert( int k ){
            Node pos = this;

            if( pos.value == null ){
                pos.value = k;
                return;
            }

            while( pos.value != null ){
//                System.out.println( pos.value );
                if( pos.value > k ){
                    if( pos.left == null ){
                        pos.left = new Node();
                    }
                    pos = pos.left;
                }else{
                    if( pos.right == null ){
                        pos.right = new Node();

                    }
                    pos = pos.right;
                }
                cnt++;
            }

            pos.value = k;
        }
    }
}