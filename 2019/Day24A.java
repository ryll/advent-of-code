import java.util.*;

public class Day24A {
    static int reader(String name){
        int bugs=0,index=0;
        for (String line:InputReader.readLines(name)) for (char value:line.toCharArray()) {
            if (value=='#') bugs|=1<<index;
            index++;
        }
        return bugs;
    }
    static boolean bug(int bugs,int x,int y){ return x>=0 && x<5 && y>=0 && y<5 && (bugs&(1<<(y*5+x)))!=0; }
    static int step(int bugs){
        int next=0;
        for (int y=0; y<5; y++) for (int x=0; x<5; x++) {
            int adjacent=0;
            if (bug(bugs,x-1,y)) adjacent++; if (bug(bugs,x+1,y)) adjacent++;
            if (bug(bugs,x,y-1)) adjacent++; if (bug(bugs,x,y+1)) adjacent++;
            if (adjacent==1 || (!bug(bugs,x,y) && adjacent==2)) next|=1<<(y*5+x);
        }
        return next;
    }
    public static void main(String[] args) {
        int bugs=reader("Day24_input.txt"); HashSet<Integer> seen=new HashSet<>();
        while (seen.add(bugs)) bugs=step(bugs);
        System.out.println(bugs);
    }
}
