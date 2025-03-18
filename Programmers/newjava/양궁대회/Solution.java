import java.util.*;
class Solution {
    /**

     * 어피치가 n발 다쏘고 라이언 n발
     * k점을 어피치가 a발 라이언이  b발 -> 이긴쪽이 k점 가져감.
     * a = b 어피치가 k점
     * a = b = 0 아무도 x
     * 가장 큰 점수 차이로 이기기 위해서 n발을 어떤 과녁 점수에 맞혀야 하는지 구하려고 한다.

     depth Mx 10;
     중복 조합
     nhr = n+r-1Cr

     19C10 92378



     */
    int n;
    int diff = 0;
    int apeech = 0;
    int[] answer, info;
    ArrayList< int[] > lst = new ArrayList<>();
    public int[] solution(int n, int[] info) {
        this.answer = new int[ 11 ];
        this.info = info;
        Arrays.fill( this.answer, 11 );
        this.n = n;
        Combination( 0, new int[ 11 ], n );
        return answer[ 0 ] == 11 ? new int[]{ -1 } : answer;

    }

    public void Combination( int depth, int[] arr, int remain ){

        if( remain == 0 || depth == 10 ){

            arr[ depth ] = remain;
            int lion = 0, apeech = 0;
            for( int i = 0; i < 11; i ++ ){

                if( arr[ i ] == 0 && info[ i ] == 0 ) continue;
                if( arr[ i ] > info[ i ] ){
                    lion += 10 - i;
                }else{
                    apeech += 10 - i;
                }

            }
            if( lion > apeech ){
                if( lion - apeech > diff ){
                    diff = lion - apeech;
                    for( int j = 0; j < 11; j ++ ){
                        answer[ j ] = arr[ j ];
                    }
                }else if( lion - apeech == diff ){
                    // System.out.println( Arrays.toString( arr ) + " " + Arrays.toString( answer ) );
                    boolean flag = false;
                    for( int i = 10; i >= 0; i -- ){
                        if( arr[ i ] == 0 && answer[ i ] == 0 ){
                            continue;
                        }else{
                            if( answer[ i ] == arr[ i ] ){
                                continue;
                            }else{
                                if( answer[ i ] > arr[ i ] ){
                                    flag = false;
                                    break;
                                }else{
                                    flag = true;
                                    break;
                                }
                            }
                        }
                    }

                    if( flag ){

                        for( int j = 0; j < 11; j ++ ){
                            answer[ j ] = arr[ j ];
                        }
                    }
                }
            }
            arr[depth] = 0;
            return;
        }



        int next = info[ depth ] + 1;
        if( remain >= next ){
            arr[ depth ] = next;
            Combination( depth + 1, arr, remain - next );
            arr[ depth ] = 0;
        }
        for( int i = 0; i <= info[ depth ] && i <= remain; i ++ ){
            arr[ depth ] = i;
            Combination( depth + 1, arr, remain - i );
            arr[ depth ] = 0;
        }

    }

}