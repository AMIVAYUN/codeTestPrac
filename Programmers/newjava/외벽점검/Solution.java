import java.util.*;
import java.io.*;
class Solution {
    /**

     외벽 n미터 둘레

     추위 심하면 취약 지점 o

     1시간 제한 검사

     1시간 마다 인부들 이동거리가 다름

     시계 반시계 선택 가능

     보내야 되는 친구 최소 값

     n은 1 이상 200 이하 자연수

     사람은 최대 8명

     그러면 1명 부터 8명 까지 조합을 구하고 이게 되는지 판별하는게 제일 빠를듯

     */
    public boolean[] visited;
    public int people, k;
    public boolean flag = false;
    public int[] doubleWeak, dist;
    public ArrayList<Integer> workers = new ArrayList<>();
    public int solution(int n, int[] weak, int[] dist) {
        int answer = 0;

        people = dist.length;
        visited = new boolean[ people ];
        k = weak.length;
        this.dist = dist;
        doubleWeak = new int[ k * 2 ];
        for( int i = 0; i < k; i ++ ){
            doubleWeak[ i ] = weak[ i ];
            doubleWeak[ i + k ] = weak[ i ] + n;
        }

        for( int i = 1; i < people + 1; i ++ ){
            getPermutation( 0, i );
            if( flag ){
                // System.out.println( "result = " + i );
                answer = i;
                break;
            }
        }

        return flag ? answer : -1;
    }

    public void getPermutation( int depth, int Mx ){
        if( depth == Mx ){
            // System.out.println( workers.toString() );
            for( int i = 0; i < k; i ++ ){
                boolean result = getResult( i, Mx );
                if( result ){

                    flag = true;
                }
            }

            return;
        }
        for( int i = 0; i < people; i ++ ){
            if( !visited[ i ] ){
                visited[ i ] = true;
                workers.add( i );
                getPermutation( depth + 1, Mx );
                if( flag ) return;
                workers.remove( workers.size() - 1 );
                visited[ i ] = false;
            }
        }
    }
    public boolean getResult( int start, int Mx ){
        // System.out.println( doubleWeak[ start ]+ ", " + workers.size() );
        int pos = doubleWeak[ start ];
        int now = start;
        int person = 0;

        for( int i = start; i < start + k; i ++ ){
            if( person >= Mx ) return false;
            // System.out.println( "pos = " + pos );
            if( doubleWeak[ i ] - pos > dist[ workers.get( person ) ] ){
                person++;
                pos = doubleWeak[ i ];
            }
        }
        return person != Mx;

    }

}