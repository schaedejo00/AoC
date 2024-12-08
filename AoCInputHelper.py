import os

import requests

# Base URL for Advent of Code inputs
BASE_URL = "https://adventofcode.com/{}/day/{}/input"

# Get session cookie from environment variable
session_cookie = os.getenv("AOC_SESSION")


# Function to fetch input for a specific year and day
def get_input(year: int, day: int) -> str:
    try:
        return open("input").read()
    except FileNotFoundError:

        url = BASE_URL.format(year, day)
        cookies = {"session": open("../session-key").read().strip()}

        # Make a request
        response = requests.get(url, cookies=cookies)

        if response.status_code == 200:
            return response.text.rstrip()
        else:
            return f"Error fetching input: {response.status_code}"


def get_grid(inp: str) -> tuple[dict[tuple[int, int], str], int, int]:
    grid: dict[tuple[int, int], str] = dict()
    inp = inp.split('\n')
    for r, row in enumerate(inp):
        for c, cell in enumerate(row):
            grid[r, c] = cell
    nr = len(inp)
    nc = len(inp[0])
    return grid, nr, nc


def remove_entries_by_value(dictionary, value_to_remove):
    return {key: val for key, val in dictionary.items() if val != value_to_remove}


def is_on_grid(location: tuple[int, int], row_count: int, col_count: int) -> bool:
    return True if 0 <= location[0] < row_count and 0 <= location[1] < col_count else False

# Example usage
# year = 2024
# day = 3
# input_data = fetch_input(year, day)
# print(input_data)
