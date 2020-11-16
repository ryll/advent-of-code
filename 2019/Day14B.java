import java.util.*;

public class Day14B {
    public static void main(String[] args) {
        HashMap<String,Day14A.Reaction> reactions=Day14A.reader("Day14_input.txt");
        long ore=1000000000000L,low=0,high=1;
        while (Day14A.ore(reactions,high)<=ore) high*=2;
        while (low+1<high) {
            long middle=(low+high)/2;
            if (Day14A.ore(reactions,middle)<=ore) low=middle;
            else high=middle;
        }
        System.out.println(low);
    }
}
