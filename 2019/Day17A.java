import java.util.*;

public class Day17A {
    static ArrayList<String> map(long[] program){
        Intcode computer=new Intcode(program); computer.run();
        ArrayList<String> map=new ArrayList<>(); String line="";
        while (computer.hasOutput()) {
            char value=(char)computer.getOutput();
            if (value=='\n') { if (!line.isEmpty()) map.add(line); line=""; }
            else line+=value;
        }
        return map;
    }
    static boolean scaffold(ArrayList<String> map,int x,int y){
        return y>=0 && y<map.size() && x>=0 && x<map.get(y).length() && map.get(y).charAt(x)!='.';
    }
    public static void main(String[] args) {
        ArrayList<String> map=map(InputReader.readProgram("Day17_input.txt"));
        int sum=0;
        for (int y=1; y<map.size()-1; y++) for (int x=1; x<map.get(y).length()-1; x++) {
            if (scaffold(map,x,y) && scaffold(map,x-1,y) && scaffold(map,x+1,y)
                && scaffold(map,x,y-1) && scaffold(map,x,y+1)) sum+=x*y;
        }
        System.out.println(sum);
    }
}
