package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type pt struct{ x, y int }

var moves = map[string]pt{"U": {0, 1}, "D": {0, -1}, "L": {-1, 0}, "R": {1, 0}}

func sign(n int) int {
	switch {
	case n > 0:
		return 1
	case n < 0:
		return -1
	}
	return 0
}

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func rope(in string, n int) int {
	k, seen := make([]pt, n), map[pt]bool{{}: true}
	for _, l := range strings.Split(in, "\n") {
		f := strings.Fields(l)
		d, _ := strconv.Atoi(f[1])
		for ; d > 0; d-- {
			k[0].x += moves[f[0]].x
			k[0].y += moves[f[0]].y
			for i := 1; i < n; i++ {
				dx, dy := k[i-1].x-k[i].x, k[i-1].y-k[i].y
				if abs(dx) > 1 || abs(dy) > 1 {
					k[i].x += sign(dx)
					k[i].y += sign(dy)
				}
			}
			seen[k[n-1]] = true
		}
	}
	return len(seen)
}

func part1(in string) int { return rope(in, 2) }

func part2(in string) int { return rope(in, 10) }

func main() {
	b, _ := os.ReadFile("2022/Day09_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
