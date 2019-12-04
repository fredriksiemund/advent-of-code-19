package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func calcFuel(fuel int) int {
	newFuel := (fuel / 3) - 2
	if newFuel <= 0 {
		return 0
	}
	return newFuel + calcFuel(newFuel)
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	totalFuel := 0
	for scanner.Scan() {
		nextLine := scanner.Text()
		nextInt, err := strconv.Atoi(nextLine)
		if err != nil {
			log.Fatal(err)
		}
		totalFuel += calcFuel(nextInt)
	}
	fmt.Printf("Total fuel: %v\n", totalFuel)
}
