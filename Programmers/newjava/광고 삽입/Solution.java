import java.util.*;
class Solution {
    public int mx = 360000;
    public int[] time = new int[ mx ];
    public String solution(String play_time, String adv_time, String[] logs) {
        //로그 별로 다돌아 버리면 360000 * 300000 이므로 버티질 못한다.
        // 각 광고의 시작시간과 끝 시간을 기준으로 가장 많이 겹치는 광고를 찾아서 리턴하면 되지 않나.
        // 100 시간 => 6000분 => 360000초;
        String answer = "";

        int pmx = strToTime( play_time );
        int amx = strToTime( adv_time );

        if( pmx == amx ){ return "00:00:00"; }
        int n = logs.length;
        for( int i = 0; i < n; i ++ ){
            String log = logs[ i ];
            String[] sp = log.split("-");
            int startTime = strToTime( sp[ 0 ] );
            int endTime = strToTime( sp[ 1 ] );

            for( int j = startTime; j < endTime; j++ ){
                time[ j ]++;
            }
        }

        long tot = 0;
        long[] mxtot = new long[]{ 0, 0 };
        for( int i = 0; i < amx; i ++ ){
            tot += time[ i ];
        }

        mxtot[ 0 ] = tot;

        for( int i = amx; i < pmx; i ++ ){
            tot = tot - time[ i - amx ] + time[ i ];

            if( mxtot[ 0 ] < tot ){
                mxtot[ 0 ] = tot;
                mxtot[ 1 ] = i - amx + 1;
            }
        }

        return timeToString( (int)mxtot[ 1 ] );
    }

    public int strToTime( String time ){
        String[] sp = time.split(":");
        int h = Integer.parseInt( sp[ 0 ] );
        int m = Integer.parseInt( sp[ 1 ] );
        int s = Integer.parseInt( sp[ 2 ] );

        return 3600*h + 60*m + s;
    }

    public String timeToString( int time ){
        int h = time / 3600;
        time = time % 3600;
        int m = time / 60;
        time = time % 60;
        int s = time;

        String H = h < 10 ? "0" + h : h + "";
        String M = m < 10 ? "0" + m : m + "";
        String S = s < 10 ? "0" + s : s + "";

        return H+":"+M+":"+S;
    }
}