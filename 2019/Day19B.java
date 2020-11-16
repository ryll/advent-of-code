public class Day19B {
    public static void main(String[] args) {
        long[] program=InputReader.readProgram("Day19_input.txt");
        int x=0;
        for (int y=99; ; y++) {
            while (Day19A.beam(program,x,y)==0) x++;
            if (Day19A.beam(program,x+99,y-99)==1) {
                System.out.println(x*10000+y-99);
                return;
            }
        }
    }
}
