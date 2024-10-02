import java.util.*;
import java.io.*;
class Solution {
    public int[] solution(String s) {
        int[] answer = {};
        s = s.substring( 1, s.length() - 1 );
        String[] sp = s.split("},");

        sp[ sp.length - 1 ] = sp[ sp.length - 1 ].substring( 1, sp[ sp.length - 1 ].length() - 1 );

        for( int i = 0; i < sp.length - 1; i ++ ){
            sp[ i ] = sp[ i ].substring( 1, sp[ i ].length() );
        }
        Arrays.sort( sp, ( s1, s2 ) -> Integer.compare( s1.length(), s2.length() ) );

        ArrayList< Integer > lst = new ArrayList<>();
        HashMap< Integer, Boolean > map = new HashMap<>();

        lst.add( Integer.parseInt( sp[ 0 ] ) );
        map.put( Integer.parseInt( sp[ 0 ] ), true );

        for( int i = 1; i < sp.length; i ++ ){
            String[] kp = sp[ i ].split(",");
            // System.out.println( Arrays.toString( kp ) );
            for( String k : kp ){
                int ki = Integer.parseInt( k );
                if( map.getOrDefault( ki, false ) ){
                    continue;
                }

                lst.add( ki );
                map.put( ki, true );
            }
        }

        answer = new int[ lst.size() ];

        for( int i = 0; i < lst.size(); i ++ ){
            answer[ i ] = lst.get( i );
        }
        return answer;
    }
}