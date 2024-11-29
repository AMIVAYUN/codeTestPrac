class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = { 0, 0 };
        int lt = 0; int rt = 0;
        boolean flag = false;
        if( sequence[ lt ] == k ){ return answer; }
        int sum = sequence[ lt ], n = sequence.length;
        while( rt < n ){

            if( sum > k ){
                sum -= sequence[ lt ];
                lt++;
                if( sum < 0 ){
                    sum = sequence[ lt ];
                    rt = lt;
                }
                continue;
            }else{
                if( sum == k ){

                    if( flag ){
                        if( answer[ 1 ] - answer[ 0 ] > rt - lt ){
                            answer[ 0 ] = lt;
                            answer[ 1 ] = rt;
                        }
                    }else{
                        answer[ 0 ] = lt;
                        answer[ 1 ] = rt;
                    }
                    flag = true;
                }

                rt++;
                if( rt >= n ){
                    break;
                }
                sum += sequence[ rt ];
            }
        }
        return answer;
    }
}