import java.util.*;

public class Day14A {
    static class Chemical {
        long amount; String name;
        Chemical(String value){
            String[] parts=value.trim().split(" ");
            amount=Long.parseLong(parts[0]); name=parts[1];
        }
    }
    static class Reaction {
        long amount;
        ArrayList<Chemical> input=new ArrayList<>();
    }
    static HashMap<String,Reaction> reader(String name){
        HashMap<String,Reaction> reactions=new HashMap<>();
        for (String line:InputReader.readLines(name)) {
            String[] sides=line.split(" => ");
            Chemical result=new Chemical(sides[1]);
            Reaction reaction=new Reaction(); reaction.amount=result.amount;
            for (String value:sides[0].split(",")) reaction.input.add(new Chemical(value));
            reactions.put(result.name,reaction);
        }
        return reactions;
    }
    static long ore(HashMap<String,Reaction> reactions,long fuel){
        HashMap<String,Long> needed=new HashMap<>(), spare=new HashMap<>();
        needed.put("FUEL",fuel);
        long ore=0;
        while (!needed.isEmpty()) {
            String name=needed.keySet().iterator().next();
            long amount=needed.remove(name);
            long use=Math.min(amount,spare.getOrDefault(name,0L));
            amount-=use; spare.put(name,spare.getOrDefault(name,0L)-use);
            if (amount==0) continue;
            if (name.equals("ORE")) { ore+=amount; continue; }
            Reaction reaction=reactions.get(name);
            long batches=(amount+reaction.amount-1)/reaction.amount;
            spare.put(name,spare.getOrDefault(name,0L)+batches*reaction.amount-amount);
            for (Chemical chemical:reaction.input)
                needed.put(chemical.name,needed.getOrDefault(chemical.name,0L)+chemical.amount*batches);
        }
        return ore;
    }
    public static void main(String[] args) {
        System.out.println(ore(reader("Day14_input.txt"),1));
    }
}
