package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
)

const (
	row = 2000000
	lim = 4000000
)

type sensor struct{ x, y, r int }

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func parse(in string) ([]sensor, map[int]map[int]bool) {
	var ss []sensor
	beacons := map[int]map[int]bool{}
	for _, l := range strings.Split(in, "\n") {
		var sx, sy, bx, by int
		fmt.Sscanf(l, "Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d", &sx, &sy, &bx, &by)
		ss = append(ss, sensor{sx, sy, abs(sx-bx) + abs(sy-by)})
		if beacons[by] == nil {
			beacons[by] = map[int]bool{}
		}
		beacons[by][bx] = true
	}
	return ss, beacons
}

func spans(ss []sensor, y int) [][2]int {
	var iv [][2]int
	for _, s := range ss {
		if d := s.r - abs(s.y-y); d >= 0 {
			iv = append(iv, [2]int{s.x - d, s.x + d})
		}
	}
	slices.SortFunc(iv, func(a, b [2]int) int { return a[0] - b[0] })
	merged := iv[:1]
	for _, v := range iv[1:] {
		last := &merged[len(merged)-1]
		if v[0] <= last[1]+1 {
			last[1] = max(last[1], v[1])
		} else {
			merged = append(merged, v)
		}
	}
	return merged
}

func part1(in string) int {
	ss, beacons := parse(in)
	n := 0
	for _, v := range spans(ss, row) {
		n += v[1] - v[0] + 1
	}
	for b := range beacons[row] {
		for _, v := range spans(ss, row) {
			if b >= v[0] && b <= v[1] {
				n--
				break
			}
		}
	}
	return n
}

func part2(in string) int {
	ss, _ := parse(in)
	for y := 0; y <= lim; y++ {
		if m := spans(ss, y); len(m) > 1 {
			return (m[0][1]+1)*4000000 + y
		}
	}
	return -1
}

func main() {
	b, _ := os.ReadFile("2022/Day15_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
