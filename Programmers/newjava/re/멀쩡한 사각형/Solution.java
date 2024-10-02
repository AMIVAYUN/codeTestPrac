import java.util.*;
class Solution {

    int Mx;

    public long solution(int w, int h) {

        int gcd = getGCD( w, h );

        long ww = ( long ) w;
        long hh = ( long ) h;

        return ww * hh - ( ww + hh - getGCD( w, h ) );


    }

    public int getGCD( int a, int b ){
        if( b == 0 ){
            return a;
        }

        return getGCD( b, a % b );
    }
}