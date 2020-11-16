public class Day13B {
    public static void main(String[] args) {
        Intcode computer=new Intcode(InputReader.readProgram("Day13_input.txt"));
        computer.setMemory(0,2);
        long score=0,paddle=0,ball=0;
        while (!computer.isHalted()) {
            computer.run();
            while (computer.hasOutput()) {
                long x=computer.getOutput(), y=computer.getOutput(), tile=computer.getOutput();
                if (x==-1 && y==0) score=tile;
                else if (tile==3) paddle=x;
                else if (tile==4) ball=x;
            }
            if (computer.isWaiting()) computer.addInput(Long.compare(ball,paddle));
        }
        System.out.println(score);
    }
}
