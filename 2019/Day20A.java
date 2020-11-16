import java.util.*;

public class Day20A {
    static class Maze {
        char[][] map;
        HashMap<String,ArrayList<String>> labels=new HashMap<>();
        HashMap<String,String> portals=new HashMap<>();
        HashSet<String> outer=new HashSet<>();
        String start,end;
    }
    static Maze reader(String name){ return parse(InputReader.readLines(name)); }
    static Maze parse(ArrayList<String> input){
        Maze maze=new Maze();
        int height=input.size(),width=0;
        for (String line:input) width=Math.max(width,line.length());
        maze.map=new char[height][width];
        for (char[] line:maze.map) Arrays.fill(line,' ');
        for (int y=0; y<height; y++) for (int x=0; x<input.get(y).length(); x++) maze.map[y][x]=input.get(y).charAt(x);
        int[][] moves={{0,-1},{0,1},{-1,0},{1,0}};
        for (int y=0; y<height; y++) for (int x=0; x<width; x++) if (maze.map[y][x]=='.') {
            for (int[] move:moves) {
                int x1=x+move[0],y1=y+move[1],x2=x+2*move[0],y2=y+2*move[1];
                if (y2<0 || y2>=height || x2<0 || x2>=width || !Character.isUpperCase(maze.map[y1][x1]) || !Character.isUpperCase(maze.map[y2][x2])) continue;
                String label=move[0]+move[1]<0 ? ""+maze.map[y2][x2]+maze.map[y1][x1] : ""+maze.map[y1][x1]+maze.map[y2][x2];
                String point=x+","+y;
                maze.labels.computeIfAbsent(label,key -> new ArrayList<>()).add(point);
                if (x<=2 || y<=2 || x>=width-3 || y>=height-3) maze.outer.add(point);
            }
        }
        maze.start=maze.labels.get("AA").get(0); maze.end=maze.labels.get("ZZ").get(0);
        for (ArrayList<String> points:maze.labels.values()) if (points.size()==2) {
            maze.portals.put(points.get(0),points.get(1)); maze.portals.put(points.get(1),points.get(0));
        }
        return maze;
    }
    public static void main(String[] args) {
        Maze maze=reader("Day20_input.txt");
        int[][] moves={{0,-1},{0,1},{-1,0},{1,0}};
        ArrayDeque<String> queue=new ArrayDeque<>();
        HashMap<String,Integer> distance=new HashMap<>();
        queue.add(maze.start); distance.put(maze.start,0);
        while (!queue.isEmpty()) {
            String point=queue.remove(); int current=distance.get(point);
            if (point.equals(maze.end)) { System.out.println(current); return; }
            String[] parts=point.split(","); int x=Integer.parseInt(parts[0]),y=Integer.parseInt(parts[1]);
            for (int[] move:moves) {
                int nx=x+move[0],ny=y+move[1]; String next=nx+","+ny;
                if (maze.map[ny][nx]=='.' && !distance.containsKey(next)) { distance.put(next,current+1); queue.add(next); }
            }
            if (maze.portals.containsKey(point) && !distance.containsKey(maze.portals.get(point))) {
                distance.put(maze.portals.get(point),current+1); queue.add(maze.portals.get(point));
            }
        }
    }
}
