public class p002 {
    public static void main(String[] args) {
        int limit = 4_000_000;
        int a = 1, b = 1, c = 2, sum = 0;

        // every third Fibonacci number is even
        while (c <= limit) {
            sum += c;
            a = b + c;
            b = c + a;
            c = a + b;
        }
        System.out.println(sum);
    }
}
