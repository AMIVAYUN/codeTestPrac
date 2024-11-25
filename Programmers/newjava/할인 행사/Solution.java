import java.util.*;
class Solution {
    /**

     제품 하나씩만 구매 가능

     자신이 원하는 제품 할인 날짜 -> 10일 연속 일치
     10일 연속으로 일치 경우
     */



    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        HashMap<String, Integer> source = new HashMap<>();
        HashMap<String, Integer> target = new HashMap<>();
        for( int i = 0; i < want.length; i ++ ){
            source.put( want[ i ], number[ i ] );
        }

        int n = discount.length;


        for( int i = 0; i < n; i ++ ){
            if( i >= 10 ){
                target.put( discount[ i - 10 ], target.get( discount[ i - 10 ] ) - 1 );
            }
            target.put( discount[ i ],target.getOrDefault( discount[ i ], 0 ) + 1 );

            if( match( source, target ) ){
                answer++;
            }
        }



        return answer;
    }

    boolean match( HashMap< String, Integer > source, HashMap< String, Integer > target ){
        for( String key : source.keySet() ){
            if( !target.containsKey( key ) || !target.get( key ).equals( source.get( key ) ) ) return false;
        }

        return true;
    }

    void print( String[] want, HashMap< String, Integer > target ){
        for( String w : want ){
            System.out.print( w + " " + target.getOrDefault( w, 0 ) + " ");
        }
        System.out.println();
    }
}