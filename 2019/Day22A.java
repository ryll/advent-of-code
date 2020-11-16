import java.math.*;
import java.util.*;

public class Day22A {
    //return coefficients for new position = a*old position+b
    static BigInteger[] shuffle(ArrayList<String> input,BigInteger size){
        BigInteger a=BigInteger.ONE,b=BigInteger.ZERO;
        for (String line:input) {
            BigInteger c,d;
            if (line.equals("deal into new stack")) { c=BigInteger.valueOf(-1); d=BigInteger.valueOf(-1); }
            else if (line.startsWith("cut ")) { c=BigInteger.ONE; d=new BigInteger(line.substring(4)).negate(); }
            else { c=new BigInteger(line.substring("deal with increment ".length())); d=BigInteger.ZERO; }
            a=c.multiply(a).mod(size); b=c.multiply(b).add(d).mod(size);
        }
        return new BigInteger[]{a,b};
    }
    public static void main(String[] args) {
        BigInteger size=BigInteger.valueOf(10007);
        BigInteger[] shuffle=shuffle(InputReader.readLines("Day22_input.txt"),size);
        System.out.println(shuffle[0].multiply(BigInteger.valueOf(2019)).add(shuffle[1]).mod(size));
    }
}
