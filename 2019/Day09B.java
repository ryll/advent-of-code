public class Day09B {
    public static void main(String[] args) {
        //get input
        Intcode computer = new Intcode(InputReader.readProgram("Day09_input.txt"), 2);
        System.out.println(computer.getOutput());
    }
}
