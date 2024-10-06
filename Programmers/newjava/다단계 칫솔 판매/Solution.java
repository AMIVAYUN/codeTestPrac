import java.util.*;
class Solution {
    //유니온 파인드 그런데 압축을 곁들이지 않은
    private int parents[], n;
    private HashMap<String,Integer> map = new HashMap<>();
    private int[] answer;
    private String[] enroll;
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {

        n = enroll.length + 1;
        parents = new int[ n ];
        this.enroll = enroll;
        answer= new int[ n - 1 ];

        for( int i = 0; i < n; i ++ ){
            if( i > 0 ) map.put( enroll[ i - 1 ], i );
            parents[ i ] = i;
        }
        // System.out.println( map );
        parents[ 0 ] = -1;
        for( int i = 0; i < n - 1; i ++ ){
            String name = referral[ i ];
            int pidx;
            if( name.equals( "-" ) ){
                pidx = 0;
            }else{
                pidx = map.get( name );
            }
            parents[ map.get( enroll[ i ] ) ] = pidx;
        }
        // System.out.println( Arrays.toString( parents ) );
        for( int i = 0; i < seller.length; i ++ ){
            sell( seller[ i ], amount[ i ] );
            // System.out.println( "seller " + seller[ i ]  + " ,amount = " + (amount[ i ] * 100) + " result = " + Arrays.toString( answer ) );
        }


        return answer;
    }

    private void sell( String name, int amount ){
        int idx = map.get( name );
        amount = amount * 100;
        while( amount > 0 && idx > 0 ){
            // System.out.println( enroll[ idx- 1 ] + " , " + amount );
            int unit = amount / 10;
            answer[ idx - 1 ] += unit > 0 ? amount - unit : amount;

            amount = unit;
            idx = parents[ idx ];
        }
    }
}