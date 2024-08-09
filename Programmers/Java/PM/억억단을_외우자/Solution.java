package PM.억억단을_외우자;

import java.util.*;
class Solution {
    /**
     n**2 으로 가면 터진다.
     k번째 수를 풀었던 것 처럼 접근해볼까?

     500만 * 1억은 좀 빡셀 것 같다.

     이분탐색으로 접근.

     또한 memo를 해두어 기존 값들을 저장하고 있을 시 재활용 하자.

     어느 행까지 봐야하는가? 나의 행까지 봐야한다.

     확률적으로 수가 클 수록 더 많이 나올 확률이 커진다. > 탐색하는 행과 약수가 늘기 때문.

     근데 이런식으로 접근한다면 결국 어떤 수는 나의 depth까지만 보면 되기에, 500만 * 500만이다.

     그래도 천억이네

     근데 생각해보니 그냥 약수의 개수를 구하면 된다. 이러면 굳이 매회 반복할 필요가 있는가? 없다.

     memo[ i ] 는 i가 가진 약수의 개수.

     dp 테이블 2차원은 [ i ][ j ]  s가 i고 e가 j일 때 가장 많이 출현한 약수의  개수
     dp[ i ] = Math.max( dp[ i ][ j - 1 ]의 약수의 개수, memo[ i ]의 수 );
     ( 단 if( dp[ i ][ j - 1 ]약수의 개수 == memo[ i ]의 수 ) => dp[ i ][ j - 1 ]의 수 );

     class로 가니깐 메모리가 초과됬다.

     1. new를 지운다... 실패
     2. 배열로 구현한다. -> 반례 등장 및 메모리 초과.
     3. 그러면 2차원으로 수만 구하고 범위 내에서 해당 수를 n번 돌아 매번 찾자. -> 좋은데?
     -> 7번까진 뚫었다.

     4. 그럼 2차원도 버리자 그냥 정렬을 해버리자

     결론 // 요즘하도 dp만 풀다보니 점화식을 찾으며 문제를 어렵게 보는 버릇이 생긴 것 같다. 고치자.

     */

    int[] memo;
    // Number[] area,dp[];
    int[][] dp;
    public int[] solution(int e, int[] starts) {
        int[] answer = new int[ starts.length ];
        memo = new int[ e + 1 ];

        //이건 돌려도 시간 초과 안난다 진행.
        for( int i = 1; i < e + 1; i ++ ){
            for( int j = i; j < e + 1; j += i ){
                memo[ j ] += 1;
            }
        }
//         // dp = new Number[ e + 1 ][ e + 1 ];
//         dp = new int[ e + 1 ][ e + 1 ];
//         // for( int i = 0; i < e + 1; i ++ ){
//         //     for( int j = 0; j < e + 1; j ++ ){
//         //         dp[ i ][ j ] = new Number( j );
//         //     }
//         // }
//         // area = new Number[ e + 1 ];
//         for( int i = 1; i < e + 1; i ++ ){
//             // dp[ i ][ i ].divs = memo[ i ];
//             // area[ i ] = new Number( i, memo[ i ] );
//             dp[ i ][ i ] = memo[ i ];
//         }
//         // System.out.println( Arrays.toString( memo ) );

//         // 1 1 -> 2 2 -> ... e e ->
//         for( int i = 1; i < e + 1; i ++ ){

//             for( int j = 1; j < e - i + 1; j ++ ){
//                 int start = j;
//                 int end = j + i;


// //                 if( dp[ start ][ end - 1 ].divs > memo[ end ] ){
// //                     dp[ start ][ end ] = dp[ start ][ end - 1 ];

// //                 }else if( dp[ start ][ end - 1 ].divs == memo[ end ] ){
// //                     dp[ start ][ end ] = dp[ start ][ end - 1 ].number < end ? dp[ start ][ end - 1]  : area[ end ];
// //                 }else{
// //                     dp[ start ][ end ] = area[ end ];
// //                 }
//                 dp[ start ][ end ] = Math.max( dp[ start ][ end - 1 ], memo[ end ] );

//                 // System.out.println( "start, end = [ "+start +","+end+" ]" +  "value = [" + dp[ start ][ end ].toString() + "]" );

//             }
//         }

        Number[] nums = new Number[ e + 1 ];

        for( int i =0; i < e + 1; i ++ ){
            nums[ i ] = new Number( i, memo[ i ] );
        }

        Arrays.sort( nums, ( n1, n2 ) -> {
            if( n1.divs > n2.divs ){
                return -1;
            }else if( n1.divs == n2.divs ){
                return Integer.compare( n1.number, n2.number );
            }else{
                return 1;
            }
        });


        int idx = 0;
        for( int start: starts ){
            // answer[ idx++ ] = findValue( start, e, dp[ start ][ e ] );
            for( int i = 0; i < e + 1; i ++ ){
                Number num = nums[ i ];

                if( num.number <= e && num.number >= start ){
                    answer[ idx++ ] = num.number;
                    break;
                }

            }
        }
        //.  0. 1. 2. 3. 4. 5. 6. 7. 8
        //	[0, 1, 2, 2, 3, 2, 4, 2, 4]
        return answer;
    }
    private int findValue( int s, int e, int val ){
        for( int i = s; i < e + 1; i ++ ){
            if( memo[ i ] == val ) return i;
        }
        return -1;
    }
    class Number{
        int number;
        int divs;

        public Number( int number, int divs ){
            this.number = number;
            this.divs = divs;
        }

        public Number( int number ){
            this.number = number;
            this.divs = 0;
        }

        @Override
        public String toString(){
            return "number = " + number + " divs = " + divs;
        }
    }
}