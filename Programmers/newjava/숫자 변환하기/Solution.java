import java.util.*;
class Solution {
    int mn = Integer.MAX_VALUE;
    public int solution(int x, int y, int n) {
        int answer = 0;
        // if( x == y ) return 0;
        // find( x, y, n, 0 );

        ArrayDeque< int[] > dq = new ArrayDeque<>();
        dq.add( new int[]{ y, 0 } );

        while( !dq.isEmpty() ){
            int[] now = dq.poll();
            int pos = now[ 0 ];
            int cnt = now[ 1 ];

            if( cnt > mn ) continue;

            if( pos == x ){
                mn = cnt;
                continue;
            }

            if( pos % 3 == 0 ){
                dq.add( new int[]{ pos / 3, cnt + 1 });
            }
            if( pos % 2 == 0 ){
                dq.add( new int[]{ pos / 2, cnt + 1 });
            }
            if( pos - n >= x ){
                dq.add( new int[]{ pos - n, cnt + 1 });
            }
        }

        return mn != Integer.MAX_VALUE ? mn : -1;
    }


    public void find( int x, int y, int n, int k ){
        if( k > mn ){
            return;
        }

        if( x == y ){
            mn = k;
            return;
        }

        if( y % 3 == 0 ){
            find( x, y / 3, n, k + 1 );
        }
        if( y % 2 == 0 ){
            find( x, y / 2, n, k + 1 );
        }

        if( y - n >= x ){
            find( x, y - n, n, k + 1 );
        }


    }
}