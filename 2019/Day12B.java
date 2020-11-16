public class Day12B {
    static long period(long[][] moons, int axis){
        long[] start=new long[moons.length], position=new long[moons.length], velocity=new long[moons.length];
        for (int i=0; i<moons.length; i++) start[i]=position[i]=moons[i][axis];
        long steps=0;
        while (true) {
            for (int i=0; i<moons.length; i++) for (int j=i+1; j<moons.length; j++) {
                long change=Long.compare(position[j],position[i]);
                velocity[i]+=change; velocity[j]-=change;
            }
            boolean same=true;
            for (int i=0; i<moons.length; i++) {
                position[i]+=velocity[i];
                same&=position[i]==start[i] && velocity[i]==0;
            }
            steps++;
            if (same) return steps;
        }
    }
    static long gcd(long a,long b){ while (b!=0) { long temp=a%b; a=b; b=temp; } return a; }
    static long lcm(long a,long b){ return a/gcd(a,b)*b; }
    public static void main(String[] args) {
        long[][] moons=Day12A.reader("Day12_input.txt");
        System.out.println(lcm(lcm(period(moons,0),period(moons,1)),period(moons,2)));
    }
}
