package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parse(in string) map[string][]string {
	m := map[string][]string{}
	for _, l := range strings.Split(in, "\n") {
		p := strings.SplitN(l, ": ", 2)
		m[p[0]] = strings.Fields(p[1])
	}
	return m
}

func eval(m map[string][]string, name string) int {
	f := m[name]
	if len(f) == 1 {
		n, _ := strconv.Atoi(f[0])
		return n
	}
	a, b := eval(m, f[0]), eval(m, f[2])
	switch f[1] {
	case "+":
		return a + b
	case "-":
		return a - b
	case "*":
		return a * b
	}
	return a / b
}

func has(m map[string][]string, name, target string) bool {
	if name == target {
		return true
	}
	f := m[name]
	return len(f) == 3 && (has(m, f[0], target) || has(m, f[2], target))
}

func solve(m map[string][]string, name string, want int) int {
	if name == "humn" {
		return want
	}
	f := m[name]
	if has(m, f[0], "humn") {
		b := eval(m, f[2])
		switch f[1] {
		case "+":
			return solve(m, f[0], want-b)
		case "-":
			return solve(m, f[0], want+b)
		case "*":
			return solve(m, f[0], want/b)
		}
		return solve(m, f[0], want*b)
	}
	a := eval(m, f[0])
	switch f[1] {
	case "+":
		return solve(m, f[2], want-a)
	case "-":
		return solve(m, f[2], a-want)
	case "*":
		return solve(m, f[2], want/a)
	}
	return solve(m, f[2], a/want)
}

func part1(in string) int { return eval(parse(in), "root") }

func part2(in string) int {
	m := parse(in)
	f := m["root"]
	if has(m, f[0], "humn") {
		return solve(m, f[0], eval(m, f[2]))
	}
	return solve(m, f[2], eval(m, f[0]))
}

func main() {
	b, _ := os.ReadFile("2022/Day21_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
