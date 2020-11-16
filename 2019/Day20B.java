import java.util.*;

public class Day20B {
    static class State {
        String point; int level,distance;
        State(String point,int level,int distance){ this.point=point; this.level=level; this.distance=distance; }
    }
    public static void main(String[] args) {
        Day20A.Maze maze=Day20A.reader("Day20_input.txt");
        int[][] moves={{0,-1},{0,1},{-1,0},{1,0}};
        int maxLevel=maze.portals.size();
        ArrayDeque<State> queue=new ArrayDeque<>(); HashSet<String> seen=new HashSet<>();
        queue.add(new State(maze.start,0,0));
        while (!queue.isEmpty()) {
            State current=queue.remove();
            String state=current.point+","+current.level;
            if (!seen.add(state)) continue;
            if (current.point.equals(maze.end) && current.level==0) { System.out.println(current.distance); return; }
            String[] parts=current.point.split(","); int x=Integer.parseInt(parts[0]),y=Integer.parseInt(parts[1]);
            for (int[] move:moves) {
                int nx=x+move[0],ny=y+move[1]; String next=nx+","+ny;
                if (maze.map[ny][nx]=='.' && (current.level==0 || (!next.equals(maze.start) && !next.equals(maze.end))))
                    queue.add(new State(next,current.level,current.distance+1));
            }
            if (maze.portals.containsKey(current.point)) {
                int nextLevel=current.level+(maze.outer.contains(current.point) ? -1 : 1);
                if (nextLevel>=0 && nextLevel<=maxLevel)
                    queue.add(new State(maze.portals.get(current.point),nextLevel,current.distance+1));
            }
        }
    }
}
