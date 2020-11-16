import java.util.*;

public class Day03B {
    static class MapGuide {
        private String direction;
        private int amount;

        MapGuide(String direction, int amount){
            this.direction = direction;
            this.amount = amount;
        }

        String getDirection(){ return direction; }
        int getAmount(){ return amount; }
    }

    static MapGuide[] reader(String name, int line) {
        String[] input = InputReader.readLines(name).get(line - 1).split(",");
        MapGuide[] output = new MapGuide[input.length];
        for (int i=0; i<input.length; i++) {
            output[i] = new MapGuide(input[i].substring(0,1),Integer.parseInt(input[i].substring(1)));
        }
        return(output);
    }
   
    public static void main(String[] args) {
        MapGuide[] map = reader("Day03_input.txt",1);
        ArrayList<String> posList = new ArrayList<String>();
        posList.add("0,0");
        int posy = 0,posx = 0;
        for (int n = 0; n < map.length; n++) {
            switch (map[n].getDirection()) {
                case "R":
                    for (int i = 0; i < map[n].getAmount(); i++) {
                        posx++;
                        posList.add(posx+","+posy);
                    }
                    break;
                case "L":
                    for (int i = 0; i < map[n].getAmount(); i++) {
                        posx--;
                        posList.add(posx+","+posy);
                    }
                    break;
                case "U":
                    for (int i = 0; i < map[n].getAmount(); i++) {
                        posy++;
                        posList.add(posx+","+posy);
                    }                
                    break;
                case "D":
                    for (int i = 0; i < map[n].getAmount(); i++) {
                        posy--;
                        posList.add(posx+","+posy);
                    }
                    break;
                default:
                    break;
            }
        }
        map = reader("Day03_input.txt",2);
        posy = 0;posx = 0;int dist = 0; int tempdist; int steps = 0;
        
        for (int n = 0; n < map.length; n++) {
            switch (map[n].getDirection()) {
                case "R":
                    for (int i = 0; i < map[n].getAmount(); i++) {
                        posx++;
                        steps++;
                        if (posList.contains(posx+","+posy)) {
                            tempdist = steps+posList.indexOf(posx+","+posy);
                            if (tempdist < dist || dist == 0) {
                                dist = tempdist;                        
                            }
                        }
                    }
                    break;
                case "L":
                    for (int i = 0; i < map[n].getAmount(); i++) {
                        posx--;
                        steps++;
                        if (posList.contains(posx+","+posy)) {
                            tempdist = steps+posList.indexOf(posx+","+posy);
                            if (tempdist < dist || dist == 0) {
                                dist = tempdist;                        
                            }
                        }
                    }
                    break;
                case "U":
                    for (int i = 0; i < map[n].getAmount(); i++) {
                        posy++;
                        steps++;
                        if (posList.contains(posx+","+posy)) {
                            tempdist = steps+posList.indexOf(posx+","+posy);
                            if (tempdist < dist || dist == 0) {
                                dist = tempdist;                        
                            }
                        }
                    }                
                    break;
                case "D":
                    for (int i = 0; i < map[n].getAmount(); i++) {
                        posy--;
                        steps++;
                        if (posList.contains(posx+","+posy)) {
                            tempdist = steps+posList.indexOf(posx+","+posy);
                            if (tempdist < dist || dist == 0) {
                                dist = tempdist;                        
                            }
                        }
                    }
                    break;
                default:
                    break;
                
            }
            System.out.println(map.length+", "+ n +", "+dist);
    
        }
        System.out.println(dist);
    }
}
