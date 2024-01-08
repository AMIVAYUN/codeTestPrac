package CallbyRefTest;

public class CallbyReftest {
    public static void main( String[] args ){
        Test test = new Test();
        //call - by - reference라 파라미터로 넘긴 객체는 보존 됨.
        System.out.println( test.verification( 1 ) );
    }

}
