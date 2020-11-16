import java.util.*;

public class Day10A {
    static class Point {
        int x, y;
        Point(int x, int y){ this.x=x; this.y=y; }
        public boolean equals(Object other){
            if (!(other instanceof Point)) return false;
            Point point=(Point)other;
            return x==point.x && y==point.y;
        }
        public int hashCode(){ return Objects.hash(x,y); }
    }

    //read all asteroid positions
    static ArrayList<Point> reader(String name){
        ArrayList<String> input=InputReader.readLines(name);
        ArrayList<Point> asteroids=new ArrayList<>();
        for (int y=0; y<input.size(); y++) {
            for (int x=0; x<input.get(y).length(); x++) {
                if (input.get(y).charAt(x)=='#') asteroids.add(new Point(x,y));
            }
        }
        return asteroids;
    }

    static int gcd(int a, int b){
        a=Math.abs(a); b=Math.abs(b);
        while (b!=0) { int temp=a%b; a=b; b=temp; }
        return a;
    }

    static int visible(Point station, ArrayList<Point> asteroids){
        HashSet<String> directions=new HashSet<>();
        for (Point point:asteroids) {
            if (station.equals(point)) continue;
            int dx=point.x-station.x, dy=point.y-station.y;
            int divisor=gcd(dx,dy);
            directions.add(dx/divisor+","+dy/divisor);
        }
        return directions.size();
    }

    static Point best(ArrayList<Point> asteroids){
        Point best=null; int max=-1;
        for (Point point:asteroids) {
            int count=visible(point,asteroids);
            if (count>max) { max=count; best=point; }
        }
        return best;
    }

    public static void main(String[] args) {
        ArrayList<Point> asteroids=reader("Day10_input.txt");
        System.out.println(visible(best(asteroids),asteroids));
    }
}
