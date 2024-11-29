package temp;

public class Main {
    public static void main(String[] args) {
        System.out.println("Starting task...");

        // Sync + Non-Blocking 방식: 별도의 스레드에서 작업 수행
        Thread taskThread = new Thread(() -> {
            String result = performTask(); // 동기 작업 수행
            System.out.println("Result: " + result);
        });

        taskThread.start();

        System.out.println("Task initiated, but not waiting for result.");
    }

    // Non-Blocking 작업 메서드
    public static String performTask() {
        try {
            Thread.sleep(2000);  // 2초간 작업 수행
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return "Task Done!";
    }
}