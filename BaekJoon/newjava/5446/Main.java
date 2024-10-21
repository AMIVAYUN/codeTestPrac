import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n, k;
    static int answer;

    static ArrayList< Node > lst = new ArrayList<>();

    public static void main(String[] args) throws IOException {

        int t = stoi( bf.readLine() );

        for( int i = 0; i < t; i ++ ){
            Node trie = new Node();
            n = stoi( bf.readLine() );
            for( int j = 0; j < n; j ++ ){
                trie.insert( bf.readLine() );
            }
            k = stoi( bf.readLine() );

            for( int j = 0; j < k; j ++ ){
                trie.insertNotDelete( bf.readLine() );
            }
            boolean root = true;
            for( Node c : trie.child.values() ){
                if( !c.isDeletable ){
                    root = false;
                    break;
                }
            }
            System.out.println( root ? 1 : trie.dfs() );
        }



    }

    public static int stoi( String s ){
        return Integer.parseInt( s );
    }


    static class Node {
        HashMap<Character, Node> child = new HashMap<>();
        boolean end = false;
        boolean isDeletable = true;



        public void insert( String str ) {
            Node pos = this;
            for (int i = 0; i < str.length(); i++) {
                char cur = str.charAt( i );
                pos.child.putIfAbsent( cur, new Node() );
                pos = pos.child.get( cur );
                if( i == str.length() - 1 ){
                    pos.end = true;
                }
            }

        }

        public void insertNotDelete(String str) {
            Node pos = this;

            for (int i = 0; i < str.length(); i++) {
                char cur = str.charAt( i );
                if ( !pos.child.containsKey( cur ) ) {
                    return;
                }
                pos.child.get( cur ).isDeletable = false;
                pos = pos.child.get( cur );
            }
        }

        public int dfs() {
            int ret = 0;

            for ( Character key : child.keySet() ) {
                Node next = child.get(key);
                if (next != null) {
                    if ( next.end && !next.isDeletable ) {
                        ret++;
                    }
                    if ( next.isDeletable ) {
                        ret++;
                    } else {
                        ret += next.dfs();
                    }
                }
            }
            return ret;
        }
    }


}