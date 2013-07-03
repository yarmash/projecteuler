#!/usr/bin/env python2

from itertools import count
import requests
from bs4 import BeautifulSoup

for num in count(1):
    url = "https://projecteuler.net/problem="+str(num)
    r = requests.get(url)
    r.raise_for_status()
    s = BeautifulSoup(r.content)
    problem_number = s.body.find('h3').text
    problem_title = s.body.find('h2').text

    docstring = '"""%s: %s"""\n' % (problem_number, problem_title)
    filepath = "%03d/problem%d.py" % (num, num)

    with open(filepath, "r+") as f:
        contents = f.readlines()

        if contents[2] != docstring:
            contents.insert(2, docstring+"\n")
            f.seek(0)
            f.truncate()
            f.write("".join(contents))
