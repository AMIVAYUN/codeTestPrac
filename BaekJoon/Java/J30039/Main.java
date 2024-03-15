package J30039;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {
        /*

        hpush x : 가로 Queue의 맨 뒤에 정수 x를 넣는다.( 1<= x <= 100,000 )
        hpop : 가로 Queue에 정수가 있다면 맨 앞에 있는 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        hfront : 가로 Queue에 정수가 있다면 맨 앞에 있는 정수를 출력한다. 없다면 -1을 대신 출력한다.
        hback : 가로 Queue에 정수가 있다면 맨 뒤에 있는 정수를 출력한다. 없다면 -1을 대신 출력한다.
        hsize : 가로 Queue에 들어있는 정수의 개수를 출력한다.
        vpush x : 세로 Queue의 맨 뒤에 정수 x를 넣는다. ( 1 <= x <= 100,000 )
        vpop : 세로 Queue에 정수가 있다면 맨 앞에 있는 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        vfront : 세로 Queue에 정수가 있다면 맨 앞에 있는 정수를 출력한다. 없다면 -1을 대신 출력한다.
        vback : 세로 Queue에 정수가 있다면 맨 뒤에 있는 정수를 출력한다. 없다면 -1을 대신 출력한다.
        vsize : 세로 Queue에 들어있는 정수의 개수를 출력한다.
        size : Queueueue에 들어있는 정수의 개수를 출력한다.
        empty : Queueueue가 비어있으면 1, 아니면 0을 출력한다.
        middle : Queueueue에 정수가 있다면 Queueueue의 공유 원소에 해당하는 정수를 출력한다. 없다면 -1을 대신 출력한다.

         */

        n = Integer.parseInt( bf.readLine() );



    }

    static class Queueueue{
        ArrayDeque<Integer> up = new ArrayDeque<>();
        ArrayDeque<Integer> down = new ArrayDeque<>();
        ArrayDeque<Integer> left = new ArrayDeque<>();
        ArrayDeque<Integer> right = new ArrayDeque<>();
        Integer rowSize = 0;
        Integer verticalSize = 0;
        Integer center = 0;

        public void hpush(){

        }

        public void hpop(){

        }

        public void hfront(){

        }

        public void hback(){

        }

        public void hsize(){

        }

        public void vpush(){

        }

        public void vpop(){

        }

        public void vfront(){

        }

        public void vback(){

        }

        public void vsize(){

        }

        public void size(){
            System.out.println(this.rowSize + this.verticalSize - 1);
        }

        public void empty(){
            System.out.println( this.center == 0 ? 1 : 0 );
        }

        public void middle(){
            System.out.println( this.center == 0 ? -1 : this.center );
        }
    }
}
