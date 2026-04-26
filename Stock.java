import java.util.Scanner;

public class Stock {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        printWelcome();

        String trend = askQuestion("What is the current market trend? (Upwards/Downwards):", sc);
        String fundamentals = askQuestion("How are the fundamentals of the company? (Strong/Weak):", sc);
        String indicators = askQuestion("What do the technical indicators suggest? (Positive/Negative):", sc);

        boolean shouldBuy = evaluate(trend, fundamentals, indicators);
        printResult(shouldBuy);

        sc.close();
    }

    private static void printWelcome() {
        System.out.println("\n\n-------------------xx-------------------");
        System.out.println("Welcome to the Stock Market Trading System!");
        System.out.println("-------------------xx-------------------");
        System.out.println("\nPlease answer the following questions:");
    }

    private static String askQuestion(String question, Scanner scanner) {
        System.out.println(question + " ");
        return scanner.nextLine().trim().toLowerCase(); // normalize input
    }

    private static boolean evaluate(String trend, String fundamentals, String indicators) {
        return trend.equals("upwards") 
            && fundamentals.equals("strong") 
            && indicators.equals("positive");
    }

    private static void printResult(boolean shouldBuy) {
        System.out.println("-------------------xx-------------------");
        System.out.println("Recommendation: " + (shouldBuy ? "Buy the stock!" : "Do not buy the stock."));
        System.out.println("-------------------xx-------------------");
    }
}
