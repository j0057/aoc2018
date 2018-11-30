from datetime import date, datetime
import os
import re

import requests

import pytest

YEAR = 2018

def match_groups(regex, string):
    match = re.match(regex, string)
    if not match:
        raise ValueError('Regex did not match: {0!r}'.format(string))
    return match.groups()

re.match_groups = match_groups # shameless duck punching, but will save me 4 lines of code every day

def get_cookie():
    with open('.cookie', 'r') as f:
        return f.read().strip()

def get_input(day):
    response = requests.get('https://adventofcode.com/{0}/day/{1}/input'.format(YEAR, day), cookies={'session': get_cookie()})
    response.raise_for_status()
    return response

def download_inputs():
    if not os.path.isdir('input'):
        os.mkdir('input')
    early = datetime.now().hour >= 6
    today = (date.today() - date(YEAR, 11, 30)).days
    for day in range(1, min(25, today + early)):
        filename = 'input/day{0:02d}.txt'.format(day)
        if os.path.exists(filename):
            continue
        response = get_input(day)
        with open(filename, 'w') as f:
            f.write(response.text)

def gen_fixture(filename):
    match = re.match(r'^(day\d\d).txt$', filename)
    if not match:
        return {}

    @pytest.fixture
    def content():
        with open('input/' + filename, 'r') as f:
            return f.read().strip()

    @pytest.fixture
    def raw():
        with open('input/' + filename, 'r') as f:
            return f.read()

    @pytest.fixture
    def lines():
        with open('input/' + filename, 'r') as f:
            return [ line.strip() for line in f ]

    @pytest.fixture
    def numbers():
        with open('input/' + filename, 'r') as f:
            return [ int(line.strip()) for line in f ]

    @pytest.fixture
    def number():
        with open('input/' + filename, 'r') as f:
            return int(f.read().strip())

    @pytest.fixture
    def grid():
        with open('input/' + filename, 'r') as f:
            return [ row.split() for row in f ]

    @pytest.fixture
    def number_grid():
        with open('input/' + filename, 'r') as f:
            return [ [ int(s) for s in row.split() ] for row in f ]

    return {
        match.groups()[0]: content,
        match.groups()[0] + '_raw': raw,
        match.groups()[0] + '_lines': lines,
        match.groups()[0] + '_numbers': numbers,
        match.groups()[0] + '_number': number,
        match.groups()[0] + '_grid': grid,
        match.groups()[0] + '_number_grid': number_grid
    }

def generate_fixtures():
    for filename in os.listdir('input'):
        globals().update(gen_fixture(filename))

download_inputs()
generate_fixtures()
