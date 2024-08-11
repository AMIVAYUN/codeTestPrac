package PM.셔틀버스;

import java.util.*;
class Solution {

    Bus[] buses;
    public String solution(int n, int t, int m, String[] timetable) {
        String answer = "";
        int[] people = new int[ timetable.length ];
        buses = new Bus[ n ];



        int startTime = 540;
        for( int i = 0; i < n; i ++ ){
            buses[ i ] = new Bus( startTime );
            startTime += t;
        }

        for( int i = 0; i < timetable.length; i ++ ){
            String[] value = timetable[ i ].split(":");
            people[ i ] += 60 * Integer.parseInt( value[ 0 ] );
            people[ i ] += Integer.parseInt( value[ 1 ] );
        }

        Arrays.sort( people );

        int busIdx = 0;
        int personIdx = 0;
        while( busIdx < n ){

            Bus bus = buses[ busIdx ];
            int Mx = 0;
            while( personIdx < timetable.length && people[ personIdx ] <= bus.startTime && Mx < m ){
                bus.lst.add( people[ personIdx++ ] );
                Mx++;
            }


            busIdx++;
        }

        Bus lastBus = buses[ n - 1 ];
        int Mx = -1;
        for( int customer: lastBus.lst ){
            Mx = Math.max( customer, Mx );
        }

        if( Mx == -1 || lastBus.lst.size() < m ){
            return IntegerTimeToString( lastBus.startTime );
        }


        return IntegerTimeToString( Mx - 1 );


    }

    public class Bus{
        int startTime;
        ArrayList< Integer > lst = new ArrayList<>();

        public Bus( int startTime ){
            this.startTime = startTime;
        }
        @Override
        public String toString(){
            return "Bus = [ startedAt: " + startTime + ", customer: " + lst.toString() + "]";
        }
    }

    public String IntegerTimeToString( Integer time ){
        int hours = time / 60;
        int minutes = time % 60;

        String shours = hours < 10 ? "0" + hours : hours + "";
        String sminutes = minutes < 10 ? "0" + minutes : minutes + "";

        return shours+":"+sminutes;
    }
}