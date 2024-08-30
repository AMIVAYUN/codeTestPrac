package J16434;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    /**
     * @param args
     * @throws IOException
     * n개의 방 i -> i + 1번 이동 몬스터를 잡아야 다음 방으로 이동 가능
     * n번째 방에는 공주와 용이 있음
     * 그냥 간단한 이분 탐색인 것 같다.
     * 단 전투 로직을 깔끔하게 짜야 시간복잡도가 안정적일 것임
     * BigInteger 구현을 한번 해보았다. 재밌었다 나중에 정리하자.
     */


    static int n;

    static Room[] rooms;

    static long atk;

//    static BigInteger answer;

//    static BigNumber answer;
    static long answer = 0l;
//    static BigInteger Mx = BigInteger.valueOf( 1000000 ).multiply(  BigInteger.valueOf( 1000000 ) ).multiply(  BigInteger.valueOf( 123456 ) ).add( BigInteger.ONE );


    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );

        n = stoi( token.nextToken() );
        atk = stol( token.nextToken() );


//        rooms = new Room[ n ];
        //생각 해보니 그냥 더하면 되는거 아닌가? 누적 뎀지를 구하자
        long current = 0l;
        for( int i = 0; i < n; i ++ ){
            token = new StringTokenizer( bf.readLine() );

            int isSafe = stoi( token.nextToken() );
            int a = stoi( token.nextToken() );
            int h = stoi(token.nextToken());

            if( isSafe < 2 ){
                current += ( h % atk > 0 ? h / atk : h / atk - 1) * a;
                if( current > answer ){
                    answer = current;
                }

            }else{
                atk += a;
                current -= h;
                if( current < 0 ){
                    current = 0;
                }
            }

//            rooms[ i ] = new Room( isSafe, a, h );


        }
//        binarySearch2();



        System.out.println( answer + 1 );
//        System.out.println( answer.getNum());


//        BigNumber n = new BigNumber( "1000" );
//        BigNumber k = new BigNumber( "100" );
//        BigNumber i = new BigNumber( "100" );
//        BigNumber j = new BigNumber( "9000" );
//
//        BigNumber a = n.add( k );
//        BigNumber b = n.sub( i );
//        BigNumber c = k.sub( j );
//        BigNumber d = n.sub( k );
//        System.out.println( n + " " + k + " " + a );
//
//        System.out.println( d + "\n" + c + "\n" + b );
//
//
//        BigNumber mul = n.mul( k );
//        BigNumber mul2 = n.mul( j );

//        System.out.println( mul + " " + mul2 + " " + new BigNumber( "2" ).mul( new BigNumber( "9") ) );

//        BigNumber lt = new BigNumber("1"), rt = new BigNumber( "123456000000000001" );
//
//        System.out.println( lt.add( rt ).divHalf() );


    }

    private static long stol(String s) {
        return Long.parseLong( s );
    }

    private static void binarySearch2() {

//        BigInteger lt = BigInteger.ONE; BigInteger rt = Mx;

        BigNumber lt = new BigNumber("1"), rt = new BigNumber( "123456000000000001" );

        while ( lt.compareTo(rt) <= 0 ){

            BigNumber mid = lt.add( rt ).divHalf();
//            System.out.println( mid );
//            System.out.println( lt + " " + rt + " " + mid + " " + isSafe2( atk, mid ) );
            if( isSafe2( atk, mid ) ){
//                answer = mid;
                rt = mid.sub( new BigNumber("1") );
            }else{
                lt = mid.add( new BigNumber("1") );
            }

        }
    }

    private static boolean isSafe2( long atk, BigNumber hp ) {
        BigNumber maxHp = hp;
//        System.out.println( atk + " " + hp );
        for( int i = 0; i < n; i++ ){
//            System.out.println( i + " hp== " + hp );
            Room room = rooms[ i ];
            if( room.isSafe == 1 ){

                BigNumber mh = new BigNumber( room.h + "" );
                BigNumber ma = new BigNumber( room.a + "" );

                while( hp.compareTo( new BigNumber("0") ) > 0 ){
//                    System.out.println( hp + " " + mh );
                    mh = mh.sub( new BigNumber( atk + "" ));
                    if( mh.compareTo( new BigNumber( "0" ) ) <= 0 ){
                        break;
                    }

                    hp = hp.sub( ma );


                }

            }else{
                atk += room.a;
                hp = hp.add( new BigNumber( room.h + "") );

                if( maxHp.compareTo( hp ) < 0 ){
                    hp = maxHp;
                }
            }

            if( hp.compareTo( new BigNumber("0" )) <= 0 ) return false;
        }

        return true;
    }

//    private static void binarySearch() {
//
//        BigInteger lt = BigInteger.ONE; BigInteger rt = Mx;
//
//        while ( lt.compareTo(rt) <= 0 ){
//            BigInteger mid = lt.add( rt ) .divide( BigInteger.TWO );
////            System.out.println( mid );
////            System.out.println( lt + " " + rt + " " + mid + " " + isSafe( atk, mid ) );
//            if( isSafe( atk, mid ) ){
//                answer = mid;
//                rt = mid.subtract( BigInteger.ONE );
//            }else{
//                lt = mid.add( BigInteger.ONE );
//            }
//
//        }
//    }

//    private static boolean isSafe( long atk, BigInteger hp ) {
//        BigInteger maxHp = hp;
////        System.out.println( atk + " " + hp );
//        for( int i = 0; i < n; i++ ){
////            System.out.println( i + " hp== " + hp );
//            Room room = rooms[ i ];
//            if( room.isSafe == 1 ){
//
//                BigInteger mh = BigInteger.valueOf( room.h );
//                BigInteger ma = BigInteger.valueOf( room.a );
//
//                while( hp.compareTo( BigInteger.ZERO ) > 0 ){
////                    System.out.println( hp + " " + mh );
//                    mh = mh.subtract( BigInteger.valueOf( atk ));
//                    if( mh.compareTo( BigInteger.ZERO ) <= 0 ){
//                        break;
//                    }
//
//                    hp = hp.subtract( ma );
//
//
//                }
//
//            }else{
//                atk += room.a;
//                hp = hp.add( BigInteger.valueOf(room.h) );
//
//                if( maxHp.compareTo( hp ) < 0 ){
//                    hp = maxHp;
//                }
//            }
//
//            if( hp.compareTo( BigInteger.ZERO ) <= 0 ) return false;
//        }
//
//        return true;
//    }

    static class Room{
        int isSafe, a, h;

        public Room(int isSafe, int a, int h) {
            this.isSafe = isSafe;
            this.a = a;
            this.h = h;
        }

        @Override
        public String toString() {
            return "Room{" +
                    "isSafe=" + isSafe +
                    ", a=" + a +
                    ", h=" + h +
                    '}';
        }
    }

    static int stoi( String a ){
        return Integer.parseInt( a );
    }

    /**
     *
     *  학원 갈 때 까지 할게 없다. 한번 BigInteger를 구현해보자.
     *
     */
    static class BigNumber{
        /**
         *
         * 음수 부재
         */
            int[] number;
            int n;
            // -1 0 1
            int positive;

        public BigNumber( String number ) {
            this.n = number.length();
            this.number = new int[ n ];
            for( int i = 1; i <= n; i++ ){
                this.number[ i - 1 ] = number.charAt( n - i ) - '0';
            }
            this.positive = 1;
        }

        private BigNumber( int[] number ){
            this.number = number;
            this.n = number.length;
            this.positive = 1;
        }

        private BigNumber( int[] number, int positive ){
            this.number = number;
            this.n = number.length;
            this.positive = positive;
        }

        public int compareTo(BigNumber target) {
            if (this.n != target.n) {
                return this.n - target.n;
            }
            for (int i = this.n - 1; i >= 0; i--) {
                if (this.number[i] != target.number[i]) {
                    return this.number[i] - target.number[i];
                }
            }
            return 0;
        }

        public BigNumber add( BigNumber target ){
            //더하기는 아무리 늘려도 자릿수가 하나 늘어난다.
            int maxLen = n > target.n ? n : target.n;
            int[] result = new int[ maxLen + 1 ];
            int upper = 0;

            for( int i = 0; i < maxLen + 1; i ++){
//                System.out.println( i + " " + upper );
                int sum = upper;

                if( i < this.n ) sum += this.number[ i ];
                if( i < target.n ) sum += target.number[ i ];

                result[ i ] = sum % 10;
                upper = sum / 10;

            }


            return new BigNumber( Arrays.copyOf( result, result[ maxLen ] == 0 ? maxLen : maxLen + 1 ) );

        }
        public BigNumber sub( BigNumber target ){
            //빼기는 자릿수 주는 것에 제한이 없다.
            int check = this.compareTo( target );
            if( check < 0 ){
                return new BigNumber( new int[ 1 ], -1 );
            } else if ( check == 0 ) {
                return new BigNumber( new int[ 1 ], 0 );
            }

            int maxLen = n > target.n ? n : target.n;
            int[] result = new int[ n ];

            int carry = 0;

            for( int i = 0; i < maxLen; i ++ ){
                int diff = this.number[ i ] - carry;

                if( i < target.n ){
                    diff -= target.number[ i ];
                }

                if( diff < 0 ){
                    diff += 10;
                    carry = 1;
                }else{
                    carry = 0;
                }

                result[ i ] = diff;
            }

            int newLen = result.length;
            for( int i = result.length - 1; i >= 0; i -- ){
                if( result[ i ] != 0 ){
                    newLen = i + 1;
                    break;
                }
            }

            return new BigNumber( Arrays.copyOf( result, newLen ) );

        }
        public BigNumber mul( BigNumber target ){
            //곱셈은 각 자릿수에 곱한 값들을 자리에 맞게 더해주는 것
            // 자릿수는 절대 두 자릿수의 합을 넘을 수 없다.
            int[] result = new int[ this.n + target.n ];
            int carry = 0;
            for( int i = 0; i < this.n; i ++ ){

                for( int j = 0; j < target.n; j ++ ){
                    int current = result[ i + j ] +
                            this.number[ i ] * ( j < target.n ? target.number[ j ] : 0 ) +
                            carry;
                    result[ i + j ] = current % 10;
                    carry = current / 10;
                }
            }
            if( carry > 0 ){
                result[ this.n + target.n - 1 ] = carry;
            }

//            System.out.println( Arrays.toString( result ));
            int newLen = result.length;
            for( int i = result.length - 1; i >= 0; i -- ){
                if( result[ i ] != 0 ){
                    newLen = i + 1;
                    break;
                }
            }

            return new BigNumber( Arrays.copyOf( result, newLen ) );
        }

        public BigNumber divHalf() {
            int[] result = new int[ this.n ];
            int carry = 0;

            for (int i = this.n - 1; i >= 0; i--) {
                int current = this.number[ i ] + carry * 10;
                result[ i ] = current / 2;
                carry = current % 2;
            }

            // 앞의 불필요한 0 제거
            int newLen = result.length;
            for( int i = result.length - 1; i >= 0; i -- ){
                if( result[ i ] != 0 ){
                    newLen = i + 1;
                    break;
                }
            }

            return new BigNumber( Arrays.copyOf( result, newLen ) );
        }

        public BigNumber div( BigNumber div ){

            if( this.compareTo( div ) < 0 ){
                return new BigNumber( new int[ 1 ], 0 );
            }

            BigNumber lt = new BigNumber("1"),
            rt = this,
            mid, quotient = null;

            while( lt.compareTo( rt ) <= 0 ){
                mid = lt.add( rt ).divHalf();
                BigNumber product = mid.mul( div );

                int cmp = product.compareTo(this);
                if (cmp == 0) {
                    return mid;
                } else if (cmp < 0) {
                    quotient = mid;
                    lt = mid.add(new BigNumber("1"));
                } else {
                    rt = mid.sub(new BigNumber("1"));
                }
            }


            return quotient;
        }

        public String getNum(){
            String num = "";

            for( int i = n - 1; i >= 0; i -- ){
                num += number[ i ];
            }

            return num;
        }

        @Override
        public String toString() {
            String num = "";

            for( int i = n - 1; i >= 0; i -- ){
                num += number[ i ];
            }
            return "Postivie = " + positive + " BigNumber{" +
                    "number=" + num +
                    '}';
        }
    }
}