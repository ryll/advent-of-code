import java.util.*;

public class Day07B {

    static long getOutput(long[] program, ArrayList<Integer> phase){
        Intcode[] amps = new Intcode[5];
        for (int i = 0; i < amps.length; i++) {
            amps[i] = new Intcode(program);
            amps[i].addInput(phase.get(i));
        }

        long output = 0;
        long lastOutput = 0;
        while (!amps[4].isHalted()) {
            for (int i = 0; i < amps.length; i++) {
                amps[i].addInput(output);
                if (amps[i].runUntilOutput()) {
                    output = amps[i].getOutput();
                    if (i==4) lastOutput = output;
                }
            }
        }
        return lastOutput;
    }

    public static void main(String[] args) {
        //get input
        long[] prog = InputReader.readProgram("Day07_input.txt");
        long max = 0;

        //get permutations
        ArrayList<Integer> vals = new ArrayList<>();
        Collections.addAll(vals, 5,6,7,8,9);
        HashSet<ArrayList<Integer>> perm = Day07A.getPerm(vals);

        //loop through permutations
        for (ArrayList<Integer> arrL : perm) {
            long output = getOutput(prog, arrL);
            max = output>max ? output : max;
        }
        System.out.println(max);
    }
}
