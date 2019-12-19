package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	b, err := ioutil.ReadAll(file)
	input := string(b)
	inputArray := strings.Split(input, ",")
	i := 0
	for i < len(inputArray) {
		inputNbr, err := strconv.Atoi(inputArray[i])
		if err != nil {
			log.Fatal(err)
		}
		if inputNbr == 99 {
			break
		}
		address1, err := strconv.Atoi(inputArray[i+1])
		address2, err := strconv.Atoi(inputArray[i+2])
		address3, err := strconv.Atoi(inputArray[i+3])
		noun, err := strconv.Atoi(inputArray[address1])
		verb, err := strconv.Atoi(inputArray[address2])
		if err != nil {
			log.Fatal(err)
		}
		if inputNbr == 1 {
			inputArray[address3] = strconv.Itoa(noun + verb)
		}
		if inputNbr == 2 {
			inputArray[address3] = strconv.Itoa(noun * verb)
		}
		i += 4
	}
	fmt.Printf("First value is: %v\n", inputArray[0])
}
