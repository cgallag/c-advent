import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Scanner;

public class BuildingReader {

	final static String FILE_NAME = "/home/clgal/development/java_advent/data/day1.txt";
	final static Charset ENCODING = StandardCharsets.UTF_8;

	void calculateFloor() throws IOException {
		int currentFloor = 0;
		int basementCharPos = 0;
		Path path = Paths.get(FILE_NAME);
		try (Scanner scanner = new Scanner(path, ENCODING.name())){
			while (scanner.hasNextLine()){
				String input = scanner.nextLine();
				for (int i=0; i < input.length(); i++) {
					char c = input.charAt(i);
					if (c == ')') {
						currentFloor -= 1;
					} else {
						currentFloor += 1;
					}
					if (currentFloor < 0) {
						basementCharPos = i + 1; 
						break;
					}
				}
			}
		}
		// log(currentFloor);
		log(basementCharPos);
	}

	private static void log(Object aMsg){
		System.out.println(String.valueOf(aMsg));
	}

	public static void main(String[] args) throws IOException {
		BuildingReader reader = new BuildingReader();
		reader.calculateFloor();
	}
}
