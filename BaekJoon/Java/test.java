public class test {
    public static void main( String[] args ){
        double t = 0.1;
        int[] tc ={100,180,360,100,270};
        solution( tc );
    }


    public static long solution(int[] weights) {
        long answer = 0;


        int[] cases = new int[ 1001 ];

        for( int weight : weights ){
            cases[ weight ] += 1;
        }

        for( int idx = 1; idx < 1001; idx ++ ){
            if( cases[ idx ] > 0 ){
                // 같은 거리
                answer += cases[ idx ] - 1;

                // 2:3
                double res = idx * 1.5;

                if( res < 1001 && res % 1 == 0 ){
                    int target = Integer.parseInt( String.valueOf( Math.round( res ) ) );
                    if( cases[ target ] > 0 ){
                        answer += cases[ idx ] * cases[ target ];
                    }
                }
            }
            // 2:4
            else if( cases[ idx * 2 ] > 0 ){
                answer += cases[ idx ] * cases[ idx * 2 ];
            }
            // 3:4
            double res = idx / 3 * 4;
            if( res < 1001 && res % 1 == 0 ){
                int target = Integer.parseInt( String.valueOf( Math.round( res ) ) );
                if( cases[ target ] > 0 ){
                    answer += cases[ idx ] * cases[ target ];
                }

            }

        }

        return answer;
    }
}
