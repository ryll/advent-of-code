public class Day23B {
    public static void main(String[] args) {
        Day23A.Network network=new Day23A.Network(InputReader.readProgram("Day23_input.txt"));
        long natX=0,natY=0,lastY=Long.MIN_VALUE; boolean hasNat=false;
        while (true) {
            boolean activity=false;
            for (int i=0; i<50; i++) {
                if (network.input[i].isEmpty()) network.computers[i].addInput(-1);
                else {
                    activity=true;
                    while (!network.input[i].isEmpty()) network.computers[i].addInput(network.input[i].remove());
                }
                network.computers[i].run();
                while (network.computers[i].hasOutput()) {
                    activity=true;
                    int address=(int)network.computers[i].getOutput();
                    long x=network.computers[i].getOutput(),y=network.computers[i].getOutput();
                    if (address==255) { natX=x; natY=y; hasNat=true; }
                    else { network.input[address].add(x); network.input[address].add(y); }
                }
            }
            if (!activity && hasNat) {
                if (natY==lastY) { System.out.println(natY); return; }
                lastY=natY; network.input[0].add(natX); network.input[0].add(natY);
            }
        }
    }
}
