package PM.두수의_연산_값_비교하기;

class Solution {
    public int solution(int a, int b) {
        return operate2( operate( a, b ), 2 * a * b );
    }

    public int operate( int a, int b ){

        return Integer.parseInt( a + "" + b );
    }

    public int operate2( int a, int b ){
        if( a >= b ) return a;
        else return b;
    }
}
