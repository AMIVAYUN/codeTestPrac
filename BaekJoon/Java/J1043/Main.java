package J1043;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n, m;
    static boolean[] people;
    static ArrayList<Integer>[] parties;
    static int Mx = 0;

    static int[] parents;
    static boolean[][] visited;

    static ArrayList<Integer> known = new ArrayList<>();



    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());
        visited = new boolean[ m ][ n + 1 ];
        token = new StringTokenizer( bf.readLine() );
        int num = Integer.parseInt( token.nextToken() );
        people = new boolean[ n + 1 ];
        for( int i = 0; i < num; i ++){
            int idx = Integer.parseInt(token.nextToken() );
            people[ idx ] = true;
            known.add( idx );
        }
        parents = new int[ n + 1 ];
        for( int i = 0; i < n + 1; i ++ ){
            parents[ i ] = i;
        }

        parties = new ArrayList[ m ];
        for( int i = 0; i < m; i++ ){
            parties[ i ] = new ArrayList<>();
        }
        for( int i = 0; i < m; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            num = Integer.parseInt( token.nextToken());
            for( int j = 0; j < num; j ++ ){
                parties[ i ].add( Integer.parseInt( token.nextToken() ) );
            }
        }

//        for( int i = 1; i < n + 1 ; i ++){
//            if( people[ i ] ){
//                for( int j = 1; j < n + 1; j ++ ){
//                    if( people[ j ] ){
//                        union( i , j );
//                    }
//                }
//            }
//
//        }


        for( int i = 0; i < m; i ++ ){
            int start = parties[ i ].get( 0 );
            for( int person : parties[ i ] ){

                union( start, person );

            }
        }



        for( int i = 0; i < m; i ++ ){
            boolean flag = false;
            outer: for( int person : parties[ i ] ){
                for( int know : known ){
                    if( find( person ) == find( know ) ){
                        flag = true;
                        break outer;
                    }
                }
            }

            if( !flag ){
                Mx++;
            }

        }

//        for( int i = 0; i < n + 1; i ++ ){
//            System.out.println( i + " " + parents[ i ]);
//
//        }
//        System.out.println( Arrays.toString( people) );
        System.out.println(Mx);

    }
    // 긾이 우선으로 가니깐 조건문 조건이 너무 타이트하다.
    //# sol 2d arr와 1차원 boolean 반례 통과가 안됨. 집합으로 풀어보자
    private static void sol1( int depth, int cnt ) {
//        System.out.println( depth );
        System.out.println( "Depth: " + depth + " cnt : " + cnt );
        if( depth == m ){
            Mx = Math.max( cnt, Mx );
            return;
        }

        if( depth > 1 && Mx - ( cnt + ( m - depth ) ) > 0 ){
            return;
        }
        /*
            1 1
            1 2
            1 3
            1 4
            2 4 1

         */
        for( int i = 0; i < parties[ depth ].size(); i++ ){

            int person = parties[depth].get( i );
            if( people[ person ] ){
                for( int t : parties[ depth ] ){
                    if( people[ t ] ) continue;
                    for( int j = 0; j < depth; j ++ ){
                        if( visited[ j ][ t ] && !people[ t ] ){
                            return;
                        }
                    }
                }
                fill( depth , true );
                for( int know : parties[depth] ){
                    people[ know ] = true;
                }
                sol1( depth + 1, cnt );
                fill( depth, false );
                return;
            }
        }

        fill( depth,true );
        sol1( depth + 1, cnt + 1 );
        sol1( depth + 1, cnt );
        fill( depth, false );



    }

    public static void fill( int depth, boolean val ){
        for( int i = 0; i < parties[ depth ].size(); i++ ) {
            int person = parties[depth].get(i);
            visited[ depth ][ person ] = val;
        }

    }

    public static int find( int x ){
        if( parents[ x ] != x ){
            parents[ x ] = find( parents[ x ] );
        }
        return parents[ x ];
    }

    public static void union( int x, int y ){
        int fx = find( x ), fy = find( y );
        if( fx > fy ){
            parents[ fx ] = fy;
        }else{
            parents[ fy ] = fx;
        }
    }

}