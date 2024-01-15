package J1012;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int cnt;
    static BufferedReader bf = new BufferedReader( new InputStreamReader( System.in ) );
    static StringTokenizer token;


    public static void main(String[] args) throws IOException {


        int T = Integer.parseInt( bf.readLine() );

        for (int i = 0; i < T; i++) {
            token = new StringTokenizer( bf.readLine() );
            int M = Integer.parseInt(token.nextToken());
            int N = Integer.parseInt(token.nextToken());
            int K = Integer.parseInt(token.nextToken());

            int[][] Area = new int[N][M];

            for (int j = 0; j < K; j++) {
                token = new StringTokenizer( bf.readLine() );
                int m = Integer.parseInt(token.nextToken());
                int n = Integer.parseInt(token.nextToken());
                Area[n][m] = 1;
            }

            cnt = 0;

            for (int m_ = 0; m_ < M; m_++) {
                for (int n_ = 0; n_ < N; n_++) {
                    if (dfs(Area, m_, n_)) {
                        cnt++;
                    }
                }
            }

            System.out.println(cnt);
        }
    }

    static boolean dfs(int[][] Area, int m, int n) {
        int Mx = Area[0].length;
        int Mn = Area.length;

        if (m < 0 || n < 0 || m >= Mx || n >= Mn) {
            return false;
        }

        if (Area[n][m] == 0) {
            return false;
        }

        Area[n][m] = 0;

        for (int i = 0; i < 4; i++) {
            dfs(Area, m + dx[i], n + dy[i]);
        }

        return true;
    }
}