public class Day01A {
    public static void main(String[] args) {
        int fuel = 0;
        for (String line : InputReader.readLines("Day01_input.txt")) {
            int input = Integer.parseInt(line);
            fuel = fuel+input/3-2;
        }
        System.out.println(fuel);
    }
}
