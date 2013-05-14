#!/usr/bin/bash

for d in *; do
	if [ -d $d ]; then
		cd $d
		read answer < answer

		if [ $(./$d.py) = $answer ]; then
			echo "$d [OK]"
		else
			echo "$d [FAIL]"
		fi
		cd - > /dev/null
	fi
done
