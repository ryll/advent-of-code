package main

import (
	"fmt"
	"os"
	"strings"
)

type pt struct{ x, y int }
type state struct {
	p pt
	t int
}

var moves = []pt{{0, 0}, {1, 0}, {-1, 0}, {0, 1}, {0, -1}}
var winds = map[byte]pt{'>': {1, 0}, '<': {-1, 0}, 'v': {0, 1}, '^': {0, -1}}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func blizzards(g []string) []map[pt]bool {
	w, h := len(g[0])-2, len(g)-2
	occ := make([]map[pt]bool, w*h/gcd(w, h))
	for t := range occ {
		occ[t] = map[pt]bool{}
		for y := 1; y <= h; y++ {
			for x := 1; x <= w; x++ {
				if d, ok := winds[g[y][x]]; ok {
					occ[t][pt{((x-1+d.x*t)%w+w)%w + 1, ((y-1+d.y*t)%h+h)%h + 1}] = true
				}
			}
		}
	}
	return occ
}

func travel(g []string, occ []map[pt]bool, from, to pt, t int) int {
	seen, q := map[state]bool{}, []pt{from}
	for ; ; t++ {
		var next []pt
		for _, p := range q {
			for _, m := range moves {
				n := pt{p.x + m.x, p.y + m.y}
				if n == to {
					return t + 1
				}
				if n.y < 0 || n.y >= len(g) || g[n.y][n.x] == '#' || occ[(t+1)%len(occ)][n] {
					continue
				}
				if s := (state{n, (t + 1) % len(occ)}); !seen[s] {
					seen[s] = true
					next = append(next, n)
				}
			}
		}
		q = next
	}
}

func solve(in string) (int, int) {
	g := strings.Split(in, "\n")
	occ := blizzards(g)
	start := pt{strings.IndexByte(g[0], '.'), 0}
	end := pt{strings.IndexByte(g[len(g)-1], '.'), len(g) - 1}
	a := travel(g, occ, start, end, 0)
	b := travel(g, occ, end, start, a)
	return a, travel(g, occ, start, end, b)
}

func main() {
	b, _ := os.ReadFile("2022/Day24_input.txt")
	p1, p2 := solve(strings.TrimRight(string(b), "\n"))
	fmt.Println("Part 1:", p1)
	fmt.Println("Part 2:", p2)
}
