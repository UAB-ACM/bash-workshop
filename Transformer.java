import java.util.Scanner;


public class Transformer {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		try {
			transformInput(scanner);
		} 
		catch (NumberFormatException e) {}
		finally {
			scanner.close();
		}
	}

	static void transformInput(Scanner scanner) {
		while (scanner.hasNextLine()) {
			String line = scanner.nextLine();
			int number = Integer.parseInt(line);
			System.out.println(number * number);
		}
	}

}