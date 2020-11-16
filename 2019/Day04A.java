public class Day04A {

    static boolean valid(int number) {
        String password = Integer.toString(number);
        boolean pair = false;
        for (int i = 1; i < password.length(); i++) {
            if (password.charAt(i) < password.charAt(i - 1)) return false;
            if (password.charAt(i) == password.charAt(i - 1)) pair = true;
        }
        return pair;
    }

    public static void main(String[] args) {
        String[] range = InputReader.readString("Day04_input.txt").split("-", 2);
        int lower = Integer.parseInt(range[0]);
        int upper = Integer.parseInt(range[1]);
        int passwords = 0;
        for (int number = lower; number <= upper; number++) {
            if (valid(number)) passwords++;
        }
        System.out.println(passwords);
    }
}
