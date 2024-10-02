import java.util.*;
import java.io.*;
class Solution {
    /*

        6가지 완탐? 100 * 3 을 6번

    */
    HashMap< Character, Boolean > map = new HashMap<>();
    char[] operator = new char[ 3 ];
    long answer = 0;
    ArrayList<Integer> nums = new ArrayList<>();
    ArrayList<Character> operators = new ArrayList<>();
    public long solution(String expression) {
        String num = "";
        operator[ 0 ] = '+';
        operator[ 1 ] = '-';
        operator[ 2 ] = '*';
        map.put('+',true);map.put('-',true);map.put('*',true);
        for( int i = 0; i < expression.length(); i ++ ){
            char c = expression.charAt( i );
            if( map.getOrDefault( c, false ) ){
                nums.add( Integer.parseInt( num ) );
                num = "";
                operators.add( c );
                continue;
            }
            num += c;
        }

        nums.add( Integer.parseInt( num ) );

        permutation( 0 );

        return answer;
    }
    boolean[] visited = new boolean[ 3 ];
    ArrayList<Integer> lst = new ArrayList<>();
    public void permutation( int depth ){
        if( depth == 3 ){
            getResult();
            return;
        }

        for( int i = 0; i < 3; i ++ ){
            if( !visited[ i ] ){
                visited[ i ] = true;
                lst.add( i );
                permutation( depth + 1 );
                lst.remove( lst.size() - 1 );
                visited[ i ] = false;
            }
        }
    }

    public void getResult(){

        // System.out.println( "start! : " + nums + operators + lst );

        ArrayList<Long> tmp = new ArrayList<>();
        for( int i = 0; i < nums.size(); i ++ ){
            tmp.add( (long)nums.get( i ) ) ;
        }
        ArrayList<Character> otmp = new ArrayList<>();

        for( int i = 0; i < operators.size(); i ++ ){
            otmp.add( operators.get( i ) );
        }
        ArrayDeque< Long > dq = new ArrayDeque<>();


        for( int i = 0; i < 3; i ++ ){
            char target = operator[ lst.get( i ) ];
            ArrayList<Character> newOtmp = new ArrayList<>();

            dq.add( tmp.get( 0 ) );
            for( int j = 1; j < tmp.size(); j ++ ){
                if( target == otmp.get( j - 1 ) ){

                    long val = dq.pollLast();
                    long res = operate( target, val, tmp.get( j ) );
                    dq.add( res );

                }else{
                    dq.add( tmp.get( j ) );
                    newOtmp.add( otmp.get( j - 1 ) );
                }
            }
            // otmp = newOtmp;
            otmp = newOtmp;

            tmp = new ArrayList<>();

            while( !dq.isEmpty() ){
                tmp.add( dq.poll() );
            }

        }

        answer = Math.max( answer, Math.abs( tmp.get( 0 ) ) );

    }

    public long operate( char c, long a, long b ){
        if( c == '+' ) {
            return a + b;
        }else if( c == '*'){
            return a * b;
        }else{
            return a - b;
        }


    }
}