class Solution {
    public int solution(String s) {
        int answer = s.length();

        for( int size = 1; size <= s.length(); size ++ ){

            String res = "";
            if( size == s.length() ){
                res = s;
            }

            int count = 1;
            int idx = size;
            String query = s.substring( 0, size );
            while( idx < s.length() ){
                while( idx + size <= s.length() && query.equals( s.substring( idx, idx + size ) ) ){
                    count++;
                    idx += size;
                }

                if( count == 1 ){
                    res += query;
                }else{
                    res += count + query;
                }
                if( idx + size >= s.length() ){
                    res += s.substring( idx, s.length() );
                    break;
                }
                query = s.substring( idx, idx + size );
                idx += size;
                count = 1;

            }
            answer = Math.min( answer, res.length() );
        }

        return answer;
    }
}