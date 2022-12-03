package main

import (
	"fmt"
	"math/bits"
	"os"
	"strings"
)

func mask(s string) uint64 {
	var m uint64
	for _, c := range s {
		if c >= 'a' {
			m |= 1 << (c - 'a' + 1)
		} else {
			m |= 1 << (c - 'A' + 27)
		}
	}
	return m
}

func part1(in string) int {
	total := 0
	for _, l := range strings.Fields(in) {
		total += bits.TrailingZeros64(mask(l[:len(l)/2]) & mask(l[len(l)/2:]))
	}
	return total
}

func part2(in string) int {
	ls, total := strings.Fields(in), 0
	for i := 0; i < len(ls); i += 3 {
		total += bits.TrailingZeros64(mask(ls[i]) & mask(ls[i+1]) & mask(ls[i+2]))
	}
	return total
}

func main() {
	b, _ := os.ReadFile("2022/Day03_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
