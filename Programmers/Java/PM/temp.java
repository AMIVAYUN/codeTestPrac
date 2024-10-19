package PM;

public class temp {
    public static void main(String[] args) {
        Temp temp = new Temp1();
        temp.run();
    }
    static interface Temp{

        public void run();
    }

    static class Temp1 implements Temp{
        public void run(){
            System.out.println("temp1");
        }
    }

    static class Temp2 implements Temp{

        public void run(){
            System.out.println("temp2");
        }
    }


}
