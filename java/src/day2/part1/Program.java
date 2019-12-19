package day2.part1;

import java.util.HashMap;

public class Program {
    HashMap<Integer, Integer> program;

    public Program (String input) {
        program = new HashMap<Integer, Integer>();
        String[] arrOfInput = input.split(",");
        for(int i = 0; i < arrOfInput.length; i++) {
            program.put(i, Integer.parseInt(arrOfInput[i]));
        }
    }

    public void runProgram() {
        int i = 0;
        int instruction;
        while ((instruction = program.get(i)) != 99) {
            int address1 = program.get(i+1);
            int address2 = program.get(i+2);
            int address3 = program.get(i+3);
            switch (instruction) {
                case 1:
                    program.put(address3, program.get(address1) + program.get(address2));
                    break;
                case 2:
                    program.put(address3, program.get(address1) * program.get(address2));
                    break;
            }
            i += 4;
        }
    }

    public int getValueAtAddress(int address) {
        return program.get(address);
    }
}
