package PM.nplus1_카드게임;

import java.util.*;
class Solution {
    /** 재귀를 타면 터질 것이 분명하다 -> 카드수 최대 1000개
     잘 보면 두장을 내는 것이 조건이기에 두장 기준으로 해시맵으로 필요한 카드들을 저장해두면 될 것이다.

     멀리 간다? 최대한 코인을 적게써야 최대한 많은 카드를 볼 수 있다.

     deque에 모든 경우의 수를 담는다면, hashmap도 2**1000개 경우로 담기에 무리가 있다.

     일단은 단순 그리디로
     1. 최대한 코인을 적게 쓰자.
     2. 이 규칙대로 짜보자.
     - 1의 규칙에 맞춰 기존 카드로 내고 넘어갈 수 있나?
     - 코인을 한개쓰고 넘어갈 수 있나?
     - 코인을 두개쓰고 넘어갈 수 있나?

     -- 버리면서 가면 최대로 못간다 모든 카드를 다 집어 넣되 뺄 때 코인을 경감하는게 맞았다.
     */
    int n,coin,pair;
    HashMap< Integer, Boolean > map;
    HashMap< Integer, Boolean > add;
    public int solution(int coin, int[] cards) {
        int answer = 1;
        n = cards.length;
        map = new HashMap<>();
        add = new HashMap<>();
        this.coin = coin;
        this.pair = 0;
        int start = n / 3;

        for( int i = 0; i < start; i ++ ){
            int card = cards[ i ];
            map.put( card, true );
        }
        for( int card: map.keySet() ){
            if( map.containsKey( n + 1 - card ) ){
                pair++;
            }
        }
        pair /= 2;
        for( int i = start; i < n; i += 2 ){
            int newCard1 = cards[ i ];
            int newCard2 = cards[ i + 1 ];
            checkCard( newCard1 );
            checkCard( newCard2 );
            // System.out.println( newCard1 + ", " + newCard2 + " , coin= " + this.coin );
            // System.out.println( map.toString() + "//" + add.toString() );
            if( pair < 1 && this.coin > 1 ){
                int target = -1;
                for( int card: add.keySet() ){
                    if( add.containsKey( n + 1 - card ) ){
                        pair++;
                        this.coin -= 2;
                        target = card;
                        break;
                    }
                }

                if( target != -1 ){
                    add.remove( target );
                    add.remove( n + 1 - target );
                }
            }
            if( pair < 1 ){
                break;
            }

            answer++;
            pair--;
        }

        return answer;
    }

    public void checkCard( int card ){
        if( this.coin > 0 && map.containsKey( n + 1 - card ) ){
            this.coin--;
            pair++;
            return;
        }
        add.put( card, true );
    }

}