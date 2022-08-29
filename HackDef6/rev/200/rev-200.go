package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	args := os.Args

	if len(args) != 2 {
		fmt.Println("nope")
	} else {
		go flag()
		time.Sleep(0 * time.Millisecond)
		if len(args[1]) == 8 {
			// fmt.Println(args[1])
			// fmt.Println(len(args[1]))
			// fmt.Println(len(args[1]) == 8)
			res := followMe(args[1])
			fmt.Println(res)
		} else {
			fmt.Println("nope x2")
		}
	}
}

func flag() {
	flag_1 := [...]int{102, 97, 107, 101, 95, 102, 108, 97, 103, 95, 88, 68, 95, 88, 68}
	for _, x := range flag_1 {

		fmt.Print(string(x))
	}
}

func followMe(key string) (result string) {
	var code [48]int
	code = [48]int{0x22, 0x52, 0x56, 0x1e, 0x17, 0x21, 0x56, 0x16, 0x38, 0x0, 0x43, 0x10, 0x1, 0x37, 0x1, 0x3, 0x2d, 0x6c, 0x52, 0x45, 0x2c, 0x75, 0x44, 0x58, 0x15, 0x7, 0x6a, 0x13, 0x18, 0x2a, 0x6f, 0x0, 0x79, 0x6, 0x0, 0x2a, 0xa, 0x74, 0x45, 0x32, 0x2e, 0x2, 0x51, 0x2a, 0x42, 0x30, 0x11, 0x10}

	var code_2 [48]int
	key_arr := []rune(key)
	x := 0
	for i := 0; i < 48; i++ {
		if x == 8 {
			x = 0
		}
		code_2[i] = code[i] ^ int(key_arr[x])
		x += 1
	}

	if code_2[0] == 0x68 {
		if code_2[1] == 0x61 {
			if code_2[2] == 0x63 {
				if code_2[3] == 0x6b {
					if code_2[4] == 0x64 {
						if code_2[5] == 0x65 {
							if code_2[6] == 0x66 {
								if code_2[7] == 0x7b {
									for j := 0; j < 48; j++ {
										fmt.Printf("%c", rune(code_2[j]))
									}
									result = "\nCongrats!"
									return
								}
							}
						}
					}
				}
			}

		}

	}
	result = "nope x3"
	return
}

//hackdef{}
