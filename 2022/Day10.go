package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func run(in string) []int {
	x, xs := 1, []int{}
	for _, l := range strings.Split(in, "\n") {
		xs = append(xs, x)
		if strings.HasPrefix(l, "addx") {
			n, _ := strconv.Atoi(l[5:])
			xs = append(xs, x)
			x += n
		}
	}
	return xs
}

func part1(in string) int {
	xs, total := run(in), 0
	for c := 20; c <= 240 && c <= len(xs); c += 40 {
		total += c * xs[c-1]
	}
	return total
}

func part2(in string) string {
	xs, out := run(in), strings.Builder{}
	for i, x := range xs {
		if i%40 == 0 {
			out.WriteByte('\n')
		}
		if d := i%40 - x; d >= -1 && d <= 1 {
			out.WriteByte('#')
		} else {
			out.WriteByte('.')
		}
	}
	return out.String()
}

func main() {
	b, _ := os.ReadFile("2022/Day10_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
