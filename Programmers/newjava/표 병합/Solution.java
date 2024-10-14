import java.util.*;
class Solution {
    /**
     유니온 파인드 근데 이차원을 곁들인
     */

    int n = 2500;
    int[] parents = new int[ n ];
    String[] graph = new String[ 2500 ];


    public String[] solution(String[] commands) {
        ArrayList< String> answer = new ArrayList<>();

        for( int i = 0; i < 2500; i ++ ){
            parents[ i ] = i;
        }
        for( String command: commands ){
            String[] cp = command.split( " " );

            if( cp[ 0 ].equals( "UPDATE") ){
                if( cp.length == 3 ){
                    String value1 = cp[ 1 ];
                    String value2 = cp[ 2 ];
                    updateValueByValue( value1, value2 );
                }else{
                    int x = Integer.parseInt( cp[ 1 ] ) - 1;
                    int y = Integer.parseInt( cp[ 2 ] ) - 1;
                    String value = cp[ 3 ];
                    updateValue( x, y, value );
                }
            }else if( cp[ 0 ].equals( "MERGE" ) ){
                int x1 = Integer.parseInt( cp[ 1 ] ) - 1;
                int y1 = Integer.parseInt( cp[ 2 ] ) - 1;
                int x2 = Integer.parseInt( cp[ 3 ] ) - 1;
                int y2 = Integer.parseInt( cp[ 4 ] ) - 1;
                merge( getIdx(x1, y1), getIdx(x2, y2) );
            }else if( cp[ 0 ].equals( "UNMERGE") ){
                int x = Integer.parseInt( cp[ 1 ] ) - 1;
                int y = Integer.parseInt( cp[ 2 ] ) - 1;
                unmerge( x, y );
            }else if( cp[ 0 ].equals( "PRINT" ) ){
                int x = Integer.parseInt( cp[ 1 ] ) - 1;
                int y = Integer.parseInt( cp [ 2 ] ) - 1;
                String value = print( x, y );
                answer.add( value );
            }
        }
        // System.out.println( Arrays.toString( parents ) );
        // System.out.println( Arrays.toString( graph ) );

        return answer.toArray( new String[ answer.size() ] );
    }

    public int getIdx( int x, int y ){
        return 50 * x + y;
    }
    public int[] getPos( int idx ){
        return new int[]{ idx / 50, idx % 50 };
    }

    public int find( int x ){
        if( parents[ x ] != x ){
            return find( parents[ x ] );
        }
        return x;
    }

    public void updateValue( int x, int y, String value ){
        int idx = getIdx( x, y );
        int px = find( idx );
        graph[ px ] = value;
    }

    public void updateValueByValue( String value1, String value2 ){
        if( value1.equals( value2 ) ) return;
        ArrayList<Integer> idxes = new ArrayList<>();
        for( int i = 0; i < 2500; i ++ ){
            int px = find( i );

            if( value1.equals( graph[ px ] ) ){
                idxes.add( px );
            }
        }

        for( int idx: idxes ){
            graph[ idx ] = value2;
        }

    }



    public void merge( int x, int y ){
        // System.out.println( "merge " + Arrays.toString( getPos(x) ) + " , " + Arrays.toString( getPos(y) ) );

        int px = find( x );
        int py = find( y );

        if( px == py ) return;

        String vx = graph[ px ];
        String vy = graph[ py ];


        if( vx == null ){
            //부모가 밸류가 없을 때
            if( vy != null ){

                graph[ py ] = null;
                graph[ px ] = vy;
            }
        }else{
            if( vy != null ){

                graph[ py ] = null;
            }
        }
        parents[ py ] = px;



    }

    public void unmerge( int x, int y ){

        int idx = getIdx( x, y );
        int px = find( idx );
        // System.out.println( "unmerge : " + x + ", " + y + " = " + graph[ px ] );
        List<Integer> lst = new ArrayList<>();
        for( int i = 0; i < 2500; i ++ ){
            int py = find( i );
            if( px == py ) lst.add( i );
        }

        for( int i: lst ){
            parents[ i ] = i;
        }

        String value = graph[ px ];
        if( value == null ) return;


        graph[ px ] = null;
        graph[ idx ] = value;


    }

    public String print( int x, int y ){
        int px = find( getIdx( x, y ) );
        return graph[ px ] != null ? graph[ px ] : "EMPTY";
    }

}