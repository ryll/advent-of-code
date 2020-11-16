import java.util.*;

public class Day24B {
    static boolean bug(HashMap<Integer,Integer> levels,int level,int x,int y){
        return (levels.getOrDefault(level,0)&(1<<(y*5+x)))!=0;
    }
    static int adjacent(HashMap<Integer,Integer> levels,int level,int x,int y){
        int count=0;
        int[][] moves={{0,-1},{0,1},{-1,0},{1,0}};
        for (int[] move:moves) {
            int nx=x+move[0],ny=y+move[1];
            if (nx==2 && ny==2) {
                if (x==2 && y==1) for (int innerX=0; innerX<5; innerX++) if (bug(levels,level+1,innerX,0)) count++;
                if (x==2 && y==3) for (int innerX=0; innerX<5; innerX++) if (bug(levels,level+1,innerX,4)) count++;
                if (x==1 && y==2) for (int innerY=0; innerY<5; innerY++) if (bug(levels,level+1,0,innerY)) count++;
                if (x==3 && y==2) for (int innerY=0; innerY<5; innerY++) if (bug(levels,level+1,4,innerY)) count++;
            }
            else if (nx<0) { if (bug(levels,level-1,1,2)) count++; }
            else if (nx>=5) { if (bug(levels,level-1,3,2)) count++; }
            else if (ny<0) { if (bug(levels,level-1,2,1)) count++; }
            else if (ny>=5) { if (bug(levels,level-1,2,3)) count++; }
            else if (bug(levels,level,nx,ny)) count++;
        }
        return count;
    }
    static HashMap<Integer,Integer> step(HashMap<Integer,Integer> levels,int min,int max){
        HashMap<Integer,Integer> next=new HashMap<>();
        for (int level=min-1; level<=max+1; level++) {
            int bugs=0;
            for (int y=0; y<5; y++) for (int x=0; x<5; x++) {
                if (x==2 && y==2) continue;
                int adjacent=adjacent(levels,level,x,y);
                if (adjacent==1 || (!bug(levels,level,x,y) && adjacent==2)) bugs|=1<<(y*5+x);
            }
            if (bugs!=0) next.put(level,bugs);
        }
        return next;
    }
    public static void main(String[] args) {
        HashMap<Integer,Integer> levels=new HashMap<>(); levels.put(0,Day24A.reader("Day24_input.txt")&~(1<<12));
        for (int minute=0; minute<200; minute++) levels=step(levels,-minute-1,minute+1);
        int total=0;
        for (int bugs:levels.values()) total+=Integer.bitCount(bugs);
        System.out.println(total);
    }
}
