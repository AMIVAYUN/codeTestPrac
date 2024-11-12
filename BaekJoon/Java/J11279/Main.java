package J11279;



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;



    public static void main(String[] args) throws IOException {

        int n = Integer.parseInt( bf.readLine() );
        Heap heap = new Heap();
        for( int i = 0; i < n; i ++ ){
            int t = Integer.parseInt( bf.readLine() );
//            System.out.println( t );
            if( t == 0 ){
                if( heap.heap.size() != 1 ){
                    System.out.println(heap.delete());
                }else{
                    System.out.println(0);
                }
            }else{
                heap.insert( t );
            }
        }

    }
    static class Heap{
        ArrayList< Integer > heap;
        public Heap() {
            heap = new ArrayList<>();
            heap.add( 0 );
        }

        void insert( int k ){
            heap.add( k );
            int p = heap.size() - 1;

//            System.out.println( p + " " + heap.toString() );

            while( p > 1 && heap.get( p ) > heap.get( p / 2 ) ){
                swap( p, p / 2 );
                p /= 2;
            }

//            System.out.println( heap );
        }

        void swap( int i1, int i2 ){
            int temp = heap.get( i1 );
            heap.set( i1, heap.get( i2 ) );
            heap.set( i2, temp );
        }

        int delete(){
            int result = heap.get( 1 );
            int idx = 1;



            if( heap.size() == 2 ){
                heap.remove( 1 );
                return result;
            }

            heap.set( idx, heap.remove( heap.size() - 1 ) );

            while( idx * 2 < heap.size() ){
                int mx = heap.get( idx * 2 );
                int left = idx * 2;
                int right = left + 1;

                int next = left;

                if( right < heap.size() && heap.get( left ) < heap.get( right )){
                    mx = heap.get( right );
                    next = right;
                }

                if( mx < heap.get( idx ) ){
                    break;
                }
                swap( idx, next );
                idx = next;
            }

//            System.out.println(heap.toString());

            return result;

        }
    }
}
