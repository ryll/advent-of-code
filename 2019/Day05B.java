public class Day05B {
    public static void main(String[] args) {
        //get input
        Intcode computer = new Intcode(InputReader.readProgram("Day05_input.txt"));
        computer.addInput(5);
        computer.run();
        while (computer.hasOutput()) System.out.println("Output: "+computer.getOutput());
    }
}
