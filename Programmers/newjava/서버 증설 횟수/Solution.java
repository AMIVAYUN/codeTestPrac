import java.util.*;
class Solution {
    /**
     * 같은 시간대에 게임 이용 m명 늘 때마다 1대가 추가로 필요.

     어느 시간대 m명 미만이면 서버 증설 필요 x
     어느 시간대 이용자가 n * m 명 이상 (n + 1) * m 명 미만 -> 최소 n대의 증설된 서버가 운영 중이어야 한다.
     한번 증설 -> k시간 동안 운영 후 반납
     k 5 -> 10 ~ 15
     모든 게임 이용자가 이용하기 위해 최소 몇번 증설해야 하는지 알고 싶다.

     */
    public int solution(int[] players, int m, int k) {
        int answer = 0;

        PriorityQueue< Integer > pq = new PriorityQueue<>( (e1, e2 ) -> {return Integer.compare( e1, e2 ); } );
        for( int i = 0; i < players.length; i ++ ){
            while( !pq.isEmpty() && pq.peek()<= i ){
                pq.poll();
            }

            int player = players[ i ];

            int necessary = player / m;
            int need = necessary - pq.size();
            if( need < 1 ){
                continue;
            }else{
                for( int j = 0; j < need; j ++ ){
                    pq.add( i + k );
                    answer++;
                }
            }
        }

        return answer;
    }
}