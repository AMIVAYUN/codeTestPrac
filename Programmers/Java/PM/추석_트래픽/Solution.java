package PM.추석_트래픽;

import java.util.*;
class Solution {
    /*
        9월 15일 로그 데이터 분석 -> 초당 처리량 ㄱ산

            => 초당 최대 처리량 -> 임의 시간부터 1초간 처리하는 요청의 최대 개수

            로그 개수 최대 2000개

            1000 밀리초 -> 1초

            60초 -> 1분

            60분 -> 1시간

            1시간 -> 60 * 60 * 1000 밀리초
            1분 -> 60 * 1000 밀리초
            1초 -> 1000 밀리초


            log는 응답 완료 시간을 기준으로 오름차순 정렬이 되어있다.


    */

    public int solution(String[] lines) {
        int answer = 0;
        Time[] times = new Time[ lines.length ];
        int idx = 0;
        for( String line : lines ){
            times[ idx++ ] = new Time( line );
        }

        for( int i = 0; i < times.length; i ++ ){
            Time now = times[ i ];
            int cnt = 0;

            for( int j = i; j < times.length; j ++ ){
                Time target = times[ j ];
                if( now.endTime + 1000 > target.startTime ) cnt ++;
            }

            answer = Math.max( answer, cnt );
        }
        return answer;
    }


    public class Time{
        int startTime, endTime;

        public String toString(){
            return "startTime = " + startTime + " ,endTime = " + endTime;
        }

        public Time( String line ){
            String[] split = line.split(" ");
            String log = split[ 1 ];
            String turnAround = split[ 2 ];

            String[] logsplit = log.split(":");

            int time = 0;
            time += Integer.parseInt( logsplit[ 0 ] ) * 60 * 60 * 1000;
            time += Integer.parseInt( logsplit[ 1 ] ) * 60 * 1000;

            String[] secsplit = logsplit[ 2 ].split( "\\." );
            int test = 0;
            test += Integer.parseInt( secsplit[ 0 ] ) * 1000;
            test += Integer.parseInt( secsplit[ 1 ] );
            time += Integer.parseInt( secsplit[ 0 ] ) * 1000;
            time += Integer.parseInt( secsplit[ 1 ] );

            double turn = Double.parseDouble( turnAround.split("s")[ 0 ] ) * 1000;

            int val = ( int ) turn - 1;

            this.startTime = time - val;
            this.endTime = time;

        }
    }
}