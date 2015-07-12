#!/usr/bin/python

import os
from itertools import count
import requests
from bs4 import BeautifulSoup

for num in count(1):
    filename = "problem{:03d}.py".format(num)

    if not os.path.exists(filename):
        break

    url = "https://projecteuler.net/problem="+str(num)
    r = requests.get(url)
    r.raise_for_status()
    s = BeautifulSoup(r.content)
    problem_number = s.body.find('h3').text
    problem_title = s.body.find('h2').text

    docstring = '"""{}: {}"""\n'.format(problem_number, problem_title)
    print(docstring[3:-4])

    with open(filename, "r+") as f:
        contents = f.readlines()

        if contents[2] != docstring:
            contents[2:2] = [docstring, "\n"]
            f.seek(0)
            f.truncate()
            f.write("".join(contents))
