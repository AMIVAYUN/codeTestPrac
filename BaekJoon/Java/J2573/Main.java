package J2573;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int m, n, graph[][], dx[] = { -1, 1, 0, 0 }, dy[] = { 0, 0, -1, 1 };

    static ArrayList< Ice > lst = new ArrayList<Ice>();

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = Integer.parseInt( token.nextToken() );
        m = Integer.parseInt( token.nextToken() );
        graph = new int[ n ][ m ];
        for( int i = 0 ; i< n; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            for( int j = 0; j < m; j ++ ){
                graph[ i ][ j ] = Integer.parseInt( token.nextToken() );
                if( graph[ i ][ j ] > 0 ){
                    lst.add( new Ice( i, j ) );
                }
            }
        }
        int time = 0;
        int cnt;
        while( true ){
//            for( int x = 0; x < n; x ++ ){
//                for( int y = 0; y < m; y ++ ){
//                    System.out.print( graph[ x ][ y ] + " " );
//                }
//                System.out.println();
//            }
            cnt = getCnt();
//            System.out.println( cnt );
            if( cnt == 0 || cnt > 1 ){
                break;
            }
            time ++;
            meltDown();

        }


        System.out.println( cnt != 0 ? time : cnt );


    }


    static void meltDown(){
        ArrayList< Ice > nextLst = new ArrayList<>();
        int[][] nextGraph = new int[ n ][ m ];
        for( int i = 0; i < lst.size(); i ++ ){
            Ice ice = lst.get( i );
            int cnt = 0;
            for( int j = 0; j < 4; j ++ ){
                int nx = ice.x + dx[ j ];
                int ny = ice.y + dy[ j ];
                if( nx >= 0 && nx < n && ny >= 0 && ny < m ){
                    if( graph[ nx ][ ny ] == 0 ){
                        cnt ++;
                    }
                }
            }

            if( graph[ ice.x ][ ice.y ] > cnt ){
                nextGraph[ ice.x ][ ice.y ] = graph[ ice.x ][ ice.y ] - cnt;
                nextLst.add( ice );
            }

        }

        graph = nextGraph;
        lst = nextLst;
    }

    static int getCnt(){

        boolean[][] visit = new boolean[ n ][ m ];
        int cnt = 0;
        ArrayDeque< int[] > dq = new ArrayDeque<>();

        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
//                System.out.println( i + " " + j );
                if( graph[ i ][ j ] > 0 && visit[ i ][ j ] == false ){

                    visit[ i ][ j ] = true;
                    cnt++;
                    dq.add( new int[] { i, j } );
                    while( !dq.isEmpty() ){

                        int[] pos = dq.poll();
                        int x = pos[ 0 ];
                        int y = pos[ 1 ];
                        for( int k = 0; k < 4; k ++ ){
                            int nx = x + dx[ k ];
                            int ny = y + dy[ k ];
                            if( nx >= 0 && nx < n && ny >= 0 && ny < m ){
                                if( visit[ nx ][ ny ] == false && graph[ nx ][ ny ] > 0 ){
                                    visit[ nx ][ ny ] = true;
                                    dq.add( new int[]{ nx, ny } );
                                }
                            }
                        }
                    }
                }
            }
        }



//
//        for( int x = 0; x < n; x ++ ){
//            for( int y = 0; y < m; y ++ ){
//                System.out.print( visit[ x ][ y ] + " " );
//            }
//            System.out.println();
//        }

        return cnt;
    }

    private static class Ice {
        int x;
        int y;

        public Ice(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Ice ice = (Ice) o;
            return x == ice.x && y == ice.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
}