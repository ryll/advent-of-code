import java.util.*;

public class Intcode {

    private HashMap<Long, Long> program = new HashMap<>();
    private ArrayDeque<Long> input = new ArrayDeque<>();
    private ArrayDeque<Long> output = new ArrayDeque<>();
    private long n = 0;
    private long relbase = 0;
    private boolean halted = false;

    public Intcode(long[] inProg){
        for (int i = 0; i < inProg.length; i++) {
            program.put((long)i, inProg[i]);
        }
    }

    //old constructor kept for the earlier solutions
    public Intcode(long[] inProg, long value){
        this(inProg);
        addInput(value);
        run();
    }

    //copy a computer, including its current state
    public Intcode(Intcode computer){
        program.putAll(computer.program);
        input.addAll(computer.input);
        output.addAll(computer.output);
        n = computer.n;
        relbase = computer.relbase;
        halted = computer.halted;
    }

    private long get(long address){
        return program.getOrDefault(address, 0L);
    }

    private void set(long address, long value){
        program.put(address, value);
    }

    private int mode(int parameter){
        long modes = get(n)/100;
        for (int i = 1; i < parameter; i++) modes /= 10;
        return (int)(modes%10);
    }

    private long read(int parameter){
        long value = get(n+parameter);
        if (mode(parameter)==0) return get(value);
        if (mode(parameter)==1) return value;
        return get(relbase+value);
    }

    private long address(int parameter){
        long value = get(n+parameter);
        return mode(parameter)==2 ? relbase+value : value;
    }

    public void addInput(long value){
        input.add(value);
    }

    public boolean hasOutput(){
        return !output.isEmpty();
    }

    public long getOutput(){
        return output.isEmpty() ? 0 : output.remove();
    }

    public boolean isHalted(){
        return halted;
    }

    public boolean isWaiting(){
        return !halted && get(n)%100==3 && input.isEmpty();
    }

    public long getMemory(long address){
        return get(address);
    }

    public void setMemory(long address, long value){
        set(address, value);
    }

    //run until the program halts or needs another input
    public void run(){
        while (!halted && !step()) {}
    }

    //run until one output is available, the program halts or needs input
    public boolean runUntilOutput(){
        if (hasOutput()) return true;
        while (!halted && !isWaiting()) {
            step();
            if (hasOutput()) return true;
        }
        return false;
    }

    //return true when execution has to pause
    private boolean step(){
        int op = (int)(get(n)%100);
        switch (op){
            case 1: //addition
                set(address(3), read(1)+read(2)); n += 4; break;
            case 2: //multiplication
                set(address(3), read(1)*read(2)); n += 4; break;
            case 3: //input
                if (input.isEmpty()) return true;
                set(address(1), input.remove()); n += 2; break;
            case 4: //output
                output.add(read(1)); n += 2; break;
            case 5: //jump if true
                n = read(1)!=0 ? read(2) : n+3; break;
            case 6: //jump if false
                n = read(1)==0 ? read(2) : n+3; break;
            case 7: //less than
                set(address(3), read(1)<read(2) ? 1 : 0); n += 4; break;
            case 8: //equals
                set(address(3), read(1)==read(2) ? 1 : 0); n += 4; break;
            case 9: //change relative base
                relbase += read(1); n += 2; break;
            case 99:
                halted = true; return true;
            default:
                throw new IllegalStateException("Unknown opcode: "+op);
        }
        return false;
    }
}
