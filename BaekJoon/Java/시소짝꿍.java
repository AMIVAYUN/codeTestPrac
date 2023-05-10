import java.util.*;
import java.io.*;
class 시소짝꿍 {


    //WA 4 ~ 11
    public long solution(int[] weights) {
        long answer = 0;


        long[] cases = new long[ 1001 ];

        for( int weight : weights ){
            cases[ weight ] += 1;
        }

        for( int idx = 100; idx < 1001; idx ++ ){
            if( cases[ idx ] > 0 ){
                // 같은 거리
                answer += ( cases[ idx ] * ( cases[ idx ] - 1 ) ) / 2;

                // 2:3
                double res = idx /2 * 3;

                if( idx % 2 == 0 && res < 1001 && res % 1.0 == 0.0 ){
                    int target = Integer.parseInt( String.valueOf( Math.round( res ) ) );
                    if( cases[ target ] > 0 ){

                        answer += cases[ idx ] * cases[ target ];
                    }
                }
                // 2:4
                if( idx * 2 < 1001 && cases[ idx * 2 ] > 0 ){

                    answer += cases[ idx ] * cases[ idx * 2 ];
                }
                // 3:4
                double res2 = idx / 3 * 4;
                if( idx % 3 == 0 && res2 < 1001 && res2 % 1.0 == 0.0 ){
                    int target = Integer.parseInt( String.valueOf( Math.round( res2 ) ) );
                    if( cases[ target ] > 0 ){

                        answer += cases[ idx ] * cases[ target ];
                    }

                }
            }
        }

        return answer;
    }
}
