import java.util.*;
class Solution {
    public int solution(int coin, int[] cards) {
        int answer = 1;
        int n = cards.length;
        //갈 수 있는 라운드 수 : cards.length / 3 + 1;
        HashMap< Integer, Boolean > map = new HashMap<>();
        boolean[] visit = new boolean [ n + 1 ];
        boolean[] used = new boolean [ n + 1 ];
        for( int i = 0; i < debug item 154n / 3; i ++ ) {
            map.put( cards[ i ], true );
            visit[ cards[ i ] ] = true;
        }


            outer: for( ; answer <= n / 3 + 1; answer ++ ){
                // System.out.println( "round == " + answer + " coin = " + coin );
                int cardMx = n / 3 + ( 2 * ( answer ) );
                if( cardMx - 1 < n && cardMx - 2 < n ) {
                    visit[ cards[ cardMx - 1 ] ] = true;
                    visit[ cards[ cardMx - 2 ] ] = true;
                    // System.out.println( "visit check " + cards[ ( cardMx - 1 ) ]+ " , " + cards[ ( cardMx - 2 ) ] );
                }


                for( int card: map.keySet() ) {
                if( map.containsKey( n + 1 - card ) && !used[ n + 1 - card ] ){
                    used[ n + 1 - card ] = true;
                    used[ card ] = true;
                    map.remove( n + 1 - card );
                    map.remove( card );
                    // System.out.println( "not used! " + card + " " + ( n + 1 - card ) );

                    continue outer;
                }
            }


            //1개

            for( int card: map.keySet() ) {
                if( visit[ n + 1 - card ] && !used[ n + 1 - card ] ){
                    if( coin - 1 < 0 ) break outer;
                    coin--;
                    used[ n + 1 - card ] = true;
                    used[ card ] = true;
                    map.remove( card );

                    continue outer;
                }
            }
            //2개
            if( coin < 2 ) break;
            for (int i = 0; i < Math.min(cardMx, n); i++){

                int ci = cards[ i ];
                if( used[ ci ] ) continue;
                if( visit[ n + 1 - ci ] && !used[ n + 1 - ci ] ){
                    coin -= 2;
                    used[ ci ] = true;
                    used[ n + 1 - ci ] = true;
                    continue outer;
                }
            }
            break;

        }

        return answer == n / 3 + 2 ? n / 3 + 1 : answer;
    }
}