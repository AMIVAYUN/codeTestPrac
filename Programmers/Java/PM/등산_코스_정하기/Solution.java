package PM.등산_코스_정하기;

import java.util.*;
class Solution {
    /**

     다익스트라 혹은 dfs를 조금 변형하면 될 것.

     노드의 구분 -> 산봉우리, 휴식처, 출입구.

     간선의 최대 value -> 넘어가면 안됨.

     n -> 50000 

     간선은 20만.

     w가 천만이나 증가하지 않기에 int로 연산한다.

     제공해야 하는 결과가 산봉우리 + intesity이므로 다익스트라를 먼저 변형해보자.

     한번에 가려고 하니 로직 처리가 안된다. 가는거 오는거 짤라서 하면 될듯 하다.

     climbup + down -> 시간 + 메모리 초과.

     생각해보니 차피 올라가는 것을 구했으면 내려오는건 똑같다.

     메모리 초과 해결.

     중요한 것? 음 gate for문은 없어도 된다?

     차피 중요한 것은 봉우리에 싸게 가는 법.

     답도 봉우리만 원한다.

     */
    // Operand Mn = new Operand( -1, Integer.MAX_VALUE );
    // Operand MnGo = new Operand( -1, Integer.MAX_VALUE, -1 );
    // Operand MnBack = new Operand( -1, Integer.MAX_VALUE, -1 );
    int answerGate = 0;

    int[] gates;
    boolean[] isGate;
    boolean[] isTop;
    int n;
    HashMap< Integer, HashMap< Integer, Integer > > map = new HashMap<>();
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        int[] answer = new int[]{ Integer.MAX_VALUE, Integer.MAX_VALUE };

        this.gates = gates;
        this.isGate = new boolean[ n + 1 ];
        this.isTop = new boolean[ n + 1 ];
        this.n = n;
        for( int gate: gates ){
            this.isGate[ gate ] = true;
        }
        for( int top: summits ){
            isTop[ top ] = true;
        }

        for( int i = 1; i < n + 1; i ++ ){
            HashMap< Integer, Integer > imap = new HashMap<>();
            map.put( i, imap );
        }

        for( int[] path: paths ){

            int x = path[ 0 ];
            int y = path[ 1 ];
            // System.out.println( x + " , " + y );
            int value = path[ 2 ];

            HashMap mapx = map.get( x );
            HashMap mapy = map.get( y );

            // System.out.println( x +  ", " + mapx );
            // System.out.println( y +  ", " + mapy );
            mapx.put( y, value );
            mapy.put( x, value );
        }


        //이걸 줄여보자
        //중요한 것? 음 gate for문은 없어도 된다?
//         for( int gate: gates){
//             int[] result = climbUp( gate );
//             for( int top: summits ){
//                 int subAnswer = result[ top ];
//                 // System.out.println( gate + "," + top + " = " + subAnswer );

//                 if( subAnswer < answer[ 1 ] ){

//                     answer[ 0 ] = top;
//                     answer[ 1 ] = subAnswer;
//                 }else if( subAnswer == answer[ 1 ] ){
//                     answer[ 0 ] = Math.min( answer[ 0 ], top );
//                 }
//             }


//         }


        // System.out.println( Mn );

        int[] result = climbUp2();

        for( int top: summits ){
            int subAnswer = result[ top ];


            if( subAnswer < answer[ 1 ] ){

                answer[ 0 ] = top;
                answer[ 1 ] = subAnswer;
            }else if( subAnswer == answer[ 1 ] ){
                answer[ 0 ] = Math.min( answer[ 0 ], top );
            }
        }

        return answer;
    }
    public int[] climbUp2(){
        int[] dists = new int[ n + 1 ];
        Arrays.fill( dists, Integer.MAX_VALUE );



        PriorityQueue< int[] > pq = new PriorityQueue< int[] >( ( e1, e2 ) -> {
            if( e1[ 1 ] == e2[ 1 ] ) return Integer.compare( e1[ 0 ], e2[ 0 ] );
            return Integer.compare(  e1[ 1 ], e2[ 1 ] );
        });


        for( int gate: gates ){
            dists[ gate ] = 0;
            pq.add( new int[]{ gate, 0 } );
        }

        while( !pq.isEmpty() ){
            int[] now = pq.poll();

            if( now[ 1 ] > dists[ now[ 0 ] ] ) continue;
            dists[ now[ 0 ] ] = now[ 1 ];
            HashMap< Integer, Integer > vertexes = map.get( now[ 0 ] );

            for( int next: vertexes.keySet() ){
                int nextValue = Math.max( vertexes.get( next ), now[ 1 ] );
                if( !isGate[ next ] && dists[ next ] > nextValue ){
                    if( isTop[ next ] ){
                        dists[ next ] = nextValue;
                        continue;
                    }
                    dists[ next ] = nextValue;
                    int[] nextPos = new int[]{ next, nextValue };
                    pq.add( nextPos );
                }
            }
        }

        return dists;

    }

    public int[] climbUp( int start ){
        int[] dists = new int[ n + 1 ];
        Arrays.fill( dists, Integer.MAX_VALUE );

        PriorityQueue< int[] > pq = new PriorityQueue< int[] >( ( e1, e2 ) -> {
            if( e1[ 1 ] == e2[ 1 ] ) return Integer.compare( e1[ 0 ], e2[ 0 ] );
            return Integer.compare(  e1[ 1 ], e2[ 1 ] );
        });

        dists[ start ] = 0;

        for( int next: map.get( start ).keySet() ){
            if( !isGate[ next ] ) pq.add( new int[]{ next, map.get( start ).get( next ) } );
        }

        while( !pq.isEmpty() ){
            int[] now = pq.poll();

            if( now[ 1 ] > dists[ now[ 0 ] ] ) continue;
            dists[ now[ 0 ] ] = now[ 1 ];
            HashMap< Integer, Integer > vertexes = map.get( now[ 0 ] );

            for( int next: vertexes.keySet() ){
                int nextValue = Math.max( vertexes.get( next ), now[ 1 ] );
                if( !isGate[ next ] && dists[ next ] > nextValue ){
                    if( isTop[ next ] ){
                        dists[ next ] = nextValue;
                        continue;
                    }
                    dists[ next ] = nextValue;
                    int[] nextPos = new int[]{ next, nextValue };
                    pq.add( nextPos );
                }
            }
        }

        return dists;

    }

    public int[] climbDown( int start ){

        int[] dists = new int[ n + 1 ];
        Arrays.fill( dists, Integer.MAX_VALUE );

        PriorityQueue< int[] > pq = new PriorityQueue< int[] >( ( e1, e2 ) -> {
            if( e1[ 1 ] == e2[ 1 ] ) return Integer.compare( e1[ 0 ], e2[ 0 ] );
            return Integer.compare( e1[ 1 ], e2[ 1 ] );
        });

        dists[ start ] = 0;

        for( int next: map.get( start ).keySet() ){
            if( !isTop[ next ] ) pq.add( new int[]{ next, map.get( start ).get( next ) } );
        }

        while( !pq.isEmpty() ){
            int[] now = pq.poll();

            if( now[ 1 ] > dists[ now[ 0 ] ] ) continue;
            dists[ now[ 0 ] ] = now[ 1 ];
            HashMap< Integer, Integer > vertexes = map.get( now[ 0 ] );

            for( int next: vertexes.keySet() ){
                int nextValue = Math.max( vertexes.get( next ), now[ 1 ] );
                if( !isTop[ next ] && dists[ next ] > nextValue ){
                    if( isGate[ next ] ){
                        dists[ next ] = nextValue;
                        continue;
                    }
                    dists[ next ] = nextValue;
                    int[] nextPos = new int[]{ next, nextValue };
                    pq.add( nextPos );
                }
            }
        }

        return dists;
    }

//     public void findMn( int gate ){
//         /**
//             가는 조건
//             1. 게이트가 아니다.
//             2. 가중치가 Mn보다 낮다면 넘긴다.
//             3. 만약 산봉우리를 찍었다면 더이상 가지 않는다. 단 도착한 산봉우리는 가지고 있는다.
//             4. gate는 가지 않는다.
//         **/

//         PriorityQueue< Operand > pq = new PriorityQueue<>( ( o1, o2 ) -> {
//             if( o1.minCost == o2.minCost ){
//                 return Integer.compare( o1.top, o2.top );
//             }

//             return Integer.compare( o1.minCost, o2.minCost );
//         });
//         for( int next: map.get( gate ).keySet() ){
//             pq.add( new Operand( next, map.get( gate ).get( next ) ) );
//         }

//         while( !pq.isEmpty() ){
//             Operand op = pq.poll();

//             if( op.minCost > Mn.minCost ){
//                 continue;
//             }else if( op.minCost == Mn.minCost ){
//                 if( op.top < Mn.top ){
//                     Mn = op;
//                     continue;
//                 }
//             }
//             if( op.pos == gate && op.top != Integer.MAX_VALUE ){
//                 Mn = op;
//                 continue;
//             }
//             HashMap< Integer, Integer > vertexes = map.get( op.pos );

//             for( int next: vertexes.keySet() ){
//                 if( ( next == gate || !isGate[ next ] ) && vertexes.get( next ) <= Mn.minCost ){
//                     if( op.top != Integer.MAX_VALUE ){
//                         if( isTop[ next ] ) continue;
//                     }
//                     Operand nextOp = new Operand( next, vertexes.get( next ) );
//                     if( isTop[ next ] ){
//                         nextOp.top = next;
//                     }
//                     pq.add( nextOp );
//                 }
//             }
//         }

//     }

//     public class Operand{
//         int top = Integer.MAX_VALUE;
//         int minCost;
//         int pos;
//         int prev;

//         public Operand( int pos, int minCost, int prev ){
//             this.pos = pos;
//             this.minCost = minCost;
//             this.prev = prev;
//         }

//         public String toString(){
//             return this.top  + "," + this.minCost + "," + pos;
//         }
//     }
}