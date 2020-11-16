public class Day19A {
    static long beam(long[] program,int x,int y){
        Intcode computer=new Intcode(program);
        computer.addInput(x); computer.addInput(y); computer.run();
        return computer.getOutput();
    }
    public static void main(String[] args) {
        long[] program=InputReader.readProgram("Day19_input.txt");
        int affected=0;
        for (int y=0; y<50; y++) for (int x=0; x<50; x++) affected+=beam(program,x,y);
        System.out.println(affected);
    }
}
