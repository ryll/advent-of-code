import java.util.*;

public class Day11A {
    static HashMap<String,Long> paint(long[] program, long start){
        Intcode computer=new Intcode(program);
        HashMap<String,Long> panels=new HashMap<>();
        int x=0,y=0,direction=0;
        int[][] moves={{0,-1},{1,0},{0,1},{-1,0}};
        panels.put("0,0",start);
        while (!computer.isHalted()) {
            String key=x+","+y;
            computer.addInput(panels.getOrDefault(key,0L));
            if (!computer.runUntilOutput()) break;
            panels.put(key,computer.getOutput());
            if (!computer.runUntilOutput()) break;
            long turn=computer.getOutput();
            direction=(direction+(turn==0 ? 3 : 1))%4;
            x+=moves[direction][0]; y+=moves[direction][1];
        }
        return panels;
    }
    public static void main(String[] args) {
        System.out.println(paint(InputReader.readProgram("Day11_input.txt"),0).size());
    }
}
