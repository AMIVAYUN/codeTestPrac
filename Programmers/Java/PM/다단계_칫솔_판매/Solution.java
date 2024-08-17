package PM.다단계_칫솔_판매;

import java.util.*;
class Solution {
    /**

     모든 판매원은 자신이 칫솔 판매에서 발생한 이익 뿐만 아니라, 자신이 조직에 추천하여 가입시킨 판매원에게서 발생하는 이익의 10% 까지 자신에 이익이 됩니다.
     => 즉 루트는 맨 마지막 피연산자가 되거나 memoization을 활용해야 될까?

     유니온 파인드를 활용해도 괜찮을 것 같다

     1. 차수로 위상 정렬을 하든 계수를 직접 구하든 하여 각 계층 별로 아래부터 연산을 실시해서 최신화 시킨다.
     2. 아래 부터 연산해서 누적한다.

     enroll이 10000 이하이면 그냥 위 로직대로 돌려도 문제가 없을 것 같다.

     단 seller가 10만 이기에 seller를 먼저 전처리하여 enroll 길이 만큼 가지고 있자.
     => 안된다. 1원 미만 이득 분배를 하지 않는다.

     1원 미만 이득 분배 x

     사람 이름이 겹치나? -> 안 적혀있다. 일단 진행시켜.
     */

    int[] parents;
    Node[] nodes;
    int n;
    int[] sells;
    HashMap< String, Integer > mapper = new HashMap<>();
    int[] answer;
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {


        mapper.put( "-", 0 );
        int idx = 1;
        n = enroll.length + 1;
        nodes = new Node[ n ];
        nodes[ 0 ] = new Node( "-" );
        parents = new int[ n ];
        parents[ 0 ] = -1;
        sells = new int[ n ];
        answer= new int[ n - 1 ];

        for( String name: enroll ){
            mapper.put( name, idx );
            nodes[ idx++ ] = new Node( name );
        }

        //집합 관계 정리
        //가능한 이유: 즉, 어느 판매원의 이름이 enroll 의 i 번째에 등장한다면, 이 판매원을 조직에 참여시킨 사람의 이름, 즉 referral 의 i 번째 원소는 이미 배열 enroll 의 j 번째 (j < i) 에 등장했음이 보장됩니다.
        idx = 1;
        for( String refer : referral ){

            int refIdx = mapper.get( refer );
            parents[ idx ] = refIdx;
            nodes[ idx ].level = nodes[ parents[ idx++ ] ].level + 1;
        }
        idx = 0;

        for( String sell : seller ){
            int sellIdx = mapper.get( sell );
            calculateSell( sellIdx, nodes[ sellIdx ], amount[ idx++ ] * 100 );
            // sells[ sellIdx ] += amount[ idx++ ] * 100;
        }

//         Arrays.sort( nodes, ( n1, n2 ) -> Integer.compare( n1.level, n2.level ) );

//         for( Node person: nodes ){
//             int pIdx = mapper.get( person.name );
//             calculateSell( pIdx, person );
//         }

        return answer;
    }

    public void calculateSell( int idx, Node person, int sellAmount ){
        // int sellAmount = sells[ idx ];
        // System.out.println( person.name + " // sell = " + sells[ idx ] );
        while( sellAmount > 0 && idx != 0 ){
            int upper = sellAmount / 10;
            answer[ idx - 1 ] += sellAmount - upper;

            idx = parents[ idx ];
            sellAmount = upper;

        }
    }

    public class Node{
        int level;
        String name;

        public Node( String name ){
            this.level = 0;
            this.name = name;
        }
    }
}