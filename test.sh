#!/usr/bin/bash

cd "$(dirname $0)"

for d in *; do
	if [ -d $d ]; then
		read answer < $d/answer
		echo -n "$d  "

		bin=$d/problem$((10#$d)).py

		if [ "$($bin)" = $answer ]; then
			echo OK
		else
			echo FAIL
		fi
	fi
done
