package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func read_input(filename string) ([][2]int, error) {
	var res [][2]int
	file, err := os.Open(filename)
	if err != nil {
		return res, err
	}
	defer file.Close()
	
	scanner := bufio.NewScanner(file)
	// Define a split function that separates on commas.
	onComma := func(data []byte, atEOF bool) (advance int, token []byte, err error) {
		for i := 0; i < len(data); i++ {
			if data[i] == ',' {
				return i + 1, data[:i], nil
			}
		}
		if !atEOF {
			return 0, nil, nil
		}
		return 0, data, bufio.ErrFinalToken
	}
	scanner.Split(onComma)
	for scanner.Scan() {
		var start, end int
		n, err := fmt.Sscanf(scanner.Text(), "%d-%d", &start, &end)
		if err != nil || n != 2 {
			return res, err
		}
		res = append(res, [2]int{start, end})
	}
	if err := scanner.Err(); err != nil {
		return res, err
	}
	return res, nil
}

func is_invalid_id1(num int) bool {
	s := strconv.Itoa(num)
	if len(s) % 2 != 0 {
		return false
	}
	return s[:len(s)/2] == s[len(s)/2:]
}

func is_invalid_id2(num int) bool {
	s := strconv.Itoa(num)
	for sub_len := 1; sub_len <= len(s)/2; sub_len++ {
		if len(s) % sub_len == 0 {
			sub_str := s[:sub_len]
			// test if all  substrings are equal to each other
			all_equal := true
			for i := sub_len; i < len(s); i += sub_len {
				all_equal = all_equal && (sub_str == s[i:i+sub_len])
			}
			if all_equal {
				return true
			}
		}
	}
	return false
}

func main() {
	filename := os.Args[1]
	nums, err := read_input(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	var invalid_ids1, invalid_ids2 []int
	var total_sum1, total_sum2 int64
	for _, num_range := range nums {
		for id := num_range[0]; id <= num_range[1]; id++ {
			if is_invalid_id1(id) {
				invalid_ids1 = append(invalid_ids1, id)
				total_sum1 += int64(id)
			}
			if is_invalid_id2(id) {
				invalid_ids2 = append(invalid_ids2, id)
				total_sum2 += int64(id)
			}
		}
	}

	// part 1
	fmt.Println(total_sum1)
	// part 2
	//for _, id := range invalid_ids2 {
	//	fmt.Println(id)
	//}
	fmt.Println(total_sum2)
}
