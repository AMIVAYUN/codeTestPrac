package J16170;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.LocalDate;
import java.time.ZoneId;
import java.util.*;

public class Main {

    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;



    public static void main(String[] args) throws IOException {
        LocalDate utcDate = LocalDate.now(ZoneId.of("UTC"));

        // 연, 월, 일 추출
        int year = utcDate.getYear();
        int month = utcDate.getMonthValue();
        int day = utcDate.getDayOfMonth();

        // 출력
        System.out.println(year);
        System.out.println(month);
        System.out.println(day);
    }
}

