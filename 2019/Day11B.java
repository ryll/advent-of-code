import java.util.*;

public class Day11B {
    public static void main(String[] args) {
        HashMap<String,Long> panels=Day11A.paint(InputReader.readProgram("Day11_input.txt"),1);
        int minX=0,maxX=0,minY=0,maxY=0;
        for (String key:panels.keySet()) {
            String[] point=key.split(",");
            int x=Integer.parseInt(point[0]), y=Integer.parseInt(point[1]);
            minX=Math.min(minX,x); maxX=Math.max(maxX,x);
            minY=Math.min(minY,y); maxY=Math.max(maxY,y);
        }
        for (int y=minY; y<=maxY; y++) {
            for (int x=minX; x<=maxX; x++)
                System.out.print(panels.getOrDefault(x+","+y,0L)==1 ? '#' : ' ');
            System.out.println();
        }
    }
}
