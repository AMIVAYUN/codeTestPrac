package J31498;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//걍 가니깐 작살남

public class OldMain {
    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
       token = new StringTokenizer( bf.readLine() );
       long a = stol( token.nextToken() );
       long b = stol( token.nextToken() );

       token = new StringTokenizer( bf.readLine() );
       long c = stol( token.nextToken() );
       long d = stol( token.nextToken() );

       long k = stol( bf.readLine() );

       Person toka = new Person( b, a, k );

       Person dd = new Person( d, a + c, 0 );
       long cnt = 0;
       while( toka.pos > 0 && toka.pos < dd.pos ){
//           System.out.println(toka.pos + " " + dd.pos );
           toka.move();
           dd.move();
           cnt++;
       }

       if( toka.pos <= 0 ){
           System.out.println(cnt);
           return;
       }else{
           if( toka.pos >= dd.pos ){
               System.out.println( -1 );
           }else{
               System.out.println( cnt );
           }
       }

    }

    static Long stol( String token ){
        return Long.parseLong( token );
    }

    static Integer stoi( String token ){
        return Integer.parseInt( token );
    }

    static class Person{
        long speed;
        long pos;
        long bias;

        public Person(long speed, long pos, long bias) {
            this.speed = speed;
            this.pos = pos;
            this.bias = bias;
        }

        public Person(long speed, long pos) {
            this.speed = speed;
            this.pos = pos;
        }

        void move(){
            pos -= speed;
            speed -= bias;
            if( speed <= 0 ) speed = 0;
        }
    }
}
