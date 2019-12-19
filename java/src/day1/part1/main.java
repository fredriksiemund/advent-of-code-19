package day1.part1;

import java.io.*;

public class main {
    public static void main(String[] args) throws IOException {
        File file = new File("src/day1/input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;
        int total = 0;
        while ((st = br.readLine()) != null) {
            total += Integer.parseInt(st) / 3 - 2;
        }
        System.out.println(total);
    }
}
