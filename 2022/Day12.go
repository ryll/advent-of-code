package main

import (
	"fmt"
	"os"
	"strings"
)

type pt struct{ x, y int }

func height(c byte) byte {
	switch c {
	case 'S':
		return 'a'
	case 'E':
		return 'z'
	}
	return c
}

func climb(in string) (int, int) {
	g := strings.Fields(in)
	var end pt
	for i := range g {
		for j := range g[i] {
			if g[i][j] == 'E' {
				end = pt{j, i}
			}
		}
	}
	dist, q := map[pt]int{end: 0}, []pt{end}
	start, low := -1, -1
	for len(q) > 0 {
		p := q[0]
		q = q[1:]
		c := g[p.y][p.x]
		if c == 'S' && start < 0 {
			start = dist[p]
		}
		if height(c) == 'a' && low < 0 {
			low = dist[p]
		}
		for _, d := range []pt{{0, 1}, {0, -1}, {1, 0}, {-1, 0}} {
			n := pt{p.x + d.x, p.y + d.y}
			if n.y < 0 || n.y >= len(g) || n.x < 0 || n.x >= len(g[n.y]) {
				continue
			}
			if _, ok := dist[n]; !ok && height(c)-height(g[n.y][n.x]) <= 1 {
				dist[n] = dist[p] + 1
				q = append(q, n)
			}
		}
	}
	return start, low
}

func main() {
	b, _ := os.ReadFile("2022/Day12_input.txt")
	in := strings.TrimRight(string(b), "\n")
	p1, p2 := climb(in)
	fmt.Println("Part 1:", p1)
	fmt.Println("Part 2:", p2)
}
