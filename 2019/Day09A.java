public class Day09A {
    public static void main(String[] args) {
        //get input
        long[] prog = InputReader.readProgram("Day09_input.txt");
        long input = 1;

        Intcode tester = new Intcode(prog, input);
        System.out.println(tester.getOutput());
                
    }
}
