package main

import (
	"fmt"
	"os"
	"strings"
)

var shapes = [5][]uint8{
	{0b0011110},
	{0b0001000, 0b0011100, 0b0001000},
	{0b0011100, 0b0000100, 0b0000100},
	{0b0010000, 0b0010000, 0b0010000, 0b0010000},
	{0b0011000, 0b0011000},
}

func fits(rows []uint8, s []uint8, y int) bool {
	for i, r := range s {
		if y+i < len(rows) && rows[y+i]&r != 0 {
			return false
		}
	}
	return true
}

func fall(jets string, n int) int {
	var rows []uint8
	j, added := 0, 0
	seen := map[string][2]int{}
	for r := 0; r < n; r++ {
		s := append([]uint8(nil), shapes[r%5]...)
		y := len(rows) + 3
		for {
			var moved []uint8
			ok := true
			for _, v := range s {
				if jets[j%len(jets)] == '<' {
					if v&0b1000000 != 0 {
						ok = false
					}
					moved = append(moved, v<<1)
				} else {
					if v&1 != 0 {
						ok = false
					}
					moved = append(moved, v>>1)
				}
			}
			j++
			if ok && fits(rows, moved, y) {
				s = moved
			}
			if y > 0 && fits(rows, s, y-1) {
				y--
			} else {
				break
			}
		}
		for i, v := range s {
			for y+i >= len(rows) {
				rows = append(rows, 0)
			}
			rows[y+i] |= v
		}
		if added == 0 {
			k := fmt.Sprint(r%5, j%len(jets), string(rows[max(0, len(rows)-30):]))
			if p, ok := seen[k]; ok {
				cycles := (n - 1 - r) / (r - p[0])
				added = cycles * (len(rows) - p[1])
				r += cycles * (r - p[0])
			} else {
				seen[k] = [2]int{r, len(rows)}
			}
		}
	}
	return len(rows) + added
}

func part1(in string) int { return fall(in, 2022) }

func part2(in string) int { return fall(in, 1000000000000) }

func main() {
	b, _ := os.ReadFile("2022/Day17_input.txt")
	in := strings.TrimSpace(string(b))
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
