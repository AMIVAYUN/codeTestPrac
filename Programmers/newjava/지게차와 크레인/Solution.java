import java.util.*;
class Solution {
    int[] dx = { -1, 1, 0, 0 };
    int[] dy = { 0, 0, -1, 1 };
    int n, m;
    char[][] graph;
    ArrayList< int[] > entries = new ArrayList<>();
    public int solution(String[] storage, String[] requests) {
        int answer = 0;
        n = storage.length + 2; m = storage[ 0 ].length() + 2;
        graph = new char[ n ][ m ];
        boolean[][] visit = new boolean[ n ][ m ];
        for( int i = 0; i < n; i ++ ){
            Arrays.fill( graph[ i ], '*' );
        }
        for( int i = 0; i < n - 2; i ++ ){
            for( int j = 0; j < m - 2; j ++ ){
                graph[ i + 1 ][ j + 1 ] = storage[ i ].charAt( j );
            }
        }
        int idx = 0;
        for( String req : requests ){
            char target = req.charAt( 0 );
            if( req.length() > 1 ){
                for( int i = 0; i < n; i ++ ){
                    for( int j = 0; j < m; j ++ ){
                        if( graph[ i ][ j ] == target ){
                            graph[ i ][ j ] = '*';
                        }
                    }
                }
            }else{
                ArrayList< int[] > entries = getEntries();
                for( int[] entry: entries ){
                    int x = entry[ 0 ];
                    int y = entry[ 1 ];
                    
                    for( int i = 0; i < 4; i ++ ){
                        int nx = x + dx[ i ];
                        int ny = y + dy[ i ];
                        
                        if( nx >= 0 && nx < n && ny >= 0 && ny < m ){
                            if( graph[ nx ][ ny ] == target ){
                                graph[ nx ][ ny ] = '*';
                            }
                        }
                    }
                }
                
            }
        }
        for( int i = 0; i < n; i ++ ){
            for( int j = 0; j < m; j ++ ){
                if( graph[ i ][ j ] != '*' ) answer++;
            }
        }
        return answer;
    }
    
    private ArrayList<int[]> getEntries(){
        ArrayList<int[]> result = new ArrayList<>();
        ArrayDeque< int[] > dq = new ArrayDeque<>();
        dq.add( new int[]{ 0, 0 } );
        result.add( new int[]{ 0, 0 });
        boolean[][] visit = new boolean[ n ][ m ];
        visit[ 0 ][ 0 ] = true;
        while( !dq.isEmpty() ){
            int[] now = dq.poll();
            int x = now[ 0 ];
            int y = now[ 1 ];
            
            for( int i = 0; i < 4; i ++ ){
                int nx = x + dx[ i ];
                int ny = y + dy[ i ];
                
                if( nx >= 0 && nx < n && ny >= 0 && ny < m ){
                    if( graph[ nx ][ ny ] == '*' ){
                        if( !visit[ nx ][ ny ] ){
                            visit[ nx ][ ny ] = true;
                            dq.add( new int[]{ nx, ny } );
                            result.add( new int[]{ nx, ny } );
                        }
                    }
                }
            }
        }
        
        
        return result;
    }
}
