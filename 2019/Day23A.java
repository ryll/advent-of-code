import java.util.*;

public class Day23A {
    @SuppressWarnings("unchecked")
    static class Network {
        Intcode[] computers=new Intcode[50];
        ArrayDeque<Long>[] input=new ArrayDeque[50];
        Network(long[] program){
            for (int i=0; i<50; i++) {
                computers[i]=new Intcode(program); computers[i].addInput(i); computers[i].run();
                input[i]=new ArrayDeque<>();
            }
        }
    }
    public static void main(String[] args) {
        Network network=new Network(InputReader.readProgram("Day23_input.txt"));
        while (true) for (int i=0; i<50; i++) {
            if (network.input[i].isEmpty()) network.computers[i].addInput(-1);
            else while (!network.input[i].isEmpty()) network.computers[i].addInput(network.input[i].remove());
            network.computers[i].run();
            while (network.computers[i].hasOutput()) {
                int address=(int)network.computers[i].getOutput();
                long x=network.computers[i].getOutput(),y=network.computers[i].getOutput();
                if (address==255) { System.out.println(y); return; }
                network.input[address].add(x); network.input[address].add(y);
            }
        }
    }
}
