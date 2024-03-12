package J20055;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringTokenizer token;
    static int n, k;
    static Part[] conveyor;
    static int top;
    static int cnt = 0;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = stoi( token.nextToken() );
        k = stoi( token.nextToken() );

        conveyor = new Part[ n * 2 ];
        top = 0;
        token = new StringTokenizer( bf.readLine() );
        for( int i = 0; i < n * 2; i ++ ){
            conveyor[ i ] =new Part( stoi(token.nextToken()), false );
        }
        while( k > 0 ){


            MoveConv();
            MoveRobot();
            cnt++;
        }

        System.out.println(cnt);
    }

    private static void MoveRobot() {
//        System.out.println( top + " : " + getLast() );
        int count = 0;
        int i = getLast();
        for( ; count < n; i = getBefore( i ) ){
//            System.out.println("idx: " +  i );
            int next = getNext( i );
            if( !conveyor[ next ].isRobot && conveyor[ next ].durability > 0 ){
                if( conveyor[ i ].isRobot ){
                    conveyor[ next ].isRobot = true;
                    conveyor[ next ].durability --;
                    conveyor[ i ].isRobot = false;
                    if( conveyor[ next ].durability == 0){
                        k--;
                    }
                }
                if( getLast() == next ) {
                    conveyor[next].isRobot = false;
                }
            }

            count++;
        }
//        System.out.println( "first : " + getNext( i ));
        if( !conveyor[ getNext( i ) ].isRobot && conveyor[ getNext( i ) ].durability > 0 ){
            conveyor[ getNext( i ) ].isRobot = true;
            conveyor[ getNext( i ) ].durability --;
            if( conveyor[ getNext( i ) ].durability == 0 ){
                k--;
            }
        }
    }

    private static int getBefore( int value ){
        int before = value - 1;
        return before >= 0 ? before : ( n * 2 ) + before;
    }

    private static int getNext( int value ){
        return ( value + 1 ) % ( n * 2 );
    }

    private static int getLast(){
        return ( top + n - 1 ) % ( n * 2 );
    }



    private static void MoveConv() {
        top = getBefore( top );
        if( conveyor[ getLast() ].isRobot ){
            conveyor[ getLast() ].isRobot = false;
        }
    }

    static int stoi( String token ){
        return Integer.parseInt( token );
    }
    static class Part{
        int durability;
        boolean isRobot;

        public Part(int durability, boolean isRobot) {
            this.durability = durability;
            this.isRobot = isRobot;
        }

        @Override
        public String toString() {
            return "Part{" +
                    "durability=" + durability +
                    ", isRobot=" + isRobot +
                    '}';
        }
    }




}
