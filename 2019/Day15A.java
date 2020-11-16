import java.util.*;

public class Day15A {
    static class State {
        int x,y,distance; Intcode computer;
        State(int x,int y,int distance,Intcode computer){
            this.x=x; this.y=y; this.distance=distance; this.computer=computer;
        }
    }
    static class Result {
        HashMap<String,Integer> map=new HashMap<>();
        int oxygenX,oxygenY,distance;
    }
    static Result explore(long[] program){
        int[][] moves={{0,0},{0,-1},{0,1},{-1,0},{1,0}};
        ArrayDeque<State> queue=new ArrayDeque<>();
        Result result=new Result();
        result.map.put("0,0",1);
        queue.add(new State(0,0,0,new Intcode(program)));
        while (!queue.isEmpty()) {
            State current=queue.remove();
            for (int command=1; command<=4; command++) {
                int x=current.x+moves[command][0], y=current.y+moves[command][1];
                String key=x+","+y;
                if (result.map.containsKey(key)) continue;
                Intcode next=new Intcode(current.computer);
                next.addInput(command); next.runUntilOutput();
                int tile=(int)next.getOutput();
                result.map.put(key,tile);
                if (tile==0) continue;
                queue.add(new State(x,y,current.distance+1,next));
                if (tile==2) {
                    result.oxygenX=x; result.oxygenY=y; result.distance=current.distance+1;
                }
            }
        }
        return result;
    }
    public static void main(String[] args) {
        System.out.println(explore(InputReader.readProgram("Day15_input.txt")).distance);
    }
}
