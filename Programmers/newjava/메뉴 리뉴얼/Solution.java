import java.util.*;
/**
 최소 두명 **
 */
class Solution {
    Map<Integer, Map< String, Integer>> map = new HashMap<>();
    Map<Integer, ArrayList<String>> map2 = new HashMap<>();
    int mx[];
    public String[] solution(String[] orders, int[] course) {
        String[] answer = {};
        int idx = 0;
        mx = new int[ course[ course.length - 1 ] + 1 ];
        for( String order: orders ){
            char[] arr = order.toCharArray();
            Arrays.sort( arr );
            String str = String.valueOf( arr );

            for( int c : course ){
                dfs( new StringBuilder(), c, 0, str );
            }
        }
        List<String> result = new ArrayList<>();
        for( int c : course ){
            if( mx[ c ] <= 1 ) continue;
            result.addAll( map2.get( c ) );
        }
        Collections.sort( result );
        answer = result.toArray( new String[ 0 ] );
        return answer;
    }

    private void dfs( StringBuilder sb, int len, int idx, String origin ){
        String str = sb.toString();
        if( str.length() == len ){

            Map<String,Integer> detail = map.getOrDefault( len, new HashMap<>() );
            detail.put( str, detail.getOrDefault( str, 0 ) + 1 );
            if( detail.get( str ) > mx[ len ] ){
                mx[ len ] = detail.get( str );
                map2.put( len, new ArrayList< String >() );
                map2.get( len ).add( str );
            }else if( detail.get( str ) == mx[ len ] ){
                map2.get( len ).add( str );
            }
            map.put( len, detail );
            return;
        }

        for( int i = idx; i < origin.length(); i ++ ){
            sb.append( origin.charAt( i ) );
            dfs( sb, len, i + 1, origin );
            sb.deleteCharAt( sb.length() - 1 );
        }
    }
}