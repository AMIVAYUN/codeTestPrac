package CallbyRefTest;

public class Test {

    public boolean verification( int k ){

        A a = new A( k );
        System.out.println( "a: "+ a.a );

        ThirdMan t = new ThirdMan();
        t.test( a );

        System.out.println( "a: "+ a.a );
        return k != a.a;
    }

    public void upperA( A a ){
        a.a++;
    }
}
