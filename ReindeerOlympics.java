import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Scanner;
import java.util.HashMap;
import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class ReindeerOlympics {

	final static String FILE_NAME = "/home/clgal/development/java_advent/data/day14.txt";
	final static Charset ENCODING = StandardCharsets.UTF_8;
	final static int RACE_TIME = 2503;

	void getWinningReindeer() throws IOException {
		List<Reindeer> reindeers = new ArrayList<Reindeer>();
		int maxDist = 0;

		Path path = Paths.get(FILE_NAME);
		try (Scanner scanner = new Scanner(path, ENCODING.name())){
			while (scanner.hasNextLine()){
				String input = scanner.nextLine();
				reindeers.add(makeReindeer(input));
			}
		}

		int[] points = new int[reindeers.size()];
		int[] currentDistances = new int[reindeers.size()];

		for (int k = 0; k < reindeers.size(); k++) {
			points[k] = 0;
		}

		log("about to start race");
		for (int i = 0; i < RACE_TIME; i++) {
			for (int j = 0; j < reindeers.size(); j++) {
				Reindeer currReindeer = reindeers.get(j);
				int currDist = currReindeer.distanceTraveled();
				currentDistances[j] = currDist;
				if (currDist > maxDist) {
					maxDist = currDist;
				}
			} 
			
			for (int k = 0; k < points.length; k++) {
				if (currentDistances[k] == maxDist) {
					points[k] += 1;
				}
			}
		}
		int maxPoints = 0;
		for (int m = 0; m < points.length; m++) {
			int reindeerPoints = points[m];
			if (reindeerPoints > maxPoints) {
				maxPoints = reindeerPoints;
			}
		}
		log(maxPoints);
	}

	private static Reindeer makeReindeer(String reindeerStr) {
		String whitespaceStr = reindeerStr.replaceAll("[\\D]", " ");
		Scanner scanner = new Scanner(whitespaceStr);
		int speed = scanner.nextInt();
		int flyTime = scanner.nextInt();
		int restTime = scanner.nextInt();
		Reindeer reindeer = new Reindeer(speed, flyTime, restTime);
		return reindeer;
	}

	private static void log(Object aMsg){
		System.out.println(String.valueOf(aMsg));
	}

	public static void main(String[] args) throws IOException {
		ReindeerOlympics reindeers = new ReindeerOlympics();
		reindeers.getWinningReindeer();
	}
}


