#!/usr/bin/python

"""Add docstrings to Python modules"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import count
from bs4 import BeautifulSoup
import requests

from utils import get_path


def fetch_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def get_docstring(html):
    soup = BeautifulSoup(html, "html.parser")
    problem_number = soup.body.find("h3").contents[0].strip()
    problem_title = soup.body.find("h2").text
    return f'"""{problem_number}: {problem_title}"""\n'


def update_file(path, docstring):
    with path.open("r+") as f:
        lines = f.readlines()

        if lines[2] != docstring:
            print(docstring[3:-4])
            lines[2:2] = [docstring, "\n"]
            f.seek(0)
            f.writelines(lines)


def main():
    with ThreadPoolExecutor() as executor:
        futures = {}

        for num in count(1):
            filename = f"problem{num:03d}.py"
            path = get_path("python", filename)
            url = f"https://projecteuler.net/problem={num}"

            if not path.exists():
                break

            futures[executor.submit(fetch_url, url)] = path

        for future in as_completed(futures):
            html = future.result()
            path = futures[future]
            docstring = get_docstring(html)
            update_file(path, docstring)


if __name__ == "__main__":
    main()
