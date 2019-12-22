package day3;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

public class Circuit {
    private List<HashSet<String>> wires = new ArrayList<>();
    private List<HashMap<String, Integer>> paths = new ArrayList<>();

    public void addWire(String[] arrOfPath) {
        HashSet<String> points = new HashSet<>();
        HashMap<String, Integer> path = new HashMap<>();
        int x = 0, y = 0, counter = 0;
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
                String point = new StringBuilder().append(x).append(";").append(y).toString();
                points.add(point);
                if (!path.containsKey(point)) {
                    path.put(point, counter);
                }
                counter++;
            }
        }
        wires.add(points);
        paths.add(path);
    }

    private HashSet<String> getIntersections() {
        HashSet<String> intersection = new HashSet<>(wires.get(0));
        for(int i = 1; i < wires.size(); i++) {
            intersection.retainAll(wires.get(i));
        }
        return intersection;
    }

    public int getClosestManhattanDistance() {
        HashSet<String> intersection = getIntersections();
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

    public int getShortestPath() {
        HashSet<String> intersection = getIntersections();
        int distance = Integer.MAX_VALUE;
        for (String point:intersection) {
            int tempDistance = 0;
            for (HashMap<String, Integer> list:paths) {
                tempDistance += list.get(point);
            }
            if (tempDistance < distance) {
                distance = tempDistance;
            }
        }
        return distance + wires.size();
    }
}
