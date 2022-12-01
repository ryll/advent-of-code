package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func totals(in string) []int {
	var t []int
	for _, b := range strings.Split(in, "\n\n") {
		s := 0
		for _, l := range strings.Fields(b) {
			n, _ := strconv.Atoi(l)
			s += n
		}
		t = append(t, s)
	}
	slices.Sort(t)
	return t
}

func part1(in string) int {
	t := totals(in)
	return t[len(t)-1]
}

func part2(in string) int {
	t := totals(in)
	return t[len(t)-1] + t[len(t)-2] + t[len(t)-3]
}

func main() {
	b, _ := os.ReadFile("2022/Day01_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
