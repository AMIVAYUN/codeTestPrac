import java.util.*;
class Solution {
    int n, m;
    int[][][] keys = new int[ 4 ][][];
    int[][] field;
    public boolean solution(int[][] key, int[][] lock) {
        boolean answer = true;
        n = key.length;
        m = lock.length;
        keys[ 0 ] = key;
        boolean flag = true;
        for( int i = 0; i < m && flag; i ++ ){
            for( int j = 0; j < m; j ++ ){
                if( lock[ i ][ j ] == 0 ){
                    flag = false;
                    break;
                }
            }
        }

        if( flag ) return true;

        for( int i = 1; i < 4; i ++ ){
            keys[ i ] = rotate( keys[ i - 1 ] );
        }



        field = new int[ n + n + m ][ n + n + m ];

        for( int x = n; x < n + m; x ++ ){
            for( int y = n; y < n + m; y ++ ){
                field[ x ][ y ] = lock[ x - n ][ y - n ];
            }
        }



        for( int x = 0; x < n + m; x ++ ){
            for( int y = 0; y < n + m; y ++ ){
                for( int i = 0; i < 4; i ++ ){
                    int[][] target = keys[ i ];
                    if( isRight( x, y, target ) ){
                        return true;
                    }
                }
            }
        }

        return false;

    }


    public int[][] rotate( int[][] key ){
        int[][] newKey = new int[ n ][ n ];
        for( int x = 0; x < n; x ++ ){
            for( int y = 0; y < n; y ++ ){
                newKey[ x ][ y ] = key[ n - y - 1 ][ x ];
            }
        }


        return newKey;
    }

    public int[][] deepcopy( int[][] field ){
        int k = field.length;
        int[][] newField = new int[ k ][ k ];

        for( int i = 0; i < k; i ++ ){
            for( int j = 0; j < k; j ++ ){
                newField[ i ][ j ] = field[ i ][ j ];
            }
        }

        return newField;
    }

    public boolean isRight( int sx, int sy, int[][] key ){
        int[][] newField = deepcopy( field );

        for( int x = sx; x < sx + n; x ++ ){
            for( int y = sy; y < sy + n; y ++ ){
                newField[ x ][ y ] += key[ x - sx ][ y - sy ];
            }
        }

//         System.out.println( "sx = " + sx + " sy = " + sy + "key == " );
//         for( int i = 0; i < key.length; i ++ ){
//             System.out.println( Arrays.toString( key[ i ] ) );
//         }

//         for( int i = 0; i < n + n + m; i ++ ){
//             System.out.println( Arrays.toString( newField[ i ] )) ;
//         }
//         System.out.println();


        for( int x = n; x < n + m; x ++ ){
            for( int y = n; y < n + m; y ++ ){
                if( newField[ x ][ y ] != 1 ){
                    return false;
                }
            }
        }

        return true;
    }
}