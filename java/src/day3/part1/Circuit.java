package day3.part1;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class Circuit {
    private List<HashSet<String>> wires = new ArrayList<HashSet<String>>();

    public void addWire(String[] arrOfPath) {
        HashSet<String> points = new HashSet<>();
        int x = 0;
        int y = 0;
        for(String s:arrOfPath) {
            int nbrOfSteps = Integer.parseInt(s.substring(1));
            char direction = s.charAt(0);
            for (int i = 0; i < nbrOfSteps; i++) {
                switch (direction) {
                    case 'U':
                        y++;
                        break;
                    case 'D':
                        y--;
                        break;
                    case 'R':
                        x++;
                        break;
                    case 'L':
                        x--;
                        break;
                }
                String point = Integer.toString(x) + ';' + y;
                points.add(point);
            }
        }
        wires.add(points);
    }

    public int getClosestManhattanDistance() {
        HashSet<String> intersection = new HashSet<>(wires.get(0));
        for(int i = 1; i < wires.size(); i++) {
            intersection.retainAll(wires.get(i));
        }
        int distance = Integer.MAX_VALUE;
        for (String point:intersection) {
            String[] points = point.split(";");
            int x = Integer.parseInt(points[0]);
            int y = Integer.parseInt(points[1]);
            if (Math.abs(x) + Math.abs(y) < distance) {
                distance = Math.abs(x) + Math.abs(y);
            }
        }
        return distance;
    }
}
