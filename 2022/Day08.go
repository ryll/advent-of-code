package main

import (
	"fmt"
	"os"
	"strings"
)

var dirs = [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func look(g []string, i, j, di, dj int) (int, bool) {
	d := 0
	for y, x := i+di, j+dj; y >= 0 && y < len(g) && x >= 0 && x < len(g[y]); y, x = y+di, x+dj {
		d++
		if g[y][x] >= g[i][j] {
			return d, false
		}
	}
	return d, true
}

func part1(in string) int {
	g, n := strings.Fields(in), 0
	for i := range g {
		for j := range g[i] {
			for _, d := range dirs {
				if _, edge := look(g, i, j, d[0], d[1]); edge {
					n++
					break
				}
			}
		}
	}
	return n
}

func part2(in string) int {
	g, best := strings.Fields(in), 0
	for i := range g {
		for j := range g[i] {
			s := 1
			for _, d := range dirs {
				v, _ := look(g, i, j, d[0], d[1])
				s *= v
			}
			if s > best {
				best = s
			}
		}
	}
	return best
}

func main() {
	b, _ := os.ReadFile("2022/Day08_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
