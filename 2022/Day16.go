package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func parse(in string) (map[string]int, map[string][]string) {
	rate, adj := map[string]int{}, map[string][]string{}
	for _, l := range strings.Split(in, "\n") {
		f := strings.SplitN(strings.NewReplacer("=", " ", ";", "", ",", "").Replace(l), " ", -1)
		name := f[1]
		rate[name], _ = strconv.Atoi(f[5])
		for _, v := range f[6:] {
			if len(v) == 2 && v[0] >= 'A' && v[0] <= 'Z' {
				adj[name] = append(adj[name], v)
			}
		}
	}
	return rate, adj
}

func best(in string, time int) map[int]int {
	rate, adj := parse(in)
	dist := map[string]map[string]int{}
	for a := range rate {
		dist[a] = map[string]int{a: 0}
		for _, b := range adj[a] {
			dist[a][b] = 1
		}
	}
	for k := range rate {
		for i := range rate {
			for j := range rate {
				if dik, ok1 := dist[i][k]; ok1 {
					if dkj, ok2 := dist[k][j]; ok2 {
						if d, ok := dist[i][j]; !ok || dik+dkj < d {
							dist[i][j] = dik + dkj
						}
					}
				}
			}
		}
	}
	var useful []string
	for v, r := range rate {
		if r > 0 {
			useful = append(useful, v)
		}
	}
	slices.Sort(useful)
	res := map[int]int{}
	var visit func(cur string, t, mask, rel int)
	visit = func(cur string, t, mask, rel int) {
		if rel > res[mask] {
			res[mask] = rel
		}
		for i, v := range useful {
			if mask&(1<<i) != 0 {
				continue
			}
			if nt := t - dist[cur][v] - 1; nt > 0 {
				visit(v, nt, mask|1<<i, rel+nt*rate[v])
			}
		}
	}
	visit("AA", time, 0, 0)
	return res
}

func part1(in string) int {
	top := 0
	for _, v := range best(in, 30) {
		top = max(top, v)
	}
	return top
}

func part2(in string) int {
	type e struct{ mask, rel int }
	var es []e
	for m, r := range best(in, 26) {
		es = append(es, e{m, r})
	}
	slices.SortFunc(es, func(a, b e) int { return b.rel - a.rel })
	top := 0
	for i, a := range es {
		if a.rel*2 <= top {
			break
		}
		for _, b := range es[i:] {
			if a.rel+b.rel <= top {
				break
			}
			if a.mask&b.mask == 0 {
				top = a.rel + b.rel
			}
		}
	}
	return top
}

func main() {
	b, _ := os.ReadFile("2022/Day16_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
