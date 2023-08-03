import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class J_12891 {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int[] limit = new int[ 4 ];
    //    static char[] alphabets = {'A', 'C', 'G', 'T'}; 제발 순서 헷갈리지마
    static int ans = 0;
    static String dna;
    static int s, p;
    static int[][] prefix_sum;

    static HashMap<Character, Integer> map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub


        /**
         * Input
         */
        token = new StringTokenizer(bf.readLine());
        s = Integer.parseInt(token.nextToken());
        p = Integer.parseInt(token.nextToken());
        dna = bf.readLine();
        token = new StringTokenizer(bf.readLine());
//        prefix_sum = new int[s + 1][4];


        for (int i = 0; i < 4; i++) {
            limit[i] = Integer.parseInt(token.nextToken());
        }
        map.put('A', 0);
        map.put('C', 1);
        map.put('G', 2);
        map.put('T', 3);
        /**
         * -------------------
         */

        /*
         * logic 2
         */
        /*


        for (int i = 0; i < s; i++) {
            int idx = map.get( dna.charAt(i) );
            for (int j = 0; j < 4; j++) {
                prefix_sum[i + 1][j] = prefix_sum[i][j];
            }

            prefix_sum[i + 1][idx] = prefix_sum[i][idx] + 1;
        }

        for (int i = 0; i < s; i++) {

            if (i + p > s) {
                break;
            }
            int[] field = getACGTbyIdx(prefix_sum[i], prefix_sum[i + p]);
            if (isRight(field)) {

                ans += 1;
            }
        }

         */
        /**
         * logic 3 start
         */
        int[] field = new int[ 4 ];
        //먼저 p길이 까지 미리 계산하기.
        for( int i = 0; i < p; i ++ ){
            field[ map.get( dna.charAt( i ) ) ] += 1;
        }
        //가능?
        if( isRight( field ) ){
            ans += 1;
        }
        //나머지도 돌아보자
        for( int i = p; i < s; i ++ ){
            field[ map.get( dna.charAt( i - p ) ) ] -= 1;
            field[ map.get( dna.charAt( i ) ) ] += 1;
            //가능?
            if( isRight( field ) ){
                ans += 1;
            }
        }
        System.out.println(ans);


    }

    static int[] getACGTbyIdx(int[] start, int[] end) {
        int[] temp = new int[4];

        for (int i = 0; i < 4; i++) {
            temp[i] = end[i] - start[i];
        }
        return temp;
    }

    static boolean isRight(int[] fields) {
        for (int i = 0; i < 4; i++) {
            //불가능
            if (fields[i] < limit[i]) {
                return false;
            }
        }
        //가능
        return true;
    }
}