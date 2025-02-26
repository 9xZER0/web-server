package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	reader = bufio.NewReaderSize(os.Stdin, 1e6)
	writer = bufio.NewWriterSize(os.Stdout, 1e6)
)

func ReadInt() int {
	s, _ := reader.ReadString('\n')
	x, _ := strconv.Atoi(strings.TrimSpace(s))
	// x, _ := strconv.ParseFloat(strings.TrimSpace(s), 64)
	return x
}

func ReadPair() (int, int) {
	line, _ := reader.ReadString('\n')
	parts := strings.Fields(line)
	u, _ := strconv.Atoi(parts[0])
	v, _ := strconv.Atoi(parts[1])
	return u, v
}

func ReadArray() []int {
	s, _ := reader.ReadString('\n')
	fields := strings.Fields(s)
	arr := make([]int, len(fields))
	for i, v := range fields {
		arr[i], _ = strconv.Atoi(v)
		// arr[i], _ = strconv.ParseFloat(v, 64)
	}
	return arr
}

func ReadString() string {
	s, _ := reader.ReadString('\n')
	return strings.TrimSpace(s)
}

func Write(a ...interface{}) {
	fmt.Fprintln(writer, a...)
}

func main() {
	defer writer.Flush()

	testCase := true
	if testCase {
		t := ReadInt()
		for i := 0; i < t; i++ {
			solve()
		}
	} else {
		solve()
	}
}

func solve() {
	
}
