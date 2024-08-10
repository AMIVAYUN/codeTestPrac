package PM.퍼즐_조각_채우기;

import java.util.*;
class Solution {
    /**

     인접한 칸이 비어있으면 안된다 > 딱 맞는 퍼즐을 넣어야 한다.

     회전은 가능하다. 각 퍼즐을 회전한 경우까지 전부 상태를 가지고 있자.

     퍼즐을 어떻게 넣어야 이게 같은 퍼즐인지 알 수 있을까?

     25 * 25 -> 625개 * 4 = 2500개 한 퍼즐당 4개씩 빠진다.

     같은 모양이 있어도 한쪽에만 넣으면 된다. 왜냐? -> 차피 구멍이 같다면 채워지는 블록 개수는 같다.

     그러면 각 blank에 대해서 전체 갯수도 갖고 있자. -> 그래야 적어도 불 필요한 탐색을 줄인다.

     0,0을 기준으로 각 좌표들에 대한 값을 갖자.

     */
    int n, m;
    ArrayList<Puzzle> blanks;
    ArrayList<Puzzle> puzzles;
    boolean[][] visit;
    int[] dx = { -1 , 1, 0, 0 }, dy = { 0, 0, -1, 1 };
    int[][] rotate = { { 0, 1 }, { 1, 1 }, { 1, 0 }, { 1, -1 }, { 0, -1 }, { -1, -1 }, { -1, 0 }, { -1, 1 } };
    boolean[] fill;
    int[][] game_board, table;
    public int solution(int[][] game_board, int[][] table) {
        int answer = -1;
        n = game_board.length;
        this.game_board = game_board;
        this.table = table;
        puzzles = new ArrayList<>();
        blanks = new ArrayList<>();
        visit = new boolean[ n ][ n ];

        for( int x = 0; x < n; x ++ ){
            for( int y = 0; y < n; y ++ ){
                if( game_board[ x ][ y ] == 0 && !visit[ x ][ y ] ){
                    visit[ x ][ y ] = true;
                    findPuzzle( x, y, 0 );
                }
            }
        }

        // for( Puzzle p : blanks ){
        //     System.out.println( p.toString() );
        // }

        fill = new boolean[ blanks.size() ];
        // System.out.println("--");
        visit = new boolean[ n ][ n ];


        for( int x = 0; x < n; x ++ ){
            for( int y = 0; y < n; y ++ ){
                if( table[ x ][ y ] == 1 && !visit[ x ][ y ] ){
                    visit[ x ][ y ] = true;
                    findPuzzle( x, y, 1 );
                }
            }
        }

//         for( Puzzle p : puzzles ){
//             System.out.println( p.toString() );
//         }
//         if( puzzles.size() >= 3 ) {
//             for( int i = 0; i < 4; i ++ ){
//             Puzzle p = puzzles.get( 2 );

//             System.out.println( "puzzle " + p.toString() );
//             System.out.println( "blanks " + blanks.get( 3 ) );

//             rotate( p.lst );
//         }
//         }


        int cnt = 0;
        for( Puzzle p : puzzles ){
            for( int i = 0; i < blanks.size(); i ++ ){
                if( fill[ i ] ) continue;

                if( blanks.get( i ).cnt == p.cnt ){
                    if( canBe( p, blanks.get( i ) ) ){
                        // System.out.println(" Matched!!! " + p.toString() + " == " + blanks.get( i ) );
                        fill[ i ] = true;
                        cnt += p.cnt;
                        break;
                    }
                }
            }
        }

        return cnt;
    }

    public boolean canBe( Puzzle p, Puzzle b ){

        int diff = 0;
        ArrayList<int[]> lst = p.lst;
        while( diff < 4 ){
            boolean isMatch = true;
            for( int i = 0; i < lst.size(); i ++ ){
                int[] ppos = lst.get( i );
                int[] bpos = b.lst.get( i );

                if( ppos[ 0 ] != bpos[ 0 ] || ppos[ 1 ] != bpos[ 1 ] ){
                    isMatch = false;
                    break;
                }
            }
            if( isMatch ){
                return true;
            }else{
                rotate( lst );
                diff++;
            }

        }


        return false;

    }

    public void findPuzzle( int sx, int sy, int block ){
        int cnt = 0;
        ArrayList< int[] > lst = new ArrayList<>();
        ArrayDeque< int[] > dq = new ArrayDeque<>();
        dq.add( new int[]{ sx, sy } );

        lst.add( new int[]{ 0, 0 } );
        while( !dq.isEmpty() ){
            int[] pos = dq.poll();
            cnt ++;
            int x = pos[ 0 ], y = pos[ 1 ];


            for( int i = 0; i < 4; i ++ ){
                int nx = x + dx[ i ];
                int ny = y + dy[ i ];

                if( isRight( nx, ny ) ){
                    if( block == 0 ){
                        if( game_board[ nx ][ ny ] == block && !visit[ nx ][ ny ] ){
                            visit[ nx ][ ny ] = true;
                            dq.add( new int[]{ nx, ny } );
                            lst.add( new int[]{ nx - sx, ny - sy } );
                        }
                    }else{
                        if( table[ nx ][ ny ] == block && !visit[ nx ][ ny ] ){
                            visit[ nx ][ ny ] = true;
                            dq.add( new int[]{ nx, ny } );
                            lst.add( new int[]{ nx - sx, ny - sy } );
                        }
                    }

                }
            }
        }

        padding( lst );


        if( block == 0 ){

            Puzzle puzzle = new Puzzle( cnt, lst );
            blanks.add( puzzle );
        }else{
            Puzzle puzzle = new Puzzle( cnt, lst );
            puzzles.add( puzzle );
        }

        return;
    }
    public void padding( ArrayList<int[]> lst ){

        Collections.sort( lst, ( p1, p2 ) -> {
            if( p1[ 1 ] == p2[ 1 ] ){
                return Integer.compare( p1[ 0 ], p2[ 0 ] );
            }
            return Integer.compare( p1[ 1 ], p2[ 1 ] );
        } );

        int[] first = lst.get( 0 );
        if( first[ 0 ] != 0 || first[ 1 ] != 0 ){
            // System.out.println(" needs to sort " );
            // for( int i = 0; i < lst.size(); i ++ ){
            //     System.out.print( Arrays.toString( lst.get( i ) ) + " " );
            // }
            for( int i = 1; i < lst.size(); i ++ ){
                int[] pos = lst.get( i );
                pos[ 0 ] -= first[ 0 ];
                pos[ 1 ] -= first[ 1 ];
            }
            first[ 0 ] = 0; first[ 1 ] = 0;
            Collections.sort( lst, ( p1, p2 ) -> {
                if( p1[ 1 ] == p2[ 1 ] ){
                    return Integer.compare( p1[ 0 ], p2[ 0 ] );
                }
                return Integer.compare( p1[ 1 ], p2[ 1 ] );
            } );
        }

    }

    public void rotate( ArrayList<int[]> lst ){
        for( int i = 0; i < lst.size(); i ++ ){
            int[] pos = lst.get( i );
            int temp = pos[ 0 ] * -1;
            pos[ 0 ] = pos[ 1 ];
            pos[ 1 ] = temp;
        }

        padding( lst );
    }

    public boolean isRight( int x, int y ){
        return x >= 0 && x < n && y >= 0 && y < n;
    }

    public class Puzzle{
        int cnt;
        ArrayList< int[] > lst;

        public Puzzle( int cnt, ArrayList< int[] > lst ){
            this.cnt = cnt;
            this.lst = lst;
        }

        public String toString(){
            String str = "";
            for( int[] pos : lst ){
                str += Arrays.toString( pos ) + " ";
            }

            return "puzzle = [ " + cnt +" , " + str + " ]";
        }
    }
}