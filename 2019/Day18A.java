import java.util.*;

public class Day18A {
    static class Edge {
        char key; int distance,doors;
        Edge(char key,int distance,int doors){ this.key=key; this.distance=distance; this.doors=doors; }
    }
    static class Search {
        int x,y,distance,doors;
        Search(int x,int y,int distance,int doors){ this.x=x; this.y=y; this.distance=distance; this.doors=doors; }
    }
    static class State implements Comparable<State> {
        String positions; int keys,distance;
        State(String positions,int keys,int distance){ this.positions=positions; this.keys=keys; this.distance=distance; }
        public int compareTo(State other){ return Integer.compare(distance,other.distance); }
    }

    static int solve(ArrayList<String> input){
        char[][] map=new char[input.size()][];
        HashMap<Character,int[]> points=new HashMap<>();
        String starts=""; char startName='0'; int allKeys=0;
        for (int y=0; y<input.size(); y++) {
            map[y]=input.get(y).toCharArray();
            for (int x=0; x<map[y].length; x++) {
                char value=map[y][x];
                if (value=='@') { value=startName++; map[y][x]=value; starts+=value; points.put(value,new int[]{x,y}); }
                else if (Character.isLowerCase(value)) {
                    points.put(value,new int[]{x,y}); allKeys|=1<<(value-'a');
                }
            }
        }
        HashMap<Character,ArrayList<Edge>> graph=new HashMap<>();
        for (Map.Entry<Character,int[]> point:points.entrySet())
            graph.put(point.getKey(),edges(map,point.getKey(),point.getValue()));

        PriorityQueue<State> queue=new PriorityQueue<>();
        HashMap<String,Integer> best=new HashMap<>();
        queue.add(new State(starts,0,0));
        while (!queue.isEmpty()) {
            State current=queue.remove();
            String stateKey=current.positions+":"+current.keys;
            if (current.distance>=best.getOrDefault(stateKey,Integer.MAX_VALUE)) continue;
            best.put(stateKey,current.distance);
            if (current.keys==allKeys) return current.distance;
            for (int robot=0; robot<current.positions.length(); robot++) {
                for (Edge edge:graph.get(current.positions.charAt(robot))) {
                    if ((edge.doors&~current.keys)!=0) continue;
                    int keys=current.keys|1<<(edge.key-'a');
                    StringBuilder positions=new StringBuilder(current.positions);
                    positions.setCharAt(robot,edge.key);
                    queue.add(new State(positions.toString(),keys,current.distance+edge.distance));
                }
            }
        }
        throw new IllegalStateException("Not all keys are reachable");
    }

    static ArrayList<Edge> edges(char[][] map,char source,int[] start){
        int[][] moves={{0,-1},{0,1},{-1,0},{1,0}};
        ArrayDeque<Search> queue=new ArrayDeque<>();
        HashSet<String> seen=new HashSet<>();
        ArrayList<Edge> edges=new ArrayList<>();
        queue.add(new Search(start[0],start[1],0,0));
        while (!queue.isEmpty()) {
            Search current=queue.remove();
            String state=current.x+","+current.y+","+current.doors;
            if (!seen.add(state)) continue;
            char value=map[current.y][current.x];
            if (Character.isLowerCase(value) && value!=source && current.distance>0) {
                edges.add(new Edge(value,current.distance,current.doors));
                continue;
            }
            int doors=current.doors;
            if (Character.isUpperCase(value)) doors|=1<<(Character.toLowerCase(value)-'a');
            for (int[] move:moves) {
                int x=current.x+move[0],y=current.y+move[1];
                if (y>=0 && y<map.length && x>=0 && x<map[y].length && map[y][x]!='#')
                    queue.add(new Search(x,y,current.distance+1,doors));
            }
        }
        return edges;
    }

    public static void main(String[] args) {
        System.out.println(solve(InputReader.readLines("Day18_input.txt")));
    }
}
