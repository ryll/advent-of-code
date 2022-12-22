package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type v3 struct{ x, y, z int }

func (a v3) add(b v3) v3  { return v3{a.x + b.x, a.y + b.y, a.z + b.z} }
func (a v3) sub(b v3) v3  { return v3{a.x - b.x, a.y - b.y, a.z - b.z} }
func (a v3) mul(n int) v3 { return v3{a.x * n, a.y * n, a.z * n} }
func (a v3) neg() v3      { return v3{-a.x, -a.y, -a.z} }

type basis struct{ o, r, d, n v3 }
type key struct{ p, n v3 }
type cell struct {
	x, y int
	r, d v3
}

var dirs = [4][2]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}

func parse(in string) ([]string, []string) {
	p := strings.SplitN(in, "\n\n", 2)
	s := strings.TrimSpace(p[1])
	var path []string
	for i := 0; i < len(s); {
		if s[i] == 'L' || s[i] == 'R' {
			path = append(path, s[i:i+1])
			i++
			continue
		}
		j := i
		for j < len(s) && s[j] >= '0' && s[j] <= '9' {
			j++
		}
		path = append(path, s[i:j])
		i = j
	}
	return strings.Split(p[0], "\n"), path
}

func at(g []string, x, y int) byte {
	if y < 0 || y >= len(g) || x < 0 || x >= len(g[y]) {
		return ' '
	}
	return g[y][x]
}

func facing(c cell, h v3) int {
	switch h {
	case c.r:
		return 0
	case c.d:
		return 1
	case c.r.neg():
		return 2
	}
	return 3
}

func part1(in string) int {
	g, path := parse(in)
	x, y, f := strings.IndexByte(g[0], '.'), 0, 0
	for _, t := range path {
		switch t {
		case "L":
			f = (f + 3) % 4
		case "R":
			f = (f + 1) % 4
		default:
			n, _ := strconv.Atoi(t)
			for ; n > 0; n-- {
				nx, ny := x+dirs[f][0], y+dirs[f][1]
				if at(g, nx, ny) == ' ' {
					for nx, ny = x, y; at(g, nx-dirs[f][0], ny-dirs[f][1]) != ' '; nx, ny = nx-dirs[f][0], ny-dirs[f][1] {
					}
				}
				if at(g, nx, ny) == '#' {
					break
				}
				x, y = nx, ny
			}
		}
	}
	return 1000*(y+1) + 4*(x+1) + f
}

func part2(in string) int {
	g, path := parse(in)
	n := 0
	for _, row := range g {
		n += len(strings.ReplaceAll(row, " ", ""))
	}
	side := 1
	for side*side*6 < n {
		side++
	}
	f0 := strings.IndexByte(g[0], '.') / side
	faces := map[[2]int]basis{{f0, 0}: {v3{}, v3{1, 0, 0}, v3{0, 1, 0}, v3{0, 0, -1}}}
	for q := [][2]int{{f0, 0}}; len(q) > 0; q = q[1:] {
		fc := q[0]
		b := faces[fc]
		next := [4]basis{
			{b.o.add(b.r.mul(side - 1)), b.n.neg(), b.d, b.r},
			{b.o.add(b.d.mul(side - 1)), b.r, b.n.neg(), b.d},
			{b.o.sub(b.n.mul(side - 1)), b.n, b.d, b.r.neg()},
			{b.o.sub(b.n.mul(side - 1)), b.r, b.n, b.d.neg()},
		}
		for i, nb := range next {
			c := [2]int{fc[0] + dirs[i][0], fc[1] + dirs[i][1]}
			if _, ok := faces[c]; ok || at(g, c[0]*side, c[1]*side) == ' ' {
				continue
			}
			faces[c] = nb
			q = append(q, c)
		}
	}
	m3, rev := map[key]cell{}, map[[2]int]key{}
	for fc, b := range faces {
		for j := 0; j < side; j++ {
			for i := 0; i < side; i++ {
				k := key{b.o.add(b.r.mul(i)).add(b.d.mul(j)), b.n}
				xy := [2]int{fc[0]*side + i, fc[1]*side + j}
				m3[k] = cell{xy[0], xy[1], b.r, b.d}
				rev[xy] = k
			}
		}
	}
	st := rev[[2]int{strings.IndexByte(g[0], '.'), 0}]
	p, nm, h := st.p, st.n, m3[st].r
	for _, t := range path {
		if t == "L" || t == "R" {
			c := m3[key{p, nm}]
			f := facing(c, h)
			if t == "L" {
				f = (f + 3) % 4
			} else {
				f = (f + 1) % 4
			}
			h = [4]v3{c.r, c.d, c.r.neg(), c.d.neg()}[f]
			continue
		}
		steps, _ := strconv.Atoi(t)
		for ; steps > 0; steps-- {
			np, nn, nh := p.add(h), nm, h
			if _, ok := m3[key{np, nn}]; !ok {
				np, nn, nh = p, h, nm.neg()
			}
			c := m3[key{np, nn}]
			if g[c.y][c.x] == '#' {
				break
			}
			p, nm, h = np, nn, nh
		}
	}
	c := m3[key{p, nm}]
	return 1000*(c.y+1) + 4*(c.x+1) + facing(c, h)
}

func main() {
	b, _ := os.ReadFile("2022/Day22_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
