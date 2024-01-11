package J4991;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    static int n, m, Mn, graph[][], dirties, sx,sy, dx[] = { -1, 1, 0, 0 }, dy[] = { 0, 0, -1, 1 };

    static ArrayList<Dirty> lst;
    static int[][][] visit;

    static boolean[] checked;

    public static void main(String[] args) throws IOException {

        outer: while( true ){
            token = new StringTokenizer( bf.readLine() );
            m = Integer.parseInt( token.nextToken() );
            n = Integer.parseInt( token.nextToken() );
            dirties = 0;
            lst = new ArrayList<>();
            graph = new int[ n ][ m ];
            Mn = Integer.MAX_VALUE;
            if( m == 0 && n == 0 ) break;
            visit = new int[ n ][ m ][ 4 ];

            for( int x = 0; x < n; x ++ ){
                String row = bf.readLine();
                for( int y = 0; y < m; y ++ ){
                    Arrays.fill( visit[ x ][ y ], Integer.MAX_VALUE );
                    if( row.charAt( y ) == '.'){
                        graph[ x ][ y ] = 0;
                    }else if( row.charAt( y ) == 'o' ){
                        sx = x;
                        sy = y;
                        graph[ x ][ y ] = 0;
                        Arrays.fill( visit[ x ][ y ], 0 );
                    }else if( row.charAt( y ) == '*' ){
                        graph[ x ][ y ] = -1;
                        dirties++;
                        lst.add( new Dirty( x, y ) );
                    }else{
                        graph[ x ][ y ] = 1;
                    }
                }
            }

            checked = new boolean[ lst.size() ];
            for( Dirty d : lst ){
                bfs( d.x, d.y );
            }

//            for( Dirty d : lst ){
//                for( int[] row : d.dists ){
//                    System.out.println( Arrays.toString( row ) );
//                }
//            }

            for( Dirty d : lst ){
                for( Dirty next: lst ){
                    if( d.dists[ next.x ][ next.y ] == Integer.MAX_VALUE ){
                        sb.append( -1 ); sb.append("\n");
                        continue outer;

                    }
                }
            }

            getPermutations( 0, sx, sy, 0 );

            String result = (Mn != Integer.MAX_VALUE ? Mn : -1)  + "\n";
            sb.append( result );
        }

        System.out.println(sb);

    }

    private static void getPermutations(int depth, int x, int y, int cnt ) {
//        System.out.println( depth + cnt );
//        System.out.println( depth + " " + x + " " + y + " " + cnt );
        if( depth == lst.size() ){
            Mn = Math.min( Mn, cnt );
            return;
        }

        if( cnt > Mn ){
            return;
        }

        for( int i = 0; i < lst.size(); i ++ ){
            if( !checked[ i ] ){
                Dirty next = lst.get( i );
                int cost = cnt + next.dists[ x ][ y ];
                if( cost < Mn ){

                    checked[ i ] = true;
                    getPermutations( depth + 1, next.x, next.y, cost );
                    checked[ i ] = false;

                }
            }
        }
    }


    static void bfs( int sx, int sy ){
        ArrayDeque< Pos > dq = new ArrayDeque<Pos>();
        int[][] visit = new int[ n ][ m ];

        for( int i = 0; i < n; i ++ ){
            Arrays.fill( visit[ i ], Integer.MAX_VALUE );
        }
        visit[ sx ][ sy ] = 0;

        dq.add( new Pos( sx, sy, 0 ) );

        while( !dq.isEmpty() ){
            Pos now = dq.poll();

            for( int i = 0; i < 4; i ++ ){
                int nx = now.x + dx[ i ];
                int ny = now.y + dy[ i ];

                if( nx >= 0 && nx < n && ny >= 0 && ny < m ){
                    if( visit[ nx ][ ny ] > now.cnt + 1 && graph[ nx ][ ny ] != 1 ){
                        visit[ nx ][ ny ] = now.cnt + 1;
                        dq.add( new Pos( nx, ny, now.cnt + 1 ) );
                    }
                }

            }
            Dirty target = lst.get( lst.indexOf(  new Dirty( sx, sy ) ) );
            target.setDists( visit );


        }



    }

    static class Pos{
        int x, y, cnt;

        public Pos(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }

    static class Dirty{
        int x, y;
        int[][] dists;
        public Dirty(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int[][] getDists() {
            return dists;
        }

        public void setDists(int[][] dists) {
            this.dists = dists;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Dirty dirty = (Dirty) o;
            return x == dirty.x && y == dirty.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }

        @Override
        public String toString() {
            return "Dirty{" +
                    "x=" + x +
                    ", y=" + y +
                    ", dists=" + Arrays.toString(dists) +
                    '}';
        }
    }

    private static void dfs( int cnt, int x, int y ) {
        if (cnt > Mn) {
            return;
        }

        if (dirties == 0) {
            Mn = Math.min(Mn, cnt);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {

                if (visit[nx][ny][i] > cnt) {
                    if (graph[nx][ny] != 1) {
                        if (graph[nx][ny] == -1) {
                            dirties--;
                            visit[nx][ny][i] = cnt;
                            dfs(cnt + 1, nx, ny);
                            dirties++;
                        } else {
                            visit[nx][ny][i] = cnt;
                            dfs(cnt + 1, nx, ny);
                        }
                    }
                }
            }
        }
    }
    // #SOL1 예제 2번 반례
    private static void dfssol1( int cnt, int x, int y ) {
        if( cnt > Mn ){
            return;
        }

        if( dirties == 0 ){
            Mn = Math.min( Mn, cnt );
            return;
        }

        for( int i = 0; i < 4; i ++ ){
            int nx = x + dx[ i ];
            int ny = y + dy[ i ];
            if( nx >= 0 && nx < n && ny >= 0 && ny < m ){

                if( visit[ nx ][ ny ][ i ] > cnt ){
                    if( graph[ nx ][ ny ] != 1 ){
                        if( graph[ nx ][ ny ] == -1 ){
                            dirties--;
                            visit[ nx ][ ny ][ i ] = cnt;
                            dfs( cnt + 1, nx, ny );
                            dirties++;
                        }else{
                            visit[ nx ][ ny ][ i ] = cnt;
                            dfs( cnt + 1, nx, ny );
                        }
                    }
                }
            }
        }
    }
}
