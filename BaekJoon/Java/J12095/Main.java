package J12095;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {

        token = new StringTokenizer( bf.readLine() );

        int N = Integer.parseInt(token.nextToken());
        int M = Integer.parseInt(token.nextToken());

        int[] arr = new int[N];
        token = new StringTokenizer( bf.readLine() );
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }

        int result = search(arr, N, M);
        System.out.println(result);
    }


    // 탐색
    static int search(int[] arr, int N, int M) {
        int result = 0;


        for (int i = 0; i < N - 2; i++) {


            for (int j = i + 1; j < N - 1; j++) {


                for (int k = j + 1; k < N; k++) {

                    int temp = arr[i] + arr[j] + arr[k];


                    if (M == temp) {
                        return temp;
                    }

                    if(result < temp && temp < M) {
                        result = temp;
                    }
                }
            }
        }

        return result;
    }
}
