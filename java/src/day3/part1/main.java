package day3.part1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class main {
    public static void main(String[] args) throws IOException {
        File file = new File("src/day3/input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        Circuit circuit = new Circuit();
        String path;
        while((path = br.readLine()) != null) {
            String[] arrOfPath = path.split(",");
            circuit.addWire(arrOfPath);
        }
        System.out.println(circuit.getClosestManhattanDistance());
    }
}
