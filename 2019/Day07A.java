import java.util.*;

public class Day07A {

    static long getOutput(long[] program, ArrayList<Integer> phase){
        long output = 0;
        for (int value : phase) {
            Intcode amp = new Intcode(program);
            amp.addInput(value);
            amp.addInput(output);
            amp.run();
            output = amp.getOutput();
        }
        return output;
    }

    public static void main(String[] args) {
        //get input
        long[] prog = InputReader.readProgram("Day07_input.txt");
        long max = 0;

        //get permutations
        ArrayList<Integer> vals = new ArrayList<>();
        Collections.addAll(vals, 0,1,2,3,4);
        HashSet<ArrayList<Integer>> perm = getPerm(vals);

        //loop through permutations
        for (ArrayList<Integer> arrL : perm) {
            long output = getOutput(prog, arrL);
            max = output>max ? output : max;
        }
        System.out.println(max);
    }

    public static HashSet<ArrayList<Integer>> getPerm(ArrayList<Integer> vals){
        //return empty hashset if vals is empty
        if (vals.size()==1) {
            HashSet<ArrayList<Integer>> one = new HashSet<>();
            one.add(vals);
            return one;
        }
        //get initial value
        int first = vals.get(0);

        //get array w/o initial
        ArrayList<Integer> vals2 = vals;
        vals2.remove(0);

        //recursive call
        HashSet<ArrayList<Integer>> rest = getPerm(vals2);
        HashSet<ArrayList<Integer>> perms = new HashSet<>();

        for (ArrayList<Integer> val : rest) {
            int loop = val.size();
            for (int i = 0; i <= loop; i++) {
                ArrayList<Integer> valTemp = new ArrayList<>(val);
                valTemp.add(i,first);
                perms.add(valTemp);
            }
        }
        return perms;
    }
}
