package J14891;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static Gear[] gears = new Gear[ 4 ];
    static int n;
    static int point;


    public static void main(String[] args) throws IOException {

        for( int i = 0; i < 4; i ++ ){
            gears[ i ] = new Gear( bf.readLine(), i );
        }
        n = Integer.parseInt( bf.readLine() );
        for( int i = 0; i < n; i++ ){
            token = new StringTokenizer( bf.readLine() );
            int idx = stoi( token.nextToken() ) - 1;
            boolean isClock = stoi( token.nextToken() ) == 1;

            gears[ idx ].rotate( isClock, idx );
//            print();
        }
        for( int j = 0; j < 4; j ++ ){
            point += gears[ j ].getPoint();
        }

        System.out.println( point );

    }

    static Integer stoi( String token ){
        return Integer.parseInt( token );
    }

    static void print(){
        for( int i = 0; i < 4; i ++ ){
            System.out.print( gears[ i ].top + " " );
        }
        System.out.println();
    }

    static class Gear{
        int top = 0;
        int idx;
        int[] bearing = new int[ 8 ];

        public Gear( String bearings, int idx ){
            for( int i = 0; i < 8; i ++ ){
                char c = bearings.charAt( i );
                bearing[ i ] = c - '0';
            }
            this.idx = idx;
        }
        public int getRight(){
//            System.out.println( "right: " + this.top + " " + (( top + 2 ) % 8) );
            return bearing[( top + 2 ) % 8];
        }
        public int getLeft(){
//            System.out.println( "left :" + this.top + " " +( ( top - 2 ) > 0 ? top - 2 : top - 2 + 8 ) );
            return bearing[( top - 2 ) >= 0 ? top - 2 : top - 2 + 8];
        }

        public boolean isLeftAvailableRotation(){
            if( this.idx == 0 ){
                return false;
            }

            return gears[ this.idx - 1 ].getRight() != this.getLeft();

        }
        public boolean isRightAvailableRotation(){
            if( this.idx == 3 ){
                return false;
            }


//            System.out.println( gears[ this.idx + 1 ].getLeft() + " " + this.getRight() );
            return gears[ this.idx + 1 ].getLeft() != this.getRight();
        }

        public void rotate( boolean isClock, int before ){
            if( this.isLeftAvailableRotation() && ( this.idx <= before )){
                gears[ idx - 1 ].rotate( !isClock, this.idx );
            }
//            System.out.println( this.idx + " : " + before );
            if( this.isRightAvailableRotation() && ( this.idx >= before )){

                gears[ idx + 1 ].rotate( !isClock,this.idx );
            }

            this.top += isClock ? -1 : +1;
            this.top = this.top % 8;
            if( this.top < 0 ){
                this.top = 8 + this.top;
            }
        }


        public int getPoint(){
            int bias = (int)Math.pow( 2, this.idx );

//            System.out.println( this.idx + " " + this.bearing[ this.top ] * bias );
            return this.bearing[ this.top ] * bias;
        }

    }
}