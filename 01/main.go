package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var filename string
	if len(os.Args) < 2 {
		filename = "input"
	} else {
		filename = os.Args[1]
	}

	// open file
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	// read and parse input
	var rots []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		var rot int
		fmt.Sscanf(line[1:], "%d", &rot)
		if line[:1] == "L" {
			rot = -rot
		}
		rots = append(rots, rot)
	}
	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	var pos = 50 // starting position
	var count_all, count_end int
	for _, rot := range rots {
		step := 1
		if rot < 0 {
			step = -step
			rot = -rot
		}
		for i := 0; i < rot; i++ {
			pos = (pos + step) % 100
			if pos == 0 {
				count_all++
			}
		}
		if pos == 0 {
			count_end++
		}
	}
	// part 1
	fmt.Println(count_end)
	// part 2
	fmt.Println(count_all)
}
