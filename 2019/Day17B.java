import java.util.*;

public class Day17B {
    static ArrayList<String> path(ArrayList<String> map){
        int x=0,y=0,direction=0;
        String robots="^>v<";
        for (int row=0; row<map.size(); row++) for (int col=0; col<map.get(row).length(); col++) {
            int found=robots.indexOf(map.get(row).charAt(col));
            if (found>=0) { x=col; y=row; direction=found; }
        }
        int[][] moves={{0,-1},{1,0},{0,1},{-1,0}};
        ArrayList<String> path=new ArrayList<>();
        while (true) {
            int left=(direction+3)%4,right=(direction+1)%4;
            if (Day17A.scaffold(map,x+moves[left][0],y+moves[left][1])) { path.add("L"); direction=left; }
            else if (Day17A.scaffold(map,x+moves[right][0],y+moves[right][1])) { path.add("R"); direction=right; }
            else break;
            int steps=0;
            while (Day17A.scaffold(map,x+moves[direction][0],y+moves[direction][1])) {
                x+=moves[direction][0]; y+=moves[direction][1]; steps++;
            }
            path.add(Integer.toString(steps));
        }
        return path;
    }
    static boolean starts(ArrayList<String> path,int index,ArrayList<String> value){
        if (index+value.size()>path.size()) return false;
        for (int i=0; i<value.size(); i++) if (!path.get(index+i).equals(value.get(i))) return false;
        return true;
    }
    static int length(List<String> values){ return String.join(",",values).length(); }
    static boolean compress(ArrayList<String> path,int index,ArrayList<ArrayList<String>> functions,ArrayList<String> main){
        if (index==path.size()) return functions.size()==3 && length(main)<=20;
        for (int i=0; i<functions.size(); i++) {
            ArrayList<String> function=functions.get(i);
            if (starts(path,index,function)) {
                main.add("ABC".substring(i,i+1));
                if (length(main)<=20 && compress(path,index+function.size(),functions,main)) return true;
                main.remove(main.size()-1);
            }
        }
        if (functions.size()<3) {
            for (int end=index+2; end<=path.size(); end+=2) {
                ArrayList<String> function=new ArrayList<>(path.subList(index,end));
                if (length(function)>20) break;
                functions.add(function); main.add("ABC".substring(functions.size()-1,functions.size()));
                if (length(main)<=20 && compress(path,end,functions,main)) return true;
                main.remove(main.size()-1); functions.remove(functions.size()-1);
            }
        }
        return false;
    }
    public static void main(String[] args) {
        long[] program=InputReader.readProgram("Day17_input.txt");
        ArrayList<ArrayList<String>> functions=new ArrayList<>();
        ArrayList<String> main=new ArrayList<>();
        if (!compress(path(Day17A.map(program)),0,functions,main)) throw new IllegalStateException("No movement program found");
        Intcode computer=new Intcode(program); computer.setMemory(0,2);
        String input=String.join(",",main)+"\n";
        for (ArrayList<String> function:functions) input+=String.join(",",function)+"\n";
        input+="n\n";
        for (char value:input.toCharArray()) computer.addInput(value);
        computer.run();
        long dust=0;
        while (computer.hasOutput()) dust=computer.getOutput();
        System.out.println(dust);
    }
}
