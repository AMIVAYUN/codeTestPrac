import java.util.*;
class Solution {
    public int solution(int[][] scores) {
        int answer = 0;

        /**

         1년간의 인사고과에 따른 인센티브 지급

         각 사원마다 근무 태도 점수, 동료 평가 점수 기록됨.

         어떤 사원이 임의 사원보다 두 점수가 모두 낮다면 인센티브를 받지 못한다.

         중요한건 완호가 몇등이냐

         **/

        // int[] wanho = scores[ 0 ];
        // 받지 못하는 경우의 등수를 캐치하지 못한다.
//         PriorityQueue<int[]>pq = new PriorityQueue<int[]>( ( a, b ) -> {
//             if( a[ 0 ] + a[ 1 ] == b[ 0 ] + b[ 1 ] ){
//                 return Integer.compare( a[ 0 ], b[ 0 ] );
//             }

//             return Integer.compare( a[ 0 ] + a[ 1 ], b[ 0 ] + b[ 1 ] );
//         });

//         for( int i = 1; i < scores.length; i ++ ){
//             int[] p = scores[ i ];
//             pq.add( p );
//         }
//         int wanhoSum = wanho[ 0 ] + wanho[ 1 ];
//         while( !pq.isEmpty() ){
//             int[] now = pq.poll();
//             int sum = now[ 0 ] + now[ 1 ];
//             if( now[ 0 ] > wanho[ 0 ] && now[ 1 ] > wanho[ 1 ] ){
//                 return -1;
//             }
//             if( sum == wanhoSum ) return answer;

//             answer++;
//         }
        /**

         9   9
         9   7
         8   9


         **/

        /**

         이 로직은 나보다 한참 위에 있는 친구들의 기준을 넘지 못한다.

         **/
//         int[] wanho = scores[ 0 ];
//         int wanhoSum = wanho[ 0 ] + wanho[ 1 ];
//         Arrays.sort( scores, ( a, b ) -> {
//             if( a[ 0 ] == b[ 0 ] ){
//                 return Integer.compare( b[ 1 ], a[ 1 ] );
//             }
//             return Integer.compare( b[ 0 ], a[ 0 ] );
//         });

//         for( int i = 0; i < scores.length; i ++ ){
//             int[] sc = scores[ i ];
//             int sum = sc[ 0 ] + sc[ 1 ];

//             if( isLow( wanho, sc ) ){
//                 return -1;
//             }

//             if( sum <= wanhoSum ){
//                 continue;
//             }
//             if( i > 0 ){
//                 if( isLow( sc, scores[ i - 1 ] ) ){
//                     continue;
//                 }
//             }

//             if( sum > wanhoSum ) answer++;


//         }

//         return answer;
//     }



        int wanhoSum = scores[ 0 ][ 0 ] + scores[ 0 ][ 1 ];
        int[] wanho = scores[ 0 ];
        Arrays.sort( scores, ( a, b ) -> {
            if( a[ 0 ] == b[ 0 ] ){
                return Integer.compare( a[ 1 ], b[ 1 ] );
            }
            return Integer.compare( b[ 0 ], a[ 0 ] );
        });
        int mx = 0;

        for( int i = 0; i < scores.length; i ++ ){
            int[] sc = scores[ i ];
            int sum = sc[ 0 ] + sc[ 1 ];
            // System.out.println( Arrays.toString( sc ) + ", " + mx );
            if( mx > sc[ 1 ] ){
                if( wanho[ 1 ] == sc[ 1 ] && wanho[ 0 ] == sc[ 0 ] ) return -1;
            }else{
                mx = sc[ 1 ];
                if( wanhoSum < sum ){
                    // System.out.println( Arrays.toString( sc ) );
                    answer++;
                }
            }




        }

        return answer + 1;
//         int[] wanho = scores[ 0 ];
//         int wanhoSum = wanho[ 0 ] + wanho[ 1 ];
//         Arrays.sort( scores, ( a, b ) -> {
//             if( a[ 0 ] == b[ 0 ] ){
//                 return Integer.compare( a[ 1 ], b[ 1 ] );
//             }
//             return Integer.compare( b[ 0 ], a[ 0 ] );
//         });

//         for( int i = 0; i < scores.length; i ++ ){
//             int[] sc = scores[ i ];
//             int sum = sc[ 0 ] + sc[ 1 ];

//             if( isLow( wanho, sc ) ){
//                 return -1;
//             }


//             if( i > 0 && i < scores.length - 1 ){
//                 if( isLow( sc, scores[ i - 1 ] ) || isLow( sc, scores[ i + 1 ] ) ){
//                     continue;
//                 }
//             }else if( i == 0 ){
//                 if( isLow( sc, scores[ i + 1 ] ) ){
//                     continue;
//                 }
//             }else if( i == scores.length ){
//                 if( isLow( sc, scores[ i - 1 ] ) ){
//                     continue;
//                 }
//             }

//             if( sum > wanhoSum ) answer++;


//         }

//         return answer;

//     }
    }
    public boolean isLow( int[] a, int[] b ){
        return a[ 0 ] < b[ 0 ] && a[ 1 ] < b[ 1 ];
    }
}