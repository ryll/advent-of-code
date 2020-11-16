public class Day01B {

    static int fuelCount(int n){
        n = n/3-2;
        if (n<0){
            return(0);
        }
        return(n+fuelCount(n));
    }

    public static void main(String[] args) {
        int fuel = 0;
        for (String line : InputReader.readLines("Day01_input.txt")) {
            int input = Integer.parseInt(line);
            fuel = fuel+fuelCount(input);
        }
        System.out.println(fuel);
    }
}
