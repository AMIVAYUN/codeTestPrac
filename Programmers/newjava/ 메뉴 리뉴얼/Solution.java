import java.util.*;
import java.io.*;
/*

    해시맵에 다 넣으면 될 것같다 조합을 구해야 한다.
*/
class Solution {
    HashMap<String, Integer > map = new HashMap<>();
    HashMap<Integer, ArrayList<String> > rev = new HashMap<>();
    HashMap<Integer, Integer> mx = new HashMap<>();
    int[] cmb;
    public String[] solution(String[] orders, int[] course) {
        String[] answer = {};

        for( int c : course ){
            cmb = new int[ c ];
            for( String order : orders ){
                // System.out.println( "c = " + c + " order = " + order );
                getCombination( 0, 0, order, c );
                // System.out.println( "result = " + map );
            }


        }


        for( String key : map.keySet() ){

            ArrayList<String> tmp = rev.getOrDefault( key.length(), new ArrayList<>() );
            tmp.add( key );
            rev.put( key.length(), tmp );

            int val = mx.getOrDefault( key.length(), 0 );

            int Mx = Math.max( val, map.get( key ) );
            mx.put( key.length(), Mx );

        }
        ArrayList<String> result = new ArrayList<>();

        for( int c: course ){
            if( mx.getOrDefault( c, 1 ) == 1 ){
                continue;
            }

            for( String key : rev.get( c ) ){
                if( map.get( key ) == mx.get( c ) ){
                    result.add( key );
                }
            }
        }

        Collections.sort( result );

        return result.toArray( new String[ result.size() ] );
    }

    public void getCombination( int pos, int idx, String o, int c ){

        if( idx == c ){
            String res = "";
            for( int ci : cmb ){
                res += o.charAt( ci );
            }
            char[] arr = res.toCharArray();
            Arrays.sort( arr );
            res = new String( arr );

            map.put( res, map.getOrDefault( res, 0 ) + 1 );
            return;
        }


        for( int i = pos; i < o.length(); i ++ ){
            cmb[ idx ] = i;
            getCombination( i + 1, idx + 1, o, c );
        }
    }
}