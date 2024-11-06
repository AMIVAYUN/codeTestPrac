package PM;

public class temp {
    public static void main(String[] args) {
        String a = "1234";
        String b = new String("12");
        String c = (b + "34");
        System.out.println( a.equals( c ) );
        System.out.println( a == c );


        String d = "1234";
        String e = "12" + "34";
        System.out.println( d.equals( e ) );
        System.out.println( d == e );
    }
}
