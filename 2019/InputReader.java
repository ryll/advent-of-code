import java.io.*;
import java.nio.file.*;
import java.util.*;

public class InputReader {

    static String readString(String name){
        try{
            return Files.readString(Paths.get(name)).trim();
        }
        catch (IOException e){
            throw new RuntimeException(e);
        }
    }

    static ArrayList<String> readLines(String name){
        try{
            return new ArrayList<>(Files.readAllLines(Paths.get(name)));
        }
        catch (IOException e){
            throw new RuntimeException(e);
        }
    }

    static long[] readProgram(String name){
        String[] input = readString(name).split(",");
        long[] program = new long[input.length];
        for (int i = 0; i < input.length; i++) program[i] = Long.parseLong(input[i]);
        return program;
    }

    static int[] readIntProgram(String name){
        String[] input = readString(name).split(",");
        int[] program = new int[input.length];
        for (int i = 0; i < input.length; i++) program[i] = Integer.parseInt(input[i]);
        return program;
    }
}
