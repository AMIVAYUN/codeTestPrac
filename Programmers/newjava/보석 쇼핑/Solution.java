import java.util.*;
import java.io.*;
class Solution {

    /*

        진열된 모든 보석을 1개 이상 포함하는 가장 짧은 구간을 구매;

        이분탐색?

    */
    HashSet< String > set = new HashSet<>();
    public int[] solution(String[] gems) {
        int[] answer = { 1, gems.length + 1 };
        int n = gems.length;
        for( String gem : gems ){
            set.add( gem );
        }
        int k = set.size();
        if( k == 1 ) return new int[]{ 1, 1 };

//         int lt = 1; int rt = n;
//         // 양사이드에서 가면 시간 초과
//         while( lt <= rt ){
//             int mid = ( lt + rt ) / 2;
//             // System.out.println( mid );
//             int start = 0;
//             int cnt = 0;
//             for( int i = 0; i < n - mid + 1; i ++ ){
//                 start = i;
//                 cnt = 0;
//                 HashMap< String, Boolean > map = new HashMap<>();
//                 for( int j = i; j < i + mid; j ++ ){
//                     if( !map.getOrDefault( gems[ j ], false ) ){
//                         cnt++;
//                         map.put( gems[ j ], true );
//                     }
//                     if( cnt == k ){
//                         break;
//                     }
//                 }
//                 if( cnt == k ){
//                     break;
//                 }

//             }

//             if( cnt == k ){
//                 rt = mid - 1;
//                 answer[ 0 ] = start + 1;
//                 answer[ 1 ] = start + mid;
//             }else{
//                 lt = mid + 1;
//             }

//         }

//         int lt = 0; int rt = 0;

//         while( lt <= rt && lt < n && rt < n ){
//             HashSet<String> set = new HashSet<>();
//             for( int i = lt; i <= rt; i ++ ){
//                 set.add( gems[ i ] );
//             }

//             // System.out.println( lt + ", " + rt + ", " + set + set.size() );
//             if( set.size() < k ){
//                 rt++;
//             }else{

//                 if( answer[ 1 ] - answer[ 0 ] > rt - lt ){
//                     // System.out.println( "answer!! " + lt + " , " + rt + ", " + set.size() );
//                     answer[ 0 ] = lt + 1; answer[ 1 ] = rt + 1;
//                 }
//                 lt++;
//             }
//         }


//         return answer;

        ArrayDeque< String > dq = new ArrayDeque<>();

        HashMap< String, Integer> map = new HashMap<>();
        int lt = 0;
        for( int i = 0; i < n; i ++ ){
            dq.add( gems[ i ] );
            map.put( gems[ i ], map.getOrDefault( gems[ i ], 0 ) + 1 );
            while( !dq.isEmpty() && map.getOrDefault( dq.peekFirst(), 0 ) - 1 > 0 ){
                map.put( dq.peekFirst(), map.get( dq.peekFirst() ) -1 );
                dq.poll();
                lt++;
            }

            if( map.keySet().size() == k && answer[ 1 ] - answer[ 0 ] > i - lt ){
                answer[ 0 ] = lt + 1;
                answer[ 1 ] = i + 1;
            }
        }
        return answer;

    }
}