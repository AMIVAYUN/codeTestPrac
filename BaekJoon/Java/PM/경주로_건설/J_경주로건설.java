package PM.경주로_건설;

public class J_경주로건설 {
    public static void main( String[] args ){
        Solution s = new Solution();
        int[][] tc = {{0,0,0},{0,0,0},{0,0,0}};
        s.solution( tc );
        for( int[][] row : s.visit ){
            for( int[] a : row ){
                System.out.print( "[");
                for( int b : a ){
                    System.out.print( b + ",");
                }
                System.out.print( "]");
                System.out.print( " , ");
            }
            System.out.println();

        }

    }
}
