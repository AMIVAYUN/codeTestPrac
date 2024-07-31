package PM.디스크_컨트롤러;

import java.util.*;
import java.io.*;
class Solution {
    /**
     작업 길이가 적은 순서대로
     */
    int time = 0;
    public int solution(int[][] jobs) {
        int answer = 0;
        //기존 pq 너무 어렵게 생각했나?
//         PriorityQueue<Task> pq = new PriorityQueue<>( ( t1, t2 ) -> {

//             int totalt1, totalt2;

//             if( time > t1.requestTime ){

//                 totalt1 = ( time - t1.requestTime ) + t1.remainTime;

//             }else{
//                 totalt1 = t1.remainTime;

//             }

//             if( time > t2.requestTime ){
//                 totalt2 = ( time - t2.requestTime ) + t2.remainTime;

//             }else{
//                 totalt2 = t2.remainTime;

//             }
//             // return Integer.compare( t1.remainTime, t2.remainTime );
//             return Double.compare( t2.remainTime / totalt2, t1.remainTime / totalt1 );

//         });
        // for( int[] job : jobs ){
//             Task task = new Task( job[ 1 ], job[ 0 ] );
//             pq.add( task );
//         }

//         while( !pq.isEmpty() ){
//             Task task = pq.poll();
//             int value;
//             if( time > task.requestTime ){
//                 value = ( time - task.requestTime ) + task.remainTime;
//                 time += task.remainTime;
//             }else{
//                 value = task.remainTime;
//                 time = task.requestTime;
//                 time += task.remainTime;
//             }
//             // System.out.println( "val: " + value );
//             answer += value;

//         }
//         // System.out.println( answer );
//         return answer / jobs.length;
        //문제에 요청시간 기준 정렬이 없었다.
        /**

         한번에 가려고 하는 버릇을 없애자.

         1. 내가 작업중인 시간이 있을 것이다.
         2. 작업이 끝나고 난 후에 요청이 가능한 것들이 있을 것이다.
         3. 이 요청 가능한 친구들 내에서 작업을 계속 뺀다.
         4. 전체 소요 시간이 나오면 전체 업무 갯수에서 나눈다.

         */
        Arrays.sort(jobs, ( t1, t2 ) -> t1[ 0 ] - t2[ 0 ]);
        PriorityQueue<Task> pq = new PriorityQueue<>( ( t1, t2 ) -> Integer.compare( t1.remainTime, t2.remainTime ) );

        int done = 0;
        int n = jobs.length;
        int idx = 0;
        while( done < n ){
            //1. 내가 작업 중인 시간대에 작업 가능한 job들을 pq에 넣자.

            while( idx < n && jobs[ idx ][ 0 ] <= time ){
                Task newTask = new Task( jobs[ idx ][ 1 ], jobs[ idx ][ 0 ] );
                idx ++;
                pq.add( newTask );
            }

            //시간이 0초에서 시작하는데 그럼 pq가 빌 수도 있다 이땐 시프팅.
            if( pq.isEmpty( ) ){
                time = jobs[ idx ][ 0 ];
                continue;
            }else{
                // 3.아니라면 해결 가능한 업무들이 있을 것이다. 이중 우선순위가 높은 애들을 뽑아서 처리하자.
                Task next = pq.poll();
                answer += ( time - next.requestTime ) + next.remainTime;
                time += next.remainTime;
                done++;
            }
        }
        //4. 나누자 / 문제에서 소수점은 버리라고 했다.
        return answer / n;


    }

    public class Task{
        int remainTime;
        int requestTime;
        public Task( int remainTime, int requestTime){
            this.remainTime = remainTime;
            this.requestTime = requestTime;
        }

    }
}