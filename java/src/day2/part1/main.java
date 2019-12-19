package day2.part1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

public class main {
    public static void main(String[] args) throws IOException {
        File file = new File("src/day2/input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        String input = br.readLine();
        br.close();
        Program program = new Program(input);
        program.runProgram();
        HashMap<Integer, Integer> result = program.getProgram();
        System.out.println(result.get(0));
    }

}
