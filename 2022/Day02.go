package main

import (
	"fmt"
	"os"
	"strings"
)

func score(in string, f func(a, b int) int) int {
	total := 0
	for _, l := range strings.Split(in, "\n") {
		if l == "" {
			continue
		}
		total += f(int(l[0]-'A'), int(l[2]-'X'))
	}
	return total
}

func part1(in string) int {
	return score(in, func(a, b int) int { return b + 1 + (b-a+4)%3*3 })
}

func part2(in string) int {
	return score(in, func(a, b int) int { return (a+b+2)%3 + 1 + b*3 })
}

func main() {
	b, _ := os.ReadFile("2022/Day02_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
