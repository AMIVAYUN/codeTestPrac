package J9202;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;


    static int n, k;
    static String[] graph;
    static String[] words;

    static int[] dx = { 0, 0, -1, 1, -1, -1, 1, 1 };
    static int[] dy = { -1, 1, 0, 0, -1, 1, -1, 1 };

    static String found = "";
    static int cnt = 0;
    static int score = 0;
    static HashMap< String, Boolean > map;
    static boolean[][] visit;

    public static void main(String[] args) throws IOException {

        n = Integer.parseInt( bf.readLine() );
        Node trie = new Node();
        words = new String[ n ];
        for( int i = 0; i < n; i ++ ){
            words[ i ] = bf.readLine();
            trie.insert( words[ i ] );
        }
        bf.readLine();

        k = Integer.parseInt( bf.readLine() );

        for( int i = 0; i < k; i ++ ){
            found = "";
            cnt = 0;
            score = 0;
            graph = new String[ 4 ];
            map = new HashMap<>();
            for( int j = 0; j < 4; j++ ){
                graph[ j ] = bf.readLine();
            }
//            ArrayDeque< Object[] > dq = new ArrayDeque<>();
            for( int x = 0; x < 4; x ++ ){
                for( int y = 0; y < 4; y ++ ) {
                    if (trie.childs.containsKey(graph[ x ].charAt( y ))) {
                        visit = new boolean[ 4 ][ 4 ];
                        visit[ x ][ y ] = true;
                        dfs( "" + graph[x].charAt(y), trie.childs.get( graph[ x ].charAt( y )), x, y  );
                        visit[ x ][ y ] = false;
                    }
                }
            }
            //간 주사위는 한번만 갈 수 있다 -> BFS -> DFS

//            while( !dq.isEmpty() ){
//                Object[] now = dq.poll();
//
//                String s = (String) now[ 0 ];
//                Node pos = (Node) now[ 1 ];
//                int x = (int) now[ 2 ];
//                int y = (int) now[ 3 ];
//
////                System.out.println( s + " " + pos + " " + x + " " + y );
//
//                if( s.length() > 8 ) continue;
//
//                if( pos.end ){
//                    if( map.getOrDefault( s , false ) ) continue;
//                    if( found.length() < s.length() ){
//                        found = s;
//
//                    }else if( found.length() == s.length() ){
//                        if( found.compareTo( s ) > 0 ){
//                            found = s;
//                        }
//                    }
//                    score += getScore( s );
//                    cnt++;
//                    map.put( s, true );
//                }
//
//                for( int dir = 0; dir < 8; dir ++ ){
//                    int nx = x + dx[ dir ];
//                    int ny = y + dy[ dir ];
//
//                    if( isRight( nx, ny ) ){
//                        char c = graph[ nx ].charAt( ny );
//                        if( pos.childs.containsKey( c ) ){
//                            dq.add( new Object[]{ s + c, pos.childs.get( c ), nx, ny } );
//                        }
//                    }
//                }
//
//            }
            if( i!= k -1 ){
                bf.readLine();
            }

            if( found.equals("")){
                System.out.println( "0 0");
            }else{
                System.out.println( score + " " + found + " " + cnt );
            }


        }


    }

    private static void dfs(String s, Node node, int x, int y) {
        if( s.length() > 8 ) return;

        if( node.end ){
            if( found.length() < s.length() ){
                found = s;

            }else if( found.length() == s.length() ){
                if( found.compareTo( s ) > 0 ){
                    found = s;
                }
            }

            if( map.getOrDefault( s, true ) ){
                score += getScore( s );
                cnt++;
                map.put( s, false );
            }

        }

        for( int dir = 0; dir < 8; dir ++ ){
            int nx = x + dx[ dir ];
            int ny = y + dy[ dir ];

            if( isRight( nx, ny ) ){
                char c = graph[ nx ].charAt( ny );
                if( node.childs.containsKey( c ) && !visit[ nx ][ ny ]){
                    visit[ nx ][ ny ] = true;
                    dfs( s + c, node.childs.get( c ), nx, ny );
                    visit[ nx ][ ny ] = false;
                }
            }
        }
    }


    static int getScore( String word ){
        int len = word.length();
        if( len > 2 && len < 5 ){
            return 1;
        }else if( len == 5 ){
            return 2;
        }else if( len == 6 ){
            return 3;
        }else if( len == 7 ){
            return 5;
        }else if( len == 8 ){
            return 11;
        }else{
            return 0;
        }
    }

    static boolean isRight( int x, int y ){
        return x >= 0 && x < 4 && y >= 0 && y < 4;
    }

    static class Node{
        Map< Character, Node > childs = new HashMap<>();
        boolean end = false;

        public void insert( String word ){
            Node pos = this;
            for( int i = 0; i < word.length(); i++ ){
                char c = word.charAt( i );
                pos.childs.putIfAbsent( c, new Node() );
                pos = pos.childs.get( c );

                if( i == word.length() - 1){
                    pos.end = true;
                }
            }
        }

        public boolean contains( String word ){
            Node pos = this;
            for( int i = 0; i < word.length(); i ++ ){
                char c = word.charAt( i );
                Node now = pos.childs.get( c );
                if( now == null ) return false;
                pos = now;
            }
            return pos.end;
        }

    }
}
