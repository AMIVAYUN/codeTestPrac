package PM.길_찾기_게임;

import java.util.*;
class Solution {
    /**

     1회전 -> 레벨 별 정리 및 root 찾기.
     이진 트리 -> 그냥 트리 아님 -> 즉 2 n제곱 형태로 늘어남
     항상 구성할 수 있는 트리만 주어짐.

     좌표값은 100000

     */
    int treeDepth, n, len[]; Node[] nodes;
    int[][] answer;
    ArrayList<Integer> pre = new ArrayList<>(),post = new ArrayList<>();
    public int[][] solution(int[][] nodeinfo) {

        HashSet<Integer> set = new HashSet<>();
        n = nodeinfo.length;
        answer = new int[ 2 ][ n ];
        nodes = new Node[ n ];
        for( int i = 0; i < n; i ++ ){
            nodes[ i ] = new Node( nodeinfo[ i ][ 0 ], nodeinfo[ i ][ 1 ] );
            nodes[ i ].idx = i+1;
            set.add( nodeinfo[ i ][ 1 ] );
        }

        Arrays.sort( nodes, ( n1, n2 ) -> {
            if( n1.y == n2.y ){
                return Integer.compare( n1.x, n2.x );
            }
            return Integer.compare( n2.y, n1.y );
        });

        int rootIdx = 0, idx = 0;



        treeDepth = set.size();
        len = new int[ treeDepth ];

        int treeIdx = 0;
        int levelIdx = 0;
        for( int i = 0; i < treeDepth; i ++ ){
            int level = nodes[ treeIdx ].y;
            // ArrayList<Node>levelNode = new ArrayList<>();
            int cnt = 0;
            while( treeIdx < n && level == nodes[ treeIdx ].y ){
                // levelNode.add( nodes[ treeIdx ] );
                nodes[ treeIdx++ ].level = levelIdx;

                cnt++;

            }
            levelIdx++;
            len[ i ] = cnt;
            if( i > 0 ) len[ i ] += len[ i - 1 ]; // prefix로 각 레벨 별 구간을 정의. 각 레벨 별 가능한 경우에 맞추어 진행


//             len[ i ] = levelNode.size();
//             len[ i ] += len[ i - 1 ]; // prefix로 각 레벨 별 구간을 정의. 각 레벨 별 가능한 경우에 맞추어 진행
//             System.out.println(" previous : " );

//             for( int j = i - 2 < 0 ? 0 : len[ i - 2 ]; j < len[ i - 1 ]; j ++ ){
//                 // System.out.println( nodes[ j ] );
//             }

            // System.out.println( levelNode.toString() );
        }

        dfs( 1 );

        nodes[ 0 ].preOrder();
        nodes[ 0 ].postOrder();

        // System.out.println( pre.toString() + " // " + post.toString() );
        idx = 0;
        for( int i : pre ){
            answer[ 0 ][ idx++ ] = i;
        }
        idx = 0;
        for( int i : post ){
            answer[ 1 ][ idx++ ] = i;
        }
        return answer;
    }

    public boolean dfs( int depth ){
        if( depth == n ){
            return true;
        }
        Node now = nodes[ depth ];
        for( int i = now.level - 2 < 0 ? 0 : len[ now.level - 2 ]; i < len[ now.level - 1 ]; i ++ ){
            if( nodes[ i ].lt == null && nodes[ i ].x > nodes[ depth ].x && canBe( depth, i ) ){
                nodes[ i ].lt = nodes[ depth ];
                nodes[ depth ].parent = nodes[ i ];
                nodes[ depth ].dir = 0;

                boolean result = dfs( depth + 1 );
                if( result ) return true; // 원피스를 찾았다는 것.

                nodes[ depth ].parent = null;
                nodes[ depth ].dir = -1;
                nodes[ i ].lt = null;
            }

            if( nodes[ i ].rt == null && nodes[ i ].x < nodes[ depth ].x &&canBe( depth, i )){
                nodes[ i ].rt = nodes[ depth ];
                nodes[ depth ].parent = nodes[ i ];
                nodes[ depth ].dir = 1;

                boolean result = dfs( depth + 1 );
                if( result ) return true;

                nodes[ depth ].dir = -1;
                nodes[ depth ].parent = null;
                nodes[ i ].rt = null;

            }
        }

        return false;


    }

    public boolean canLeft( int depth, int i ){
        Node pos = nodes[ depth ];
        Node target = nodes[ i ];
        while( pos != null && pos.level != 0 && pos.dir != 1 ){
            if( pos.x > target.x ){
                return false;
            }
            pos = pos.parent;
        }

        return true;
    }
    public boolean canBe( int depth, int i ){
        Node target = nodes[ depth ];
        Node pos = nodes[ i ];


        while( pos.level != 0 ){

            if( pos.dir == 0 ){
                if( pos.parent.x < target.x ) return false;
            }else if( pos.dir == 1 ){
                if( pos.parent.x > target.x ) return false;
            }

            pos = pos.parent;
        }

        return true;
    }
    class Node{
        int x;
        int y;
        int level = -1;
        int idx = -1;
        int dir = -1;

        Node lt, rt, parent;

        public Node( int x, int y ){
            this.x = x;
            this.y = y;

        }
        public String toString(){
            String base = "idx = "+ this.idx +" [x = " + this.x + ", y = " + this.y + " level = " + this.level + /*" Mxx = " + Mxx +" Mnx = " + Mnx +*/ "dir = " + dir + " ]\n";
            String append = "";
            if( this.lt != null ){
                append += " lt = [ " + this.lt.idx +" ]\n";
            }
            if( this.rt != null ){
                append += " rt = [ " + this.rt.idx +" ]\n";
            }

            return base + append;
        }


        public void preOrder(){
            pre.add( this.idx );
            if( this.lt != null ){
                this.lt.preOrder();
            }
            if( this.rt != null ){
                this.rt.preOrder();
            }
        }

        public void postOrder(){

            if( this.lt != null ){
                this.lt.postOrder();
            }
            if( this.rt != null ){
                this.rt.postOrder();
            }

            post.add( this.idx );
        }
    }



}
