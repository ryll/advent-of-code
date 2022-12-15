package main

import (
	"encoding/json"
	"fmt"
	"os"
	"slices"
	"strings"
)

func decode(s string) any {
	var v any
	json.Unmarshal([]byte(s), &v)
	return v
}

func cmp(a, b any) int {
	x, ok1 := a.([]any)
	y, ok2 := b.([]any)
	switch {
	case !ok1 && !ok2:
		n, m := a.(float64), b.(float64)
		if n != m {
			if n < m {
				return -1
			}
			return 1
		}
		return 0
	case !ok1:
		x = []any{a}
	case !ok2:
		y = []any{b}
	}
	for i := 0; i < len(x) && i < len(y); i++ {
		if c := cmp(x[i], y[i]); c != 0 {
			return c
		}
	}
	return len(x) - len(y)
}

func part1(in string) int {
	total := 0
	for i, b := range strings.Split(in, "\n\n") {
		l := strings.Split(b, "\n")
		if cmp(decode(l[0]), decode(l[1])) < 0 {
			total += i + 1
		}
	}
	return total
}

func part2(in string) int {
	d2, d6 := decode("[[2]]"), decode("[[6]]")
	ps := []any{d2, d6}
	for _, l := range strings.Fields(in) {
		ps = append(ps, decode(l))
	}
	slices.SortFunc(ps, cmp)
	i := slices.IndexFunc(ps, func(p any) bool { return cmp(p, d2) == 0 })
	j := slices.IndexFunc(ps, func(p any) bool { return cmp(p, d6) == 0 })
	return (i + 1) * (j + 1)
}

func main() {
	b, _ := os.ReadFile("2022/Day13_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
