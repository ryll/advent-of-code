package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

type monkey struct {
	items       []int
	op          byte
	arg         int
	div, t, f   int
	inspections int
}

func parse(in string) []*monkey {
	var ms []*monkey
	for _, b := range strings.Split(in, "\n\n") {
		l := strings.Split(b, "\n")
		m := &monkey{}
		for _, s := range strings.Split(strings.SplitN(l[1], ": ", 2)[1], ", ") {
			n, _ := strconv.Atoi(s)
			m.items = append(m.items, n)
		}
		f := strings.Fields(l[2])
		m.op = f[len(f)-2][0]
		if f[len(f)-1] != "old" {
			m.arg, _ = strconv.Atoi(f[len(f)-1])
		}
		for i, p := range []*int{&m.div, &m.t, &m.f} {
			g := strings.Fields(l[3+i])
			*p, _ = strconv.Atoi(g[len(g)-1])
		}
		ms = append(ms, m)
	}
	return ms
}

func business(in string, rounds int, relief bool) int {
	ms, mod := parse(in), 1
	for _, m := range ms {
		mod *= m.div
	}
	for r := 0; r < rounds; r++ {
		for _, m := range ms {
			for _, w := range m.items {
				m.inspections++
				a := m.arg
				if a == 0 {
					a = w
				}
				if m.op == '*' {
					w *= a
				} else {
					w += a
				}
				if relief {
					w /= 3
				} else {
					w %= mod
				}
				if w%m.div == 0 {
					ms[m.t].items = append(ms[m.t].items, w)
				} else {
					ms[m.f].items = append(ms[m.f].items, w)
				}
			}
			m.items = nil
		}
	}
	var c []int
	for _, m := range ms {
		c = append(c, m.inspections)
	}
	slices.Sort(c)
	return c[len(c)-1] * c[len(c)-2]
}

func part1(in string) int { return business(in, 20, true) }

func part2(in string) int { return business(in, 10000, false) }

func main() {
	b, _ := os.ReadFile("2022/Day11_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
