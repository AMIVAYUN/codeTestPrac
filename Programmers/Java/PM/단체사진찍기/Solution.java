package PM.단체사진찍기;

import java.util.*;
import java.io.*;
class Solution {
    /*
    a ~ b = 0
    a ~ b 관계 간격

    8! = 40320 즉 완탐 가능

    조건이 100개 모든 조건 다 도는데 40320 * 100 4백만

    조건 전처리를 먼저한다. -> 여기서 0이면 아웃
     1. 6 거리가 되는 관계가 두개 이상 바로 0
     2. 이미 거리가 정해졌는데 모순된 거리가 나왔을 때 바로 0


    */

    int[] arr = new int[ 8 ];

    int[][] dists;
    Map<Character, Integer> mapper = new HashMap<>();
    Map<Integer, Character> reverseMapper = new HashMap<>();
    {
        mapper.put('A', 0);
        mapper.put('C', 1);
        mapper.put('F',2);
        mapper.put('J',3);
        mapper.put('M',4);
        mapper.put('N',5);
        mapper.put('R',6);
        mapper.put('T',7);


        for( int i = 0; i < 8; i ++ ){
            arr[ i ] = i;
        }
    }

    public int solution(int n, String[] data) {
        int answer = 0;

        if( isMatch( n, data ) ){
            answer ++;
        }

        // getNextPerm();
        int cnt = 0;
        // System.out.println( Arrays.toString( arr ) );
        // System.out.println( Arrays.toString( arr ) );
        while( getNextPerm() ){

            if( isMatch( n, data ) ) answer++;
            // cnt++;
        }
        return answer;
    }

    public boolean getNextPerm() {
        // System.out.println( Arrays.toString( arr ) );
        //1. 꼭대기 찾기
        int idx = arr.length - 1;

        while( idx > 0 && arr[ idx ] <= arr[ idx - 1 ] ) idx --;

        if( idx == 0 ) {
            return false;
        }

        int j = arr.length -1;

        while( arr[ j ] <= arr[ idx - 1 ] ) j --;

        swap( idx - 1, j );


        int start = idx;
        int end = arr.length - 1;

        while( start <= end ) {
            swap( start, end );
            start ++;
            end --;
        }

        return true;


    }

    void swap( int x, int y ) {
        int temp = arr[ x ];
        arr[ x ] = arr[ y ];
        arr[ y ] = temp;
    }

    public boolean isMatch( int n, String[] condition ){
        HashMap<Integer, Integer > pos = new HashMap<>();

        for( int i = 0; i < 8; i ++ ){
            pos.put(  arr[ i ], i );
        }


        for( int i = 0; i < n; i++ ){
            String cond = condition[ i ];

            int start = mapper.get( cond.charAt( 0 ) );
            int end = mapper.get( cond.charAt( 2 ) );
            char relation = cond.charAt( 3 );
            int dist = cond.charAt( 4 ) - '0';


            int startPos = pos.get( start );
            int endPos = pos.get( end );

            // System.out.println( startPos + " " + endPos + " " + relation);

            int betweenDist = Math.abs( startPos - endPos ) - 1;


            //초과
            // System.out.println( betweenDist + " " + dist );
            if( relation == '>' ){
                if( dist >= betweenDist ) return false;
            }else if( relation == '<'){
                if( dist <= betweenDist ) return false;
            }else{
                if( dist != betweenDist ) return false;
            }



        }

        return true;

    }
}