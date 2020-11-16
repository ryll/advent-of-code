import java.math.*;

public class Day22B {
    public static void main(String[] args) {
        BigInteger size=new BigInteger("119315717514047");
        BigInteger repeats=new BigInteger("101741582076661");
        BigInteger[] shuffle=Day22A.shuffle(InputReader.readLines("Day22_input.txt"),size);
        BigInteger a=shuffle[0],b=shuffle[1];
        BigInteger repeatedA=a.modPow(repeats,size);
        BigInteger repeatedB=a.equals(BigInteger.ONE)
            ? b.multiply(repeats).mod(size)
            : b.multiply(repeatedA.subtract(BigInteger.ONE)).multiply(a.subtract(BigInteger.ONE).modInverse(size)).mod(size);
        BigInteger card=BigInteger.valueOf(2020).subtract(repeatedB).multiply(repeatedA.modInverse(size)).mod(size);
        System.out.println(card);
    }
}
