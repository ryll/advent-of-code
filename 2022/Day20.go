package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func mix(nums []int, key, rounds int) int {
	n := len(nums)
	idx := make([]int, n)
	for i := range idx {
		idx[i] = i
	}
	for r := 0; r < rounds; r++ {
		for i := 0; i < n; i++ {
			p := slices.Index(idx, i)
			idx = append(idx[:p], idx[p+1:]...)
			q := ((p+nums[i]*key)%(n-1) + n - 1) % (n - 1)
			idx = append(idx[:q], append([]int{i}, idx[q:]...)...)
		}
	}
	z := slices.IndexFunc(idx, func(i int) bool { return nums[i] == 0 })
	total := 0
	for _, o := range []int{1000, 2000, 3000} {
		total += nums[idx[(z+o)%n]] * key
	}
	return total
}

func part1(nums []int) int { return mix(nums, 1, 1) }

func part2(nums []int) int { return mix(nums, 811589153, 10) }

func main() {
	b, _ := os.ReadFile("2022/Day20_input.txt")
	var nums []int
	for _, l := range strings.Fields(string(b)) {
		n, _ := strconv.Atoi(l)
		nums = append(nums, n)
	}
	fmt.Println("Part 1:", part1(nums))
	fmt.Println("Part 2:", part2(nums))
}
