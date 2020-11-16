import java.util.*;

public class Day18B {
    public static void main(String[] args) {
        ArrayList<String> input=InputReader.readLines("Day18_input.txt");
        ArrayList<StringBuilder> map=new ArrayList<>();
        for (String line:input) map.add(new StringBuilder(line));
        int centerX=0,centerY=0;
        for (int y=0; y<map.size(); y++) {
            int x=map.get(y).indexOf("@");
            if (x>=0) { centerX=x; centerY=y; break; }
        }
        for (int y=-1; y<=1; y++) for (int x=-1; x<=1; x++)
            map.get(centerY+y).setCharAt(centerX+x,(Math.abs(x)==1 && Math.abs(y)==1) ? '@' : '#');
        input.clear();
        for (StringBuilder line:map) input.add(line.toString());
        System.out.println(Day18A.solve(input));
    }
}
