public class Day02B {
    public static void main(String[] args) {
        int out = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                int[] prog = InputReader.readIntProgram("Day02_input.txt");
                prog[1] = i;
                prog[2] = j;
                int n = 0;
                while(!(prog[n]==99)){
                    if (prog[n]==1) {
                        prog[prog[n+3]] = prog[prog[n+1]] + prog[prog[n+2]];
                    } else if (prog[n]==2){
                        prog[prog[n+3]] = prog[prog[n+1]] * prog[prog[n+2]];
                    } else {
                        System.out.println("Error");
                    }
                    n=n+4;
                }
                if (prog[0]==19690720) {
                    System.out.println(prog[0]+", "+i+", "+j);
                    out = 1;
                    break;
                }

            }
            if (out==1) {
                break;
            }
        }
    }
}
