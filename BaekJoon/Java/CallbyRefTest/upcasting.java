package CallbyRefTest;

public class upcasting {
    public static void main(String[] args) {
        B bc2 = (B) new C();
        int numByBC2 = bc2.foo();
        System.out.println("bc2.foo() is " + numByBC2);
    }
}
class B {
    int foo() { return 3; }
}


class C extends B {
    int foo() { return 6; }
}




