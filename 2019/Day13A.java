public class Day13A {
    public static void main(String[] args) {
        Intcode computer=new Intcode(InputReader.readProgram("Day13_input.txt"));
        computer.run();
        int blocks=0;
        while (computer.hasOutput()) {
            computer.getOutput(); computer.getOutput();
            if (computer.getOutput()==2) blocks++;
        }
        System.out.println(blocks);
    }
}
