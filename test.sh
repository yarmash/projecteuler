#!/usr/bin/bash

cd "$(dirname $0)"

for d in *; do
	if [ -d $d ]; then
		read answer < $d/answer
		echo -n "$d  "

		if [ -e $d/$d.py ]; then
			bin=$d/$d.py
		else
			bin=$d/problem$((10#$d)).py
		fi

		if [ "$($bin)" = $answer ]; then
			echo OK
		else
			echo FAIL
		fi
	fi
done
