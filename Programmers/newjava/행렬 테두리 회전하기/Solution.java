class Solution {
    int n, m, graph[][];
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[ queries.length ];
        n = rows;
        m = columns;
        int val = 1;
        graph = new int[ n ][ m ];
        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
                graph[ i ][ j ] = val++;
            }
        }
        int idx = 0;
        for( int[] query: queries ){
            answer[ idx ++ ] = rotate( query[ 0 ] - 1, query[ 1 ] - 1, query[ 2 ] - 1, query[ 3 ] - 1 );

            // print();
            // break;
        }

        return answer;
    }
    public void print(){
        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
                System.out.print( graph[ i ][ j ] + " " );
            }
            System.out.println();
        }
    }
    int[] dx = { 0, 1, 0, -1 };
    int[] dy = { 1, 0, -1, 0 };
    public int rotate( int x1, int y1, int x2, int y2 ){
        int val = graph[ x1 ][ y1 ];

        int mn = val;

        int cnt = x2 - x1 + y2 - y1;
        cnt *= 2;
        int ro = y2 - y1;
        int co = x2 - x1;

        int x = x1;
        int y = y1;
        int dir = 0;
        while( cnt > 0 ){
            int rem = dir % 2 == 0 ? ro : co;
            // System.out.println( rem + " " + x + ", " + y );
            while( rem > 0 ){
                x = x + dx[ dir ];
                y = y + dy[ dir ];
                int tmp = graph[ x ][ y ];
                graph[ x ][ y ] = val;
                val = tmp;
                mn = Math.min( mn, val );
                rem--;
                cnt--;
            }

            // System.out.println( rem + " " + x + ", " + y + ", cnt = " + cnt );
            dir = ( dir + 1 ) % 4;

        }


        return mn;
    }
}