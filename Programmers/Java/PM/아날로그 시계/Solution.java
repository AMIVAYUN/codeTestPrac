import java.util.*;
import java.io.*;
class Solution {
    // 1초 -> 1/60분 1/3600 시간
    // 1초를 3600 이라 가정하면
    // 3600( 1초 ) -> 60 (분) - 1시간
    // 너무 큼 다른 방식으로 풀어보자.

    //60초 -> 원 한바퀴 > 360
    //1초 -> 시침 부채꼴 -> 6
    //1초 -> 분침 -> 0.1
    //1초 -> 시침 -> 1/120
    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {


        int sec1 = Time.toSecond( h1, m1, s1 );
        int sec2 = Time.toSecond( h2, m2, s2 );

        int answer = ( (sec1 == 0) || ( sec1 == 43200 ) ) ? 1 : 0;

        while( sec1 < sec2 ){
            int nextsec = sec1 + 1;
            int[] nowTime = Time.getTime( sec1 );
            int[] nextTime = Time.getTime( nextsec );

            Double[] nowDegree = Time.getDegree( nowTime[ 0 ], nowTime[ 1 ], nowTime[ 2 ] );
            Double[] nextDegree = Time.getDegree( nextTime[ 0 ] , nextTime[ 1 ], nextTime[ 2 ] );


            boolean hResult = hourPass( nowDegree, nextDegree );
            boolean mResult = minutePass( nowDegree, nextDegree );

            if( hResult && mResult ){
                if(Double.compare(nextDegree[0],nextDegree[1]) == 0){
                    answer ++;
                }else{
                    answer += 2;
                }
            }else if( hResult || mResult ){
                answer ++;
            }

            sec1++;

        }

        return answer;
    }
    static class Time{

        static int[] getTime( int sec ){
            int[] times = new int[ 3 ];
            times[ 0 ] = sec / 3600;
            times[ 1 ] = ( sec % 3600 ) / 60;
            times[ 2 ] = ( sec % 3600 ) % 60;

            return times;
        }


        static int toSecond( int h, int m, int s ){
            return h * 3600 + m * 60 + s;
        }

        static Double[] getDegree( int h, int m, int s ){
            Double[] doubles = new Double[ 3 ];
            doubles[ 0 ] = (h % 12) * 30d + m*0.5d + s * (1/120d);
            doubles[ 1 ]= m * 6d + s * (0.1d);
            doubles[ 2 ] = s * 6d;

            return doubles;
        }
    }

    boolean hourPass( Double[] now, Double[] next ){
        if( now[ 0 ] > now[ 2 ] && next[ 0 ] <= next[ 2 ] ) return true;
        if( (now[ 2 ] == 354d ) && next[ 0 ] > 354d ) return true;
        return false;
    }

    boolean minutePass( Double[] now, Double[] next ){
        if( now[ 1 ] > now[ 2 ] && next [ 1 ] <= next[ 2 ] ) return true;
        if( (now[ 2 ] == 354d) && next[ 1 ] > 354d ) return true;
        return false;
    }
}