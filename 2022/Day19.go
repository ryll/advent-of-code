package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func parse(in string) [][7]int {
	f := regexp.MustCompile(`\d+`).FindAllString(in, -1)
	var bps [][7]int
	for i := 0; i+7 <= len(f); i += 7 {
		var bp [7]int
		for j := range bp {
			bp[j], _ = strconv.Atoi(f[i+j])
		}
		bps = append(bps, bp)
	}
	return bps
}

func geodes(bp [7]int, time int) int {
	cost := [4][3]int{{bp[1], 0, 0}, {bp[2], 0, 0}, {bp[3], bp[4], 0}, {bp[5], 0, bp[6]}}
	limit := [3]int{max(bp[1], bp[2], bp[3], bp[5]), bp[4], bp[6]}
	best := 0
	var dfs func(t int, res, bots [3]int, geo int)
	dfs = func(t int, res, bots [3]int, geo int) {
		if geo+t*(t-1)/2 <= best {
			return
		}
		best = max(best, geo)
		for k := 3; k >= 0; k-- {
			if k < 3 && bots[k] >= limit[k] {
				continue
			}
			wait := 0
			for r := 0; r < 3; r++ {
				if need := cost[k][r] - res[r]; need > 0 {
					if bots[r] == 0 {
						wait = time + 1
						break
					}
					wait = max(wait, (need+bots[r]-1)/bots[r])
				}
			}
			if wait+1 >= t {
				continue
			}
			nres, nbots := res, bots
			for r := 0; r < 3; r++ {
				nres[r] += bots[r]*(wait+1) - cost[k][r]
			}
			if k < 3 {
				nbots[k]++
			}
			ngeo := geo
			if k == 3 {
				ngeo += t - wait - 1
			}
			dfs(t-wait-1, nres, nbots, ngeo)
		}
	}
	dfs(time, [3]int{}, [3]int{1, 0, 0}, 0)
	return best
}

func part1(in string) int {
	total := 0
	for _, bp := range parse(in) {
		total += bp[0] * geodes(bp, 24)
	}
	return total
}

func part2(in string) int {
	bps, total := parse(in), 1
	for _, bp := range bps[:min(3, len(bps))] {
		total *= geodes(bp, 32)
	}
	return total
}

func main() {
	b, _ := os.ReadFile("2022/Day19_input.txt")
	in := strings.TrimRight(string(b), "\n")
	fmt.Println("Part 1:", part1(in))
	fmt.Println("Part 2:", part2(in))
}
