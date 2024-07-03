package PM.붕대감기;

import java.io.*;
class Solution {
    //t초동안 붕대를 감으면서 1초마다 x만큼 회복 t초 연속 회복시 y 추가 회복
    // 최대 체력을 넘길 순 없다.
    // 공격받으면 다시 붕대 감기 -> 0
    // 공격 받으면 정해진 피해량 만큼 체력이 줄어듦 0 이하가 되면 캐릭터 죽고 더이상 회복 ㅜㅂㄹ가

    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int max = health;
        int lead = 0;
        int idx = 0;
        while( answer <= attacks[ attacks.length - 1 ][ 0 ]){
            // System.out.println( answer + " :: hp = " + health + ",lead = " + lead );
            if( idx < attacks.length && attacks[ idx ][ 0 ] == answer ){
                lead = 0;
                health -= attacks[ idx ][ 1 ];
                idx ++;
                if( health <= 0){
                    return -1;
                }
                answer++;
                continue;
            }

            health += bandage[ 1 ];
            lead++;
            if( lead == bandage[ 0 ] ){
                health += bandage[ 2 ];
                lead = 0;
            }

            if( health > max ){
                health = max;
            }

            answer++;
        }

        return health;
    }
}