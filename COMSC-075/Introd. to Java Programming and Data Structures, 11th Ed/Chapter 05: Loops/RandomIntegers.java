import java.util.Random;

/*
 * Write a program that creates a Random object with seed 1000
 * and displays the first 50 random integers between 0 and 100
 * using the nextInt(100) method.
 */

public class RandomIntegers {

    public static void main(String[] args) {
        Random rand = new Random(1000);
        
        for (int i = 0; i < 50; i++) {
            System.out.println(rand.nextInt(100));
        }
    }
}
