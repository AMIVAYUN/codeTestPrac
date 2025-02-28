
import java.util.*;
class Solution {
    /*

        1. 이모티콘 플러스 가입자 최대한 늘리기
        2. 이모티콘 판매액 최대한 늘리기

        1 목표가 우선, 2 목표가 그 다음.

        n명 에게 m개 할인 판매

        자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘 모두 구매
        이모티콘 구매 비용 합이 -> 일정 가격 이상 // 이모티콘 구매 취소 후 이모티콘 플러스에 가입.

        사용자 일정 비율 이상 전부 구매
        일정 가격 이상이 되면 이모티콘 플러스에 가입

        유저 1 100
        가격 100 10000000
        이모티콘 최대 7개

       아...
       할인율 10 20 30 40 중 하나

       단순 완탐이었던 것;

    */
    int[] answer;
    int dis[], users[][], emoticons[];
    public int[] solution(int[][] users, int[] emoticons) {
        answer = new int[ 2 ];
        this.dis = new int[ emoticons.length ];
        this.users = users;
        this.emoticons = emoticons;
        getPermutation( 0 );

        return answer;
    }

    public void getPermutation( int depth ){
        if( depth  == emoticons.length ){
            getResult();
            return;
        }

        for( int i = 1; i < 5; i ++ ){
            dis[ depth ] = i * 10;
            getPermutation( depth + 1 );
        }
    }

    public void getResult(){
        int sum = 0;
        int member = 0;
        for( int i = 0; i < users.length; i ++ ){
            int[] user = users[ i ];
            int indivSum = 0;
            int stan = user[ 0 ];
            int price = user[ 1 ];

            for( int j = 0; j < emoticons.length; j ++ ){
                if( dis[ j ] >= stan ){
                    indivSum += (( emoticons[ j ] / 100) * (100-dis[j]));
                }


            }

            if( indivSum >= price ){
                member++;

            }else{
                sum += indivSum;
            }

        }

        if( answer[ 0 ] < member ){
            answer[ 0 ] = member;
            answer[ 1 ] = sum;

        }else if( answer[ 0 ] == member ){
            if( answer[ 1 ] < sum ){
                answer[ 1 ] = sum;
            }
        }

    }
}