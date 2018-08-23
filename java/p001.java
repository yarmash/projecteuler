public class p001 {
    public static void main(String[] args) {
        int lim = 999;
        System.out.println(
            arithmeticSeries(3, lim/3*3, lim/3)
            + arithmeticSeries(5, lim/5*5, lim/5)
            - arithmeticSeries(15, lim/15*15, lim/15)
        );
    }

    public static int arithmeticSeries(int first, int last, int terms) {
        return terms * (first + last) / 2;
    }
}
