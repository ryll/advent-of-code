package main

import (
	"fmt"
	"os"
	"strings"
)

type pt struct{ x, y int }

var checks = [4][3]pt{
	{{-1, -1}, {0, -1}, {1, -1}},
	{{-1, 1}, {0, 1}, {1, 1}},
	{{-1, -1}, {-1, 0}, {-1, 1}},
	{{1, -1}, {1, 0}, {1, 1}},
}

func parse(in string) map[pt]bool {
	elves := map[pt]bool{}
	for y, l := range strings.Fields(in) {
		for x, c := range l {
			if c == '#' {
				elves[pt{x, y}] = true
			}
		}
	}
	return elves
}

func spread(elves map[pt]bool, rounds int) (map[pt]bool, int) {
	for r := 0; ; r++ {
		if r == rounds {
			return elves, r
		}
		prop, count := map[pt]pt{}, map[pt]int{}
		for e := range elves {
			free := [4]bool{}
			any := false
			for d := 0; d < 4; d++ {
				free[d] = true
				for _, c := range checks[d] {
					if elves[pt{e.x + c.x, e.y + c.y}] {
						free[d], any = false, true
					}
				}
			}
			if !any {
				continue
			}
			for i := 0; i < 4; i++ {
				if d := (r + i) % 4; free[d] {
					t := pt{e.x + checks[d][1].x, e.y + checks[d][1].y}
					prop[e] = t
					count[t]++
					break
				}
			}
		}
		if len(prop) == 0 {
			return elves, r + 1
		}
		next := map[pt]bool{}
		for e := range elves {
			if t, ok := prop[e]; ok && count[t] == 1 {
				next[t] = true
			} else {
				next[e] = true
			}
		}
		elves = next
	}
}

func part1(in string) int {
	elves, _ := spread(parse(in), 10)
	mn, mx := pt{1 << 30, 1 << 30}, pt{-1 << 30, -1 << 30}
	for e := range elves {
		mn = pt{min(mn.x, e.x), min(mn.y, e.y)}
		mx = pt{max(mx.x, e.x), max(mx.y, e.y)}
	}
	return (mx.x-mn.x+1)*(mx.y-mn.y+1) - len(elves)
}

func part2(in string) int {
	_, r := spread(parse(in), -1)
	return r
}

func main() {
	b, _ := os.ReadFile("2022/Day23_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
