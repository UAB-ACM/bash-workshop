import java.util.Random;

public class Generator {


	public static void main(String[] args) {
		Random rand = new Random();
		try {
			printRandomNumbers(rand);
		} 
		catch (InterruptedException e) {}
	}

	static void printRandomNumbers(Random rand) throws InterruptedException {
		for (int i = 0; i < 30; i++) {
			Thread.sleep(500);
			if (rand.nextFloat() <= 0.1f) {
				System.err.println("Error on " + i);
				continue;
			}
			System.out.println(i);
		}
	}

}