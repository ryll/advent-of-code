import java.util.*;

public class Day08B {

    //method to read file and return as array
    static ArrayList<String> reader(String name){
        String input = InputReader.readString(name);
        ArrayList<String> layers = new ArrayList<>();

        while (!input.isEmpty()) {
            layers.add(input.substring(0, 150));
            input = input.substring(150);
        }
        return(layers);
    }

    public static void main(String[] args) {
        //get input
        ArrayList<String> layers = reader("Day08_input.txt");
        String image = "";


        //get decoded image
        for (int i = 0; i < 150; i++) {
            for (String layer : layers) {
                if (layer.charAt(i)=='0') {
                    image += '.';
                    break;
                }
                else if (layer.charAt(i)=='1') {
                    image += '#';
                    break;
                }
            }
        }
        while (!image.isEmpty()) {
            System.out.println(image.substring(0, 25));
            image = image.substring(25);
        }
    }

}
