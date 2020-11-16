public class Day16A {
    static int[] reader(String name){
        String input=InputReader.readString(name);
        int[] signal=new int[input.length()];
        for (int i=0; i<input.length(); i++) signal[i]=input.charAt(i)-'0';
        return signal;
    }
    static int[] phase(int[] signal){
        int[] result=new int[signal.length];
        for (int i=0; i<signal.length; i++) {
            int sum=0,repeat=i+1;
            for (int j=0; j<signal.length; j++) {
                int pattern=((j+1)/repeat)%4;
                if (pattern==1) sum+=signal[j];
                else if (pattern==3) sum-=signal[j];
            }
            result[i]=Math.abs(sum)%10;
        }
        return result;
    }
    public static void main(String[] args) {
        int[] signal=reader("Day16_input.txt");
        for (int i=0; i<100; i++) signal=phase(signal);
        for (int i=0; i<8; i++) System.out.print(signal[i]);
        System.out.println();
    }
}
