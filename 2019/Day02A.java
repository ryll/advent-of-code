public class Day02A {
    public static void main(String[] args) {
        int[] prog = InputReader.readIntProgram("Day02_input.txt");
        prog[1] = 12;
        prog[2] = 2;
        int n = 0;
        while(!(prog[n]==99)){
            //System.out.println(program[n]);
            if (prog[n]==1) {
                prog[prog[n+3]] = prog[prog[n+1]] + prog[prog[n+2]];
            } else if (prog[n]==2){
                prog[prog[n+3]] = prog[prog[n+1]] * prog[prog[n+2]];
            } else {
                System.out.println("Error");
            }
            n=n+4;
        }
        System.out.println(prog[0]);
    }
}
