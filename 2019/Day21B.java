public class Day21B {
    public static void main(String[] args) {
        String script="NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nNOT E T\nNOT T T\nOR H T\nAND T J\nRUN\n";
        System.out.println(Day21A.run(InputReader.readProgram("Day21_input.txt"),script));
    }
}
