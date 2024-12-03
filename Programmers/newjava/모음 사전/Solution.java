import java.util.*;
class Solution {
    boolean flag = true;
    String word;
    HashMap<String, Integer> map = new HashMap<>();
    String[] ws = { "A", "E", "I", "O", "U" };
    public int solution(String word) {
        this.word = word;
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        dfs( 0, sb );
        return map.get( word );
    }
    int cnt = 1;
    void dfs( int depth, StringBuilder sb ){
        if( sb.toString().equals( word ) ){
            flag = false;
            return;
        }

        if( depth == 5 ){
            return;
        }

        for( int i = 0; i < 5 && flag; i ++ ){
            sb.append( ws[ i ] );
            map.put( sb.toString(), cnt++ );
            dfs( depth + 1, sb );
            sb.deleteCharAt( sb.length() - 1 );
        }



    }
}