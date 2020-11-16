public class Day04B {

    static boolean valid(int number) {
        String password = Integer.toString(number);
        boolean pair = false;
        int groupSize = 1;
        for (int i = 1; i < password.length(); i++) {
            if (password.charAt(i) < password.charAt(i - 1)) return false;
            if (password.charAt(i) == password.charAt(i - 1)) {
                groupSize++;
            } else {
                if (groupSize == 2) pair = true;
                groupSize = 1;
            }
        }
        return pair || groupSize == 2;
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
