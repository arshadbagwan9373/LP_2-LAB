import java.util.Scanner;

public class Chatbot {

    private static final String EXIT_COMMAND = "bye";

    // Predefined responses
    private static final String COURSES_RESPONSE = 
        "We offer a variety of courses including:\n" +
        "\t- Engineering\n" +
        "\t- Pharma\n" +
        "\t- Management\n" +
        "\t- C-DAC\n" +
        "\t- MCA\n" +
        "Please visit our website for more details.";

    private static final String FEES_RESPONSE = 
        "The fee structure varies for each course. " +
        "Please visit our website or contact our admissions department for detailed information.";

    private static final String FACULTY_RESPONSE = 
        "We have a highly qualified and experienced faculty who are experts in their respective fields.";

    private static final String FEATURES_RESPONSE = 
        "Our courses are designed to provide comprehensive knowledge and practical skills. " +
        "They include hands-on projects, interactive learning materials, and experienced faculty guidance.";

    private static final String CONTACT_RESPONSE = 
        "For further assistance, please contact us through our website.";

    private static final String DEFAULT_RESPONSE = 
        "I'm sorry, I didn't understand. Could you please rephrase or ask another question?";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        greetUser();

        while (true) {
            System.out.print("User: ");
            String userInput = scanner.nextLine().trim();

            if (isExitCommand(userInput)) {
                sayGoodbye();
                break;
            }

            String response = getBotResponse(userInput);
            System.out.println("Chatbot: " + response);
        }

        scanner.close();
    }

    private static void greetUser() {
        System.out.println("----Welcome to MET-BKC----\n");
        System.out.println("How can I assist you today?");
    }

    private static boolean isExitCommand(String input) {
        return input.equalsIgnoreCase(EXIT_COMMAND);
    }

    private static void sayGoodbye() {
        System.out.println("Chatbot: Goodbye! Have a nice day!");
    }

    private static String getBotResponse(String userInput) {
        userInput = userInput.toLowerCase();

        if (userInput.contains("courses")) return COURSES_RESPONSE;
        if (userInput.contains("fees")) return FEES_RESPONSE;
        if (userInput.contains("faculty")) return FACULTY_RESPONSE;
        if (userInput.contains("features")) return FEATURES_RESPONSE;
        if (userInput.contains("contact")) return CONTACT_RESPONSE;

        return DEFAULT_RESPONSE;
    }
}
