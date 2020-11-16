public class Day21A {
    static long run(long[] program,String script){
        Intcode computer=new Intcode(program);
        for (char value:script.toCharArray()) computer.addInput(value);
        computer.run(); long result=0;
        while (computer.hasOutput()) {
            long value=computer.getOutput();
            if (value>255) result=value;
        }
        return result;
    }
    public static void main(String[] args) {
        String script="NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nWALK\n";
        System.out.println(run(InputReader.readProgram("Day21_input.txt"),script));
    }
}
