public class Reindeer {

	public int speed = 0;
	public int flyTime = 0;
	public int restTime = 0;
	public boolean isFlying = true;
	public int timeSpent = 0;	
	public int distance = 0;

	public Reindeer(int s, int ft, int rt) {
		speed = s;
		flyTime = ft;
		restTime = rt;
	}

	public int distanceTraveled() {
		if (isFlying) {
			distance += speed;
			timeSpent += 1;
			if (timeSpent == flyTime) {
				isFlying = false;
				timeSpent = 0;
			}
		} else {
			timeSpent += 1;
			if (timeSpent == restTime) { 
				isFlying = true;
				timeSpent = 0;
			}
		}
		return distance;
	}
	
}