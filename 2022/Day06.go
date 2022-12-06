package main

import (
	"fmt"
	"math/bits"
	"os"
	"strings"
)

func marker(in string, n int) int {
	for i := n; i <= len(in); i++ {
		var m uint32
		for _, c := range in[i-n : i] {
			m |= 1 << (c - 'a')
		}
		if bits.OnesCount32(m) == n {
			return i
		}
	}
	return -1
}

func part1(in string) int { return marker(in, 4) }

func part2(in string) int { return marker(in, 14) }

func main() {
	b, _ := os.ReadFile("2022/Day06_input.txt")
	in := strings.TrimSpace(string(b))
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
