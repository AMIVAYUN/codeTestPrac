import java.util.*;
import java.io.*;
public class J_1103 {
    public static int answer = 0;
    public static int[] dx = { 0, 0, -1, 1 };
    public static int[] dy = { 1, -1, 0, 0 };
    public static void DFS( int N, int R, ArrayList<String> graph, int[][] visit, int[][] mapper, int cnt, int[] now ){
        //System.out.println( now[ 0 ] + " " + now[ 1 ] +  " cnt: " + cnt);
        int x = now[ 0 ];
        int y = now[ 1 ];

        if( answer == -1 ){
            return;
        }
        char[] str0 = graph.get( x ).toCharArray();
        if( String.valueOf( str0[ y ] ).equals( "H" ) ){
            answer = Math.max( answer, cnt );
            return;
        }
        int bias = Integer.parseInt( String.valueOf(str0[ y ] ) );
        int dxi, dyi, nx, ny;
        for( int i = 0; i < 4; i++ ){
            if( answer == -1 ){
                return;
            }
            dxi = dx[ i ];
            dyi = dy[ i ];

            nx = x + dxi * bias;
            ny = y + dyi * bias;

            if( 0<= nx && nx < N && 0<= ny && ny < R ){

                String row = graph.get( nx );
                Character obj = row.charAt( ny );
                if( mapper[ nx ][ ny ] < cnt + 1 ){
                    if( visit[ nx ][ ny ] == 1 ){
                        answer = -1;
                        return;

                    }
                    mapper[ nx ][ ny ] = cnt + 1;
                    visit[ nx ][ ny ] = 1;
                    int[] next = { nx, ny };
                    answer = Math.max( answer, cnt + 1 );
                    DFS( N,R,graph,visit,mapper,cnt+1, next );
                    visit[ nx ][ ny ] = 0;

                }


            }
            else{
                answer = Math.max( answer, cnt + 1 );
            }




        }

    }
    public static void main( String[] args ) throws IOException {
        /*
        Scanner sc = new Scanner( System.in );
        int N = sc.nextInt();
        int R = sc.nextInt();

         */
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );
        String[] str0 = br.readLine().split( " " );
        int N = Integer.parseInt( str0[ 0 ] );
        int R = Integer.parseInt( str0[ 1 ] );
        ArrayList< String > arrayList = new ArrayList<>();

        for( int i = 0; i < N; i++){
            arrayList.add( br.readLine() );
        }

        int[][] visit = new int[ N ][ R ];
        int[][] mapper = new int[ N ][ R ];

        visit[ 0 ][ 0 ] = 1;
        mapper[ 0 ][ 0 ] = 1;

        int[] now = { 0, 0 };
        DFS( N,R ,arrayList, visit, mapper, 0, now );

        System.out.println( answer );

    }

}
