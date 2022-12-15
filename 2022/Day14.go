package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type pt struct{ x, y int }

func scan(in string) (map[pt]bool, int) {
	rock, max := map[pt]bool{}, 0
	for _, l := range strings.Split(in, "\n") {
		var prev pt
		for i, s := range strings.Split(l, " -> ") {
			f := strings.Split(s, ",")
			x, _ := strconv.Atoi(f[0])
			y, _ := strconv.Atoi(f[1])
			if y > max {
				max = y
			}
			if i > 0 {
				dx, dy := sign(x-prev.x), sign(y-prev.y)
				for p := prev; p != (pt{x, y}); p = (pt{p.x + dx, p.y + dy}) {
					rock[p] = true
				}
			}
			rock[pt{x, y}] = true
			prev = pt{x, y}
		}
	}
	return rock, max
}

func sign(n int) int {
	switch {
	case n > 0:
		return 1
	case n < 0:
		return -1
	}
	return 0
}

func pour(in string, floor bool) int {
	rock, max := scan(in)
	for n := 0; ; n++ {
		p := pt{500, 0}
		if rock[p] {
			return n
		}
		for p.y <= max {
			if next := (pt{p.x, p.y + 1}); !rock[next] {
				p = next
			} else if next = (pt{p.x - 1, p.y + 1}); !rock[next] {
				p = next
			} else if next = (pt{p.x + 1, p.y + 1}); !rock[next] {
				p = next
			} else {
				break
			}
		}
		if !floor && p.y > max {
			return n
		}
		rock[p] = true
	}
}

func part1(in string) int { return pour(in, false) }

func part2(in string) int { return pour(in, true) }

func main() {
	b, _ := os.ReadFile("2022/Day14_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
