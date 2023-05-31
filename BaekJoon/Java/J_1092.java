import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class J_1092 {

    public static int bisect_right( ArrayList<Integer> lst, int target ){
        int lt, rt, mid;

        int ans = 0 ;
        boolean flag = true;
        lt = 0; rt = lst.size() - 1;

        while( lt <= rt ){
            mid = ( lt + rt ) / 2;

            if( lst.get( mid ) <= target ){
                lt = mid + 1;
                flag = false;
                ans = mid;
            }
            else{
                rt = mid - 1;
            }

        }
        if( flag ){
            return -1;
        }

        return ans;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in) );
        int N = Integer.parseInt( bf.readLine() );
        int[] cranes = Arrays.stream(bf.readLine().split(" ")).mapToInt( Integer::parseInt ).toArray();

        int M = Integer.parseInt( bf.readLine() );
        ArrayList< Integer >boxes = (ArrayList<Integer>) Arrays.stream( bf.readLine().split( " " ) ).map( Integer::parseInt ).collect(Collectors.toList() );

        Arrays.sort( cranes );
        Collections.sort( boxes );

        if( cranes[ cranes.length - 1 ] < boxes.get( boxes.size() - 1 ) ){
            System.out.println( -1 );
        }else{
            int time = 0;
            while ( !boxes.isEmpty() ){
                for( int i = 0; i < N; i++ ){
                    if( boxes.size() == 0 ){
                        break;
                    }
                    int next = bisect_right( boxes, cranes[ i ] );
                    if( next == -1 ){
                        continue;
                    }
                    boxes.remove( next );

                }
                time += 1;



            }

            System.out.println( time );
        }












    }




}
