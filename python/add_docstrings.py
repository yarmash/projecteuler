#!/usr/bin/env python

"""Add docstrings to solutions."""

import sys
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
import requests

from utils import get_path


def parse_args(args=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Add docstrings to solutions")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-n", "--number", type=int, metavar="NUM",
                       help="The problem number")
    group.add_argument("-a", "--all", action="store_true",
                       help="Process all files")

    return parser.parse_args(args)


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
    args = parse_args()

    if args.number:
        path = get_path("python", f"problem{args.number:03d}.py")
        if not path.exists():
            print(f"Module not found: {path}")
            return 1
        paths = [path]
    else:
        paths = sorted(get_path("python").glob("problem???.py"))

    with ThreadPoolExecutor() as executor:
        futures = {}

        for path in paths:
            num = path.stem[-3:]  # extract the problem number
            url = f"https://projecteuler.net/problem={num}"
            futures[executor.submit(fetch_url, url)] = path

        for future in as_completed(futures):
            html = future.result()
            path = futures[future]
            docstring = get_docstring(html)
            update_file(path, docstring)


if __name__ == "__main__":
    sys.exit(main())
