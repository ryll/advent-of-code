package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
)

func rearrange(in string, keep bool) string {
	parts := strings.Split(in, "\n\n")
	rows := strings.Split(parts[0], "\n")
	nums := strings.Fields(rows[len(rows)-1])
	stacks := make([][]byte, len(nums))
	for i := len(rows) - 2; i >= 0; i-- {
		for j := range stacks {
			if k := 1 + 4*j; k < len(rows[i]) && rows[i][k] != ' ' {
				stacks[j] = append(stacks[j], rows[i][k])
			}
		}
	}
	for _, l := range strings.Split(strings.TrimRight(parts[1], "\n"), "\n") {
		var n, from, to int
		fmt.Sscanf(l, "move %d from %d to %d", &n, &from, &to)
		s := stacks[from-1]
		moved := slices.Clone(s[len(s)-n:])
		if !keep {
			slices.Reverse(moved)
		}
		stacks[from-1] = s[:len(s)-n]
		stacks[to-1] = append(stacks[to-1], moved...)
	}
	top := make([]byte, len(stacks))
	for i, s := range stacks {
		top[i] = s[len(s)-1]
	}
	return string(top)
}

func part1(in string) string { return rearrange(in, false) }

func part2(in string) string { return rearrange(in, true) }

func main() {
	b, _ := os.ReadFile("2022/Day05_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
