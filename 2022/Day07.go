package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func sizes(in string) map[string]int {
	sz, path := map[string]int{}, []string{}
	for _, l := range strings.Split(in, "\n") {
		switch {
		case l == "$ cd /":
			path = []string{""}
		case l == "$ cd ..":
			path = path[:len(path)-1]
		case strings.HasPrefix(l, "$ cd "):
			path = append(path, l[5:])
		case l == "$ ls" || strings.HasPrefix(l, "dir "):
		default:
			n, _ := strconv.Atoi(strings.Fields(l)[0])
			for i := range path {
				sz[strings.Join(path[:i+1], "/")] += n
			}
		}
	}
	return sz
}

func part1(in string) int {
	total := 0
	for _, n := range sizes(in) {
		if n <= 100000 {
			total += n
		}
	}
	return total
}

func part2(in string) int {
	sz := sizes(in)
	need, best := 30000000-(70000000-sz[""]), sz[""]
	for _, n := range sz {
		if n >= need && n < best {
			best = n
		}
	}
	return best
}

func main() {
	b, _ := os.ReadFile("2022/Day07_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
