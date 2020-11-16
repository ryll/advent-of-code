public class Day16B {
    public static void main(String[] args) {
        int[] original=Day16A.reader("Day16_input.txt");
        int offset=0;
        for (int i=0; i<7; i++) offset=offset*10+original[i];
        int length=original.length*10000;
        if (offset<length/2) throw new IllegalArgumentException("Fast method requires offset in second half");
        int[] signal=new int[length-offset];
        for (int i=offset; i<length; i++) signal[i-offset]=original[i%original.length];
        for (int phase=0; phase<100; phase++) {
            for (int i=signal.length-2; i>=0; i--) signal[i]=(signal[i]+signal[i+1])%10;
        }
        for (int i=0; i<8; i++) System.out.print(signal[i]);
        System.out.println();
    }
}
