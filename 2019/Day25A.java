import java.util.*;
import java.util.regex.*;

public class Day25A {
    static ArrayList<String> items=new ArrayList<>(),checkpointPath;
    static String checkpointDirection;
    static HashSet<String> visited=new HashSet<>();
    static HashSet<String> dangerous=new HashSet<>(Arrays.asList(
        "escape pod","giant electromagnet","infinite loop","molten lava","photons"));

    static String output(Intcode computer){
        String text="";
        while (computer.hasOutput()) text+=(char)computer.getOutput();
        return text;
    }
    static String command(Intcode computer,String command){
        for (char value:(command+"\n").toCharArray()) computer.addInput(value);
        computer.run(); return output(computer);
    }
    static String room(String text){
        Matcher matcher=Pattern.compile("== (.+) ==").matcher(text);
        return matcher.find() ? matcher.group(1) : "";
    }
    static ArrayList<String> list(String text,String heading){
        ArrayList<String> values=new ArrayList<>();
        int start=text.indexOf(heading);
        if (start<0) return values;
        for (String line:text.substring(start+heading.length()).split("\n")) {
            if (line.startsWith("- ")) values.add(line.substring(2));
            else if (!line.isEmpty()) break;
        }
        return values;
    }
    static String opposite(String direction){
        if (direction.equals("north")) return "south";
        if (direction.equals("south")) return "north";
        if (direction.equals("east")) return "west";
        return "east";
    }
    static void explore(Intcode computer,String text,ArrayList<String> path){
        String room=room(text);
        if (!visited.add(room)) return;
        for (String item:list(text,"Items here:\n")) if (!dangerous.contains(item)) {
            command(computer,"take "+item); items.add(item);
        }
        ArrayList<String> doors=list(text,"Doors here lead:\n");
        if (room.equals("Security Checkpoint")) {
            String back=path.isEmpty() ? "" : opposite(path.get(path.size()-1));
            for (String door:doors) if (!door.equals(back)) {
                checkpointPath=new ArrayList<>(path); checkpointDirection=door;
            }
            return;
        }
        for (String door:doors) {
            String next=command(computer,door);
            String nextRoom=room(next);
            if (!nextRoom.isEmpty() && !visited.contains(nextRoom)) {
                path.add(door); explore(computer,next,path); path.remove(path.size()-1);
            }
            command(computer,opposite(door));
        }
    }
    public static void main(String[] args) {
        Intcode computer=new Intcode(InputReader.readProgram("Day25_input.txt")); computer.run();
        explore(computer,output(computer),new ArrayList<>());
        if (checkpointPath==null) throw new IllegalStateException("Security checkpoint not found");
        for (String direction:checkpointPath) command(computer,direction);
        for (String item:items) command(computer,"drop "+item);
        for (int mask=0; mask<(1<<items.size()); mask++) {
            for (int i=0; i<items.size(); i++) if ((mask&(1<<i))!=0) command(computer,"take "+items.get(i));
            String result=command(computer,checkpointDirection);
            if (!result.contains("Alert!")) {
                Matcher code=Pattern.compile("\\d+").matcher(result);
                if (code.find()) System.out.println(code.group());
                else System.out.println(result);
                return;
            }
            for (int i=0; i<items.size(); i++) if ((mask&(1<<i))!=0) command(computer,"drop "+items.get(i));
        }
    }
}
