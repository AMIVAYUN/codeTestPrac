import java.util.*;
import java.io.*;
public class J_14267 {
    public static int[] dp;

    public static void main( String[] args ) throws IOException {
        int N, M;


        BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );

        String[] numbers = bf.readLine().split( " " );

        N = Integer.parseInt( numbers[ 0 ] ); M = Integer.parseInt( numbers[ 1 ] );

        String[] arr = bf.readLine().split( " " );

        Node[] fields = new Node[ N + 1 ];

        Node root = new Node( 1 );

        fields[ 1 ] = root;

        dp = new int[ N + 1 ];

        dp[ 1 ] = 0;
        //채우고
        Arrays.fill( dp, -1 );

        for( int idx = 1; idx < N ; idx ++ ){
            int val = Integer.parseInt( arr[ idx ] );
            Node newNode = new Node( fields[ val ], idx + 1 );
            fields[ idx + 1 ] = newNode;

        }

        for( int idx = 0; idx < M; idx ++ ){
            String[] compliments = bf.readLine().split( " " );

            int a = Integer.parseInt( compliments[ 0 ] ); int b = Integer.parseInt( compliments[ 1 ] );

            fields[ a ].weight += b;

        }


        for( int idx = 1; idx < N + 1; idx ++ ){
            System.out.print( fields[ idx ].getWeight() + " " );
        }


    }

    static class Node{
        public Node father;
        public int weight = 0;
        public ArrayList< Node > childs = new ArrayList<>();
        public int index;

        public Node( Node father, int index ){
            this.index = index;
            this.father = father;
        }

        public Node( int index ){
            this.father = null;
            this.index = index;
        }

        public int getWeight(){
            int tmp = 0;

            Node pos = this;

            while( pos.father != null ){
                if( dp[ pos.index ] != -1 ){
                    tmp += dp[ pos.index ];
                    break;
                }
                tmp += pos.weight;
                pos = pos.father;
            }
            dp[ this.index ] = tmp;
            return tmp;

        }
    }


    /*
    public static solution1(){
        public static void main( String[] args ) throws IOException {
            int N, M;

            BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );

            String[] numbers = bf.readLine().split( " " );

            N = Integer.parseInt( numbers[ 0 ] ); M = Integer.parseInt( numbers[ 1 ] );

            String[] arr = bf.readLine().split( " " );

            Node[] fields = new Node[ N + 1 ];

            Node root = new Node();

            fields[ 1 ] = root;
            for( int idx = 1; idx < N ; idx ++ ){
                int val = Integer.parseInt( arr[ idx ] );
                Node newNode = new Node( fields[ val ] );
                fields[ idx + 1 ] = newNode;

            }

            for( int idx = 0; idx < M; idx ++ ){
                String[] compliments = bf.readLine().split( " " );

                int a = Integer.parseInt( compliments[ 0 ] ); int b = Integer.parseInt( compliments[ 1 ] );

                fields[ a ].weight += b;

            }


            for( int idx = 1; idx < N + 1; idx ++ ){
                System.out.print( fields[ idx ].getWeight() + " " );
            }


        }

        static class Node{
            public J_14267.Node father;
            public int weight = 0;
            public ArrayList<J_14267.Node> childs = new ArrayList<>();


            public Node( J_14267.Node father ){
                this.father = father;
            }

            public Node(){
                this.father = null;
            }

            public int getWeight(){
                int tmp = 0;

                J_14267.Node pos = this;

                while( pos.father != null ){
                    tmp += pos.weight;
                    pos = pos.father;
                }

                return tmp;

            }
        }
    }

     */

}
