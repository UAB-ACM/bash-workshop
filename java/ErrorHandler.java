import java.util.Scanner;

public class ErrorHandler {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		while (scanner.hasNextLine()) {
			String line = scanner.nextLine();
			handleError(line);
		}
		scanner.close();
	}

	static void handleError(String error) {
		System.out.println("Handled " + error);
	}

}