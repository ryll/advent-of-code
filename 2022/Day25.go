package main

import (
	"fmt"
	"os"
	"strings"
)

func decode(s string) int {
	n := 0
	for _, c := range s {
		n *= 5
		n += map[rune]int{'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}[c]
	}
	return n
}

func encode(n int) string {
	s := ""
	for n > 0 {
		switch r := n % 5; r {
		case 3:
			s, n = "="+s, n+5
		case 4:
			s, n = "-"+s, n+5
		default:
			s = string(rune('0'+r)) + s
		}
		n /= 5
	}
	return s
}

func part1(in string) string {
	n := 0
	for _, l := range strings.Fields(in) {
		n += decode(l)
	}
	return encode(n)
}

func main() {
	b, _ := os.ReadFile("2022/Day25_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
}
