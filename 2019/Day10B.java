import java.util.*;

public class Day10B {
    public static void main(String[] args) {
        ArrayList<Day10A.Point> asteroids=Day10A.reader("Day10_input.txt");
        Day10A.Point station=Day10A.best(asteroids);
        TreeMap<Double,ArrayList<Day10A.Point>> directions=new TreeMap<>();

        //group asteroids by clockwise angle, beginning straight up
        for (Day10A.Point point:asteroids) {
            if (point.equals(station)) continue;
            int dx=point.x-station.x, dy=point.y-station.y;
            double angle=Math.atan2(dx,-dy);
            if (angle<0) angle+=Math.PI*2;
            directions.computeIfAbsent(angle,key -> new ArrayList<>()).add(point);
        }
        for (ArrayList<Day10A.Point> line:directions.values()) {
            line.sort(Comparator.comparingInt(point ->
                (point.x-station.x)*(point.x-station.x)+(point.y-station.y)*(point.y-station.y)));
        }

        int destroyed=0;
        while (true) {
            for (ArrayList<Day10A.Point> line:directions.values()) {
                if (line.isEmpty()) continue;
                Day10A.Point point=line.remove(0);
                if (++destroyed==200) {
                    System.out.println(point.x*100+point.y);
                    return;
                }
            }
        }
    }
}
