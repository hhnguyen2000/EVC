public class FutureTuition {

    public static void main(String[] args) {
        double tuition = 10000; // Year 1
        int year = 1;
        
        while (tuition < 20000) {
            tuition *= 1.07;
            year ++;
        }
        
        System.out.printf("Tuition will be doubled in %d years.", year);
    }
}
