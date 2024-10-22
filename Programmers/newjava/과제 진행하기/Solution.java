import java.util.*;
class Solution {
    public String[] solution(String[][] plans) {
        String[] answer = {};
        ArrayList<String> ans = new ArrayList<>();
        /**

         과제는 시작하기로 한 시각이 되면 시작
         새로운 과제 시작 시각이 되면 기존 진행 중이던 과제에 따라 진행중이던 과제를 멈추고 새로운 과제 시작
         진행중이던 과제 끝내면 잠시 멈춘 과제 이어서 진행

         */
        Arrays.sort( plans, ( e1, e2 ) -> Integer.compare( getTime( e1[ 1 ]), getTime( e2[ 1 ] ) ) );
        int n = plans.length;
        ArrayDeque< String[] > dq = new ArrayDeque<>();
        for( int i = 0; i < n; i ++ ){
            if( i == n - 1 ){
                dq.add( new String[]{ plans[ i ][ 0 ], plans[ i ][ 2 ] } );
                continue;
            }
            String[] next = plans[ i + 1 ];
            String[] now = plans[ i ];

            int startTime = getTime( plans[ i ][ 1 ] );
            int duration = Integer.parseInt( plans[ i ][ 2 ] );
            int nextStartTime = getTime( next[ 1 ] );
            if( startTime + duration <= nextStartTime ){
                ans.add( now[ 0 ] );
                int remain = nextStartTime - startTime - duration;
                while( remain > 0 && !dq.isEmpty() ){
                    String[] elem = dq.pollLast();
                    String ename = elem[ 0 ];
                    int eremain = Integer.parseInt( elem[ 1 ] );

                    if( remain >= eremain ){
                        remain -= eremain;
                        ans.add( ename );
                    }else{

                        dq.add( new String[]{ ename, ( eremain - remain )+ ""} );
                        remain = 0;
                    }
                }
            }else{
                dq.add( new String[]{ plans[ i ][ 0 ], (startTime + duration - nextStartTime) + "" } );
            }

        }

        while( !dq.isEmpty() ){
            String[] now = dq.pollLast();
            ans.add( now[ 0 ] );
        }

        return ans.toArray( new String[ ans.size() ]);
    }

    public int getTime( String time ){
        String[] tm = time.split(":");
        return Integer.parseInt( tm[ 0 ] ) * 60 + Integer.parseInt( tm[ 1 ] );
    }
}