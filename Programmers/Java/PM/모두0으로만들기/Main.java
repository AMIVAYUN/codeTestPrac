package PM.모두0으로만들기;

public class Main {
    public static void main( String[] args ){
        Solution solution = new Solution();
        int[] a = {-5,0,2,1,2 };
        int[][] edges = {{0,1},{3,4},{2,3},{0,3}};
        System.out.print( solution.solution( a, edges ) );
    }
}
