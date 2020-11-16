import java.util.*;
import java.util.regex.*;

public class Day12A {
    static long[][] reader(String name){
        ArrayList<String> input=InputReader.readLines(name);
        long[][] moons=new long[input.size()][6];
        Pattern number=Pattern.compile("-?\\d+");
        for (int i=0; i<input.size(); i++) {
            Matcher matcher=number.matcher(input.get(i));
            for (int j=0; j<3; j++) { matcher.find(); moons[i][j]=Long.parseLong(matcher.group()); }
        }
        return moons;
    }
    static void step(long[][] moons){
        for (int i=0; i<moons.length; i++) for (int j=i+1; j<moons.length; j++) {
            for (int axis=0; axis<3; axis++) {
                long change=Long.compare(moons[j][axis],moons[i][axis]);
                moons[i][axis+3]+=change; moons[j][axis+3]-=change;
            }
        }
        for (long[] moon:moons) for (int axis=0; axis<3; axis++) moon[axis]+=moon[axis+3];
    }
    public static void main(String[] args) {
        long[][] moons=reader("Day12_input.txt");
        for (int i=0; i<1000; i++) step(moons);
        long energy=0;
        for (long[] moon:moons) {
            long potential=Math.abs(moon[0])+Math.abs(moon[1])+Math.abs(moon[2]);
            long kinetic=Math.abs(moon[3])+Math.abs(moon[4])+Math.abs(moon[5]);
            energy+=potential*kinetic;
        }
        System.out.println(energy);
    }
}
