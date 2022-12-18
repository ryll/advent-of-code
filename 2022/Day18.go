package main

import (
	"fmt"
	"os"
	"strings"
)

type pt struct{ x, y, z int }

func (p pt) neighbours() []pt {
	return []pt{{p.x - 1, p.y, p.z}, {p.x + 1, p.y, p.z}, {p.x, p.y - 1, p.z},
		{p.x, p.y + 1, p.z}, {p.x, p.y, p.z - 1}, {p.x, p.y, p.z + 1}}
}

func parse(in string) map[pt]bool {
	cubes := map[pt]bool{}
	for _, l := range strings.Fields(in) {
		var p pt
		fmt.Sscanf(l, "%d,%d,%d", &p.x, &p.y, &p.z)
		cubes[p] = true
	}
	return cubes
}

func part1(in string) int {
	cubes, n := parse(in), 0
	for c := range cubes {
		for _, v := range c.neighbours() {
			if !cubes[v] {
				n++
			}
		}
	}
	return n
}

func part2(in string) int {
	cubes := parse(in)
	mn, mx := pt{99, 99, 99}, pt{}
	for c := range cubes {
		mn = pt{min(mn.x, c.x-1), min(mn.y, c.y-1), min(mn.z, c.z-1)}
		mx = pt{max(mx.x, c.x+1), max(mx.y, c.y+1), max(mx.z, c.z+1)}
	}
	seen, q, n := map[pt]bool{mn: true}, []pt{mn}, 0
	for len(q) > 0 {
		p := q[0]
		q = q[1:]
		for _, v := range p.neighbours() {
			if v.x < mn.x || v.y < mn.y || v.z < mn.z || v.x > mx.x || v.y > mx.y || v.z > mx.z {
				continue
			}
			if cubes[v] {
				n++
			} else if !seen[v] {
				seen[v] = true
				q = append(q, v)
			}
		}
	}
	return n
}

func main() {
	b, _ := os.ReadFile("2022/Day18_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
