import java.util.*;
class Solution {

    ArrayDeque< Node > stack;

    public String solution(int n, int k, String[] cmd) {
        String answer = "";


        stack = new ArrayDeque<>();

        Node cursor = new Node( 0 );
        Node pos = cursor;
        for( int i = 1; i < n; i ++ ){
            Node newNode = new Node( i );
            newNode.prev = pos;
            pos.next = newNode;
            pos = pos.next;
        }

        for( int i = 0; i < k; i ++ ){
            cursor = cursor.next;
        }

        for( String c : cmd ){
            // System.out.println( c + " cursor = " + select + " , " + Arrays.toString( deleted ) );
            String[] cp = c.split( " " );
            if( cp[ 0 ].equals( "D" ) ){
                int cnt = 0;
                int mx = Integer.parseInt( cp[ 1 ] );
                while( cnt < mx && cursor.next != null ){
                    cursor = cursor.next;
                    cnt++;
                }

            }else if( cp[ 0 ].equals( "U" ) ){
                int cnt = 0;
                int mx = Integer.parseInt( cp[ 1 ] );
                while( cnt < mx && cursor.prev != null ){
                    cursor = cursor.prev;
                    cnt++;
                }

            }else if( cp[ 0 ].equals( "C" ) ){
                cursor.delete();
                if( cursor.next == null ){
                    cursor = cursor.prev;
                }else{
                    cursor = cursor.next;
                }

            }else{
                Node target = stack.pollLast();
                if( target.prev != null ) target.prev.next = target;
                if( target.next != null ) target.next.prev = target;

            }
        }

        char[] ans = new char[ n ];
        Arrays.fill( ans, 'O' );
        while( !stack.isEmpty() ){
            Node t = stack.poll();
            ans[ t.idx ] = 'X';
        }

        return new String( ans );
    }


    public class Node{
        Node prev;
        Node next;
        int idx;

        public Node( int idx ){
            this.idx = idx;
        }

        public void delete(){
            stack.add( this );
            if( this.prev != null ) this.prev.next = this.next;
            if( this.next != null ) this.next.prev = this.prev;

        }

    }

    //배열로 만들면 이게 문제임 -> 자식 찾는데 n번씩 돔.
    public int findChild( int n, int[] parents, int target, boolean[] deleted ){
        for( int i = 0; i < n; i ++ ){
            if( parents[ i ] == target && !deleted[ i ] ) return i;
        }

        return -1;
    }
}