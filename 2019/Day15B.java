import java.util.*;

public class Day15B {
    public static void main(String[] args) {
        Day15A.Result result=Day15A.explore(InputReader.readProgram("Day15_input.txt"));
        int[][] moves={{0,-1},{0,1},{-1,0},{1,0}};
        ArrayDeque<int[]> queue=new ArrayDeque<>();
        HashSet<String> seen=new HashSet<>();
        queue.add(new int[]{result.oxygenX,result.oxygenY,0});
        seen.add(result.oxygenX+","+result.oxygenY);
        int minutes=0;
        while (!queue.isEmpty()) {
            int[] current=queue.remove(); minutes=Math.max(minutes,current[2]);
            for (int[] move:moves) {
                int x=current[0]+move[0], y=current[1]+move[1];
                String key=x+","+y;
                if (result.map.getOrDefault(key,0)!=0 && seen.add(key))
                    queue.add(new int[]{x,y,current[2]+1});
            }
        }
        System.out.println(minutes);
    }
}
