package main

import (
	"fmt"
	"os"
	"strings"
)

func count(in string, f func(a, b, c, d int) bool) int {
	n := 0
	for _, l := range strings.Fields(in) {
		var a, b, c, d int
		fmt.Sscanf(l, "%d-%d,%d-%d", &a, &b, &c, &d)
		if f(a, b, c, d) {
			n++
		}
	}
	return n
}

func part1(in string) int {
	return count(in, func(a, b, c, d int) bool { return a <= c && b >= d || c <= a && d >= b })
}

func part2(in string) int {
	return count(in, func(a, b, c, d int) bool { return a <= d && c <= b })
}

func main() {
	b, _ := os.ReadFile("2022/Day04_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
