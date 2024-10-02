import java.util.*;
import java.io.*;
class Solution {
    /**

     1~8? 걍 완탐 돌려도 될 것이다.
     8! / 4! => 1200

     다 돌고 조건이 맞는지 체크하는 것 1200

     depth 안에서 banned_id 매칭하는 것 8**4

     그냥 뽑고 체크가 맞음

     */
    public boolean[] visited;
    public ArrayList<Integer> lst = new ArrayList<>();
    public int depthMx, cnt, n;
    public String[] user_id, banned_id;
    public HashMap< Integer, Boolean > map = new HashMap<>();
    public int solution(String[] user_id, String[] banned_id) {
        cnt = 0;
        n = user_id.length;
        this.user_id = user_id;
        this.banned_id = banned_id;
        visited = new boolean[ user_id.length ];
        depthMx = this.banned_id.length;
        permutation( 0 );

        return cnt;
    }

    public void permutation( int depth ){

        if( depth == depthMx ){
            ArrayList<Integer> tmp = new ArrayList<>();
            for( int i : lst ){
                tmp.add( i );
            }
            Collections.sort( tmp );
            int val = 0;


            for( int i = depthMx - 1; i >= 0; i -- ){
                val += tmp.get( i );
                val *= 10;
            }


            if( isRight() ){
                if( !map.getOrDefault( val, false ) ){
                    cnt++;
                    map.put( val, true );
                }
            }

            return;
        }

        for( int i = 0; i < n; i ++ ){
            if( !visited[ i ] ){
                visited[ i ] = true;
                lst.add( i );
                permutation( depth + 1 );
                lst.remove( lst.size() - 1 );
                visited[ i ] = false;
            }
        }

    }

    public boolean isRight(){
        for( int i = 0; i < depthMx; i ++ ){
            if( !match( user_id[ lst.get( i ) ], banned_id[ i ] ) ){
                return false;
            }
        }

        return true;
    }
    public boolean match( String s1, String s2 ){
        if( s1.length() != s2.length() ){
            return false;
        }


        for( int i = 0; i < s1.length(); i++ ){
            if( s1.charAt( i ) != s2.charAt( i ) ){
                if( s2.charAt( i ) != '*' ){
                    return false;
                }
            }
        }

        return true;
    }
}