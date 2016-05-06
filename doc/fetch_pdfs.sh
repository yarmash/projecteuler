rm *.pdf

for problem in $(seq -w 1 $(wc -l < ../python/answers)); do
	curl -v -L -O -J --max-redirs 0 \
		--user-agent "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0" \
		--cookie "PHPSESSID=c311032ee5b4c159b261d5395965f285" \
		https://projecteuler.net/overview=$problem
	sleep $((RANDOM % 10 + 1))
done
