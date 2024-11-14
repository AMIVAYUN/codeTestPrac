package JNI;

public class Helloworld {
    public native void printHelloWorld();

    static{
        System.loadLibrary("helloworld");
    }

    public static void main(String[] args) {
        new Helloworld().printHelloWorld();
    }
}
