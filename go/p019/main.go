package main

import "fmt"

func isLeapYear(year int) bool {
	return year%4 == 0 && (year%100 != 0 || year%400 == 0)
}

func main() {
	const startYear = 1901
	const endYear = 2000

	monthDays := [12]int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

	weekday := 2 // Tuesday, 1 Jan 1901, with Sunday represented as 0
	sundays := 0

	for year := startYear; year <= endYear; year++ {
		isLeap := isLeapYear(year)

		for month := 0; month < 12; month++ {
			var days int

			if weekday == 0 {
				sundays++
			}
			if isLeap && month == 1 {
				days = 29
			} else {
				days = monthDays[month]
			}
			weekday = (weekday + days) % 7
		}
	}
	fmt.Println(sundays)
}
