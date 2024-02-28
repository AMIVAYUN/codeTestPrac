package J26086;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main2 {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int context = 0;
    static int n,q,k;

    /**
     *
     * @param args
     * @throws IOException
     *
     * $0 p$: 고유번호가
     * $p$인 업무를 스케줄러에 추가한다. 특별히 다른 명령이 없는 한, 새로 추가된 일은 스케줄러 상의 맨 앞에 추가된다. 즉, 고유번호 값에 상관없이 스케줄러에서 가장 먼저 처리되어야 하는 업무가 된다.
     *
     * $1$: 스케줄러에 들어있는 업무를 고유번호 값 기준으로 오름차순으로 정렬한다. 이 결과, 고유번호 값이 낮은 업무일수록 스케줄러의 앞에 배치된다.
     *
     * $2$: 스케줄러에 있는 업무 처리 순서를 뒤집는다. 즉, 스케줄러에 들어가 있는 업무들의 처리 순서가 반대가 된다.
     *
     * reverse =>   t t // f
     *              t f // t
     *              f t // t
     *              f f // f
     *
     *              즉 XOR연산
     *
     *              0이면 child가 뒤에 붙고
     *              1이면 child가 앞에 붙음
     */
    static int size = 0;
    //    static Segment[] segments;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer( bf.readLine() );
        n = Integer.parseInt( token.nextToken() );
        q = Integer.parseInt( token.nextToken() );
        k = Integer.parseInt( token.nextToken() );
//        segments = new Segment[ q ];
        ArrayList< Integer > nums = new ArrayList<>();
        ArrayList< Integer > contains = new ArrayList<>();
        int lastSort = 0;
        ArrayList<ArrayList<Integer>> commands = new ArrayList<>();
        ArrayList< Integer > command = new ArrayList<>();
        ArrayList<Integer> start = new ArrayList<>();
        int startContext = 0;
        for( int i = 0; i < q; i ++ ){
            token = new StringTokenizer( bf.readLine() );
            if( token.countTokens() == 1 ){
                int cmd = Integer.parseInt(token.nextToken());
                command.add( cmd );
                commands.add(command);
                command = new ArrayList<>();
//                Segment segment = new Segment( contains );
//                contains = new ArrayList<>();

                if( cmd == 1 ){
//                    ArrayList< Integer > next = (ArrayList<Integer>) nums.clone();
//                    Collections.sort( next );
//                    segment.arrayList = next;

                    lastSort = size++;
                    Collections.sort( nums );
                    start = (ArrayList<Integer>) nums.clone();
                    startContext = context;
//                    segments[ size++ ] = segment;
                }else{
                    if( size++ > 0 ) {
//                        segment.isReversed ^= 1;
                        context ^= 1;
//                    }else{
////                        segment.isReversed = 1;
//
//                    }
//                    segments[ size++ ] = segment;
                    }
                }
            }else{
                command.add(Integer.parseInt(token.nextToken()));
                nums.add( Integer.parseInt( token.nextToken() ) );
                command.add( nums.get( nums.size() - 1 ) );
                commands.add( command );
                command = new ArrayList<>();
                size++;
//                if( context == 0 ){
//                    contains.add( 0, nums.get( nums.size() -1 ) );
//                }else{
//                    contains.add( nums.get( nums.size() -1 ) );
//                }

            }
        }
//     *              0이면 child가 뒤에 붙고
//     *              1이면 child가 앞에 붙음

//        System.out.println(size );
        context = startContext;
        ArrayList< Integer >[] beforeAfter = new ArrayList[2];
        beforeAfter[ 0 ] = new ArrayList<>();
        beforeAfter[ 1 ] = new ArrayList<>();

        if( startContext == 1 ){
            Collections.sort( start, Collections.reverseOrder() );
        }
        for( int i = lastSort + 1; i < size; i ++ ){
            ArrayList<Integer> now = commands.get( i );
            if (now.get(0) == 0) {
                beforeAfter[context].add(now.get(1));
            } else {
                context ^= 1;
            }
        }
        ArrayList<Integer> result = beforeAfter[ context ];
        result.addAll( start );
        result.addAll( beforeAfter[ context ^ 1 ] );

//        System.out.println( result );

        System.out.println(result.get( k - 1 ));
        //sol1
//        System.out.println( Arrays.toString( segments ));
//        ArrayList<Integer> serial = segments[lastSort].arrayList;
//        Collections.sort( serial );
//        int semiContext = segments[lastSort].isReversed;
//        ArrayList<Integer> before = new ArrayList<>();
//        ArrayList<Integer> after = new ArrayList<>();
//
//        for( int idx = lastSort + 1; idx < size; idx ++ ){
//            //전부 add all로 하니깐 터진다. 이 부분을 최적화
////            if( segments[ idx ].isReversed == 1 ){
////                ArrayList<Integer> temp = segments[idx].contains;
////                temp.addAll( serial );
////                serial = temp;
////            }else{
////                serial.addAll( segments[ idx ].contains );
////            }
//            if( segments[ idx ].isReversed == 1 ){
//
//            }else{
//
//            }
//        }
//
//        int target = context == 0 ? k -1 :serial.size() - k;
//
//        System.out.println(serial.get( target ));


    }




//    static class Segment{
//
//        int isReversed = 0;
//        ArrayList< Integer > arrayList;
//        ArrayList< Integer > contains;
//
//        public Segment(ArrayList<Integer> arrayList) {
//            this.contains = arrayList;
//        }
//
//        @Override
//        public String toString() {
//            return "Segment{" +
//                    "isReversed=" + isReversed +
//                    ", arrayList=" + arrayList +
//                    ", nums=" + contains +
//                    '}';
//        }
//    }
}