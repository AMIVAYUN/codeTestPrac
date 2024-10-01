import java.util.*;
import java.io.*;
class Solution{

    /**

     기둥과 보를 통한 벽면 구조물 세우기

     기둥 -> 바닥 위에 or 보의 한쪽 끝부분 or 다른 기둥위에

     보 -> 한쪽 끝이 기둥 위에 or 다른 보와 동시에 연결되어 있어야 됨.

     x, y, a, b
     -> x,y 설치 위치 좌표
     -> a 설치할 구조물 0 기둥 1 보
     -> b 0 삭제 1 설치

     기둥  삭제시 고려할 것 얘를 지우면 위의 보가 붕뜨는가? 이런 케이스
     ____
     | |

     보    삭제시 고려할 것 보를 지우면 누락되는 보가 생기는가? ( 좌 우로 )


     여기서 x,y는 도착 좌표다.


     */

    ArrayList< Build > lst = new ArrayList<>();
    boolean[][][] graph;
    int n;
    public int[][] solution(int n, int[][] build_frame) {
        int[][] answer = {};
        this.n = n;
        graph = new boolean[ n + 1 ][ n + 1 ][ 2 ];


        for( int[] frame : build_frame ){
            int x = frame[ 0 ];
            int y = frame[ 1 ];

            int type = frame[ 2 ];
            int isbuild = frame[ 3 ];


            if( isbuild == 0 ){
                delete( x, y, type );
            }else{
                build( x, y, type );
            }

        }

        Collections.sort( lst, ( e1, e2 ) -> {
            if( e1.x == e2.x ){
                if( e1.y == e2.y ){
                    return Integer.compare( e1.type, e2.type );
                }
                return Integer.compare( e1.y, e2.y );
            }

            return Integer.compare( e1.x, e2.x );
        });

        answer = new int[ lst.size() ][ 3 ];

        for( int i = 0; i < lst.size(); i ++ ){
            answer[ i ][ 0 ] = lst.get( i ).x;
            answer[ i ][ 1 ] = lst.get( i ).y;
            answer[ i ][ 2 ] = lst.get( i ).type;

        }
        return answer;
    }

    public void build( int x, int y, int type ){
        /**

         지을 때 요점

         기둥

         1. 공간이 비었다.

         2. 기둥을 짓는다 -> 아래가 바닥이다.

         3. x , y - 1에 보가 있다

         4. x , y - 1에 기둥이 있다.

         보

         1. 공간이 비었다.

         2. x - 1, y 이나 x + 1, y에 기둥이 있다.

         3. x - 1, y 과 x + 1, y에 보가 있다.

         */
        Build target = new Build( x, y, type );

        if( type == 0 ){

            if( graph[ x ][ y ][ 0 ] ){
                return;
            }

            if( isSatisfying0( x, y, type ) ){
                addBuild( target );
            }

        }else{
            if( graph[ x ][ y ][ 1 ] ){
                return;
            }

            if( isSatisfying1( x, y, type ) ){
                addBuild( target );
            }
        }



    }
    public boolean isSatisfying0( int x, int y, int type ){
        // System.out.println( x + ", " + y );
        if( y == n ) return false;

        if( y == 0 ){
            return true;
        }else if( ( y - 1 >= 0 && graph[ x ][ y - 1 ][ 0 ]) || ( x - 1 >= 0 && graph[ x - 1 ][ y ][ 1 ] ) || ( graph[ x ][ y ][ 1 ] )){
            return true;
        }

        return false;
    }

    public boolean isSatisfying1( int x, int y, int type ){
        // System.out.println( x + " , " + y + " , " + type );
        // 2 1 1
        if( y - 1 >= 0 ){
            if( graph [ x ][ y - 1 ][ 0 ] ){
                return true;
            }
        }

        if( x + 1 <= n && y - 1 >= 0 ){
            if( graph[ x + 1 ][ y - 1 ][ 0 ] ){
                return true;
            }
        }
        // System.out.println("because y + 1 1 " + x + " , " + y );        
        if( x - 1 >=0 && x + 1 <= n && graph[ x - 1 ][ y ][ 1 ] && graph[ x + 1 ][ y ][ 1 ] ){
            return true;
        }


        return false;
    }


    public void addBuild( Build build ){
        // ("Add " + build.x + " ," + build.y + ", type= " + build.type );
        lst.add( build );
        graph[ build.x ][ build.y ][ build.type ] = true;
    }

    public void delete( int x, int y, int type ){
        /**
         삭제시 고려할 점

         공통 있는가?

         기둥

         위에 있는 양 보가 조건을 만족하는지

         아래 있는 양 보가 조건을 만족하는지

         내 위에 있는 기둥이 조건을 만족하는지

         보

         내 머리 위에 있는 기둥이 조건을 만족하는지

         내 앞쪽 머리 위에 있는 기둥이 조건을 만족하는지

         내 양쪽 보가 조건을 만족하는지

         */
        Build target = new Build( x, y, type );
        if( !lst.contains( target ) ){
            return;
        }

        if( type == 0 ){
            graph[ x ][ y ][ type ] = false;
            if( canDelete0( x, y, type ) ){
                lst.remove( target );
                // System.out.println(" Delete 0: " + x + ", " + y );
                return;
            }else{
                // System.out.println("can not Delete 0: " + x + ", " + y );
                graph[ x ][ y ][ type ] = true;
            }
        }else{
            graph[ x ][ y ][ type ] = false;
            if( canDelete1( x, y, type ) ){
                lst.remove( target );
                // System.out.println(" Delete 1: " + x + ", " + y );
                return;
            }else{
                graph[ x ][ y ][ type ] = true;
            }
        }

    }

    public boolean canDelete0( int x, int y, int type ){
//         기둥

//                 위에 있는 양 보가 조건을 만족하는지

//                 내 위에 있는 기둥이 조건을 만족하는지
        if( y + 1 <= n && graph[ x ][ y + 1 ][ 1 ] ){
            if( !isSatisfying1( x, y + 1, 1 ) ){

                return false;
            }
        }

        if( x - 1 >= 0 && y + 1 <= n && graph[ x - 1 ][ y + 1 ][ 1 ] ){
            if( !isSatisfying1( x - 1, y + 1, 1 ) ){
                // System.out.println("because x - 1 y + 1 1");
                return false;
            }
        }

        if( y + 1 <= n && graph[ x ][ y + 1 ][ 0 ] ){
            if( !isSatisfying0( x, y + 1, 0 ) ){
                // System.out.println("because y + 1 0");
                return false;
            }
        }


        return true;

    }

    public boolean canDelete1( int x, int y, int type ){
        // System.out.println("hi im bo " + x + ", " + y );
//          보

//                 내 머리 위에 있는 기둥이 조건을 만족하는지

//                 내 앞쪽 머리 위에 있는 기둥이 조건을 만족하는지

//                 내 양쪽 보가 조건을 만족하는지

        if( graph[ x ][ y ][ 0 ] ){
            if( !isSatisfying0( x, y, 0 ) ){
                return false;
            }
        }

        if( x + 1 <= n && graph[ x + 1 ][ y ][ 0 ] ){
            if( !isSatisfying0( x + 1, y, 0 ) ){
                return false;
            }
        }

        if( x - 1 >= 0 && graph[ x - 1 ][ y ][ 1 ] ){
            if(!isSatisfying1( x - 1, y , 1 )){
                return false;
            }
        }

        if( x + 1 <= n && graph[ x + 1 ][ y ][ 1 ] ){
            if( !isSatisfying1( x + 1, y , 1 ) ){
                return false;
            }
        }


        return true;

    }

    public class Build {
        public int x;
        public int y;
        public int type;

        public Build(int x, int y, int type) {
            this.x = x;
            this.y = y;
            this.type = type;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) {
                return true;
            }
            if (obj == null || getClass() != obj.getClass()) {
                return false;
            }
            Build that = (Build) obj;
            return x == that.x && y == that.y && type == that.type;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y, type);
        }
    }

}