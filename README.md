# Advent of Code 2018

Python solutions to [Advent of Code 2018][1]. Pytest is needed to run the tests
as well as my new Pytest plugin **pytest-aoc** ([GitHub][2], [PyPI][3]), to
provide AoC test fixtures to the unit tests.

To run the Python code:

    python3.7 -m pip install -r requirements.txt
    python3.7 -m pytest

[1]: https://adventofcode.com/2018
[2]: https://github.com/j0057/pytest-aoc
[3]: https://pypi.org/project/pytest-aoc

## Day 1: Chronal Calibration

_"Starting with a frequency of zero, what is the resulting frequency after all
of the changes in frequency have been applied?"_ – solved with `sum`.

_"What is the first frequency your device reaches twice?"_ – solved with a
while loop, a set and `itertools.cycle`.

## Day 2: Inventory Management System

_"What is the checksum for your list of box IDs?"_ – it only took until day 2
for `collections.Counter` to save the day.

_"What letters are common between the two correct box IDs?"_ – just `zip` and
`max`.

## Day 3: No Matter How You Slice It

_"How many square inches of fabric are within two or more claims?"_ – used a
`collections.defaultdict`.

_"What is the ID of the only claim that doesn't overlap?"_ – used a set of all
claims and removed all claims that were in a coordinate with more than one
claim.

## Day 4: Repose Record

_"Find the guard that has the most minutes asleep. What minute does that guard
spend asleep the most?"_ – first used `itertools.groupby` to make a dict of all
the guards and their minutes, then `max` to find the sleepiest guard, then
`collections.Counter` for the best time.

_"Of all guards, which guard is most frequently asleep on the same minute?"_ –
same as part one but a little different.

_"What is the ID of the guard you chose multiplied by the minute you chose?"_

## Day 5: Alchemical Reduction

_"How many units remain after fully reacting the polymer you scanned?"_ – used
`functools.reduce` with a lambda that's a little too complex.

_"What is the length of the shortest polymer you can produce by removing all
units of exactly one type and fully reacting the result?"_ – same as part one
but with an additional loop over the alphabet.

## Day 6: Chronal Coordinates

_"What is the size of the largest area that isn't infinite?"_ – did some
research on properly calculating [Voronoi diagrams][6.1], decided that the O(n
log n) solution in [Fortune's Algorithm][6.2] looked like a lot of hard work,
and went with the naive quadratic solution instead: for each cell, find the
distances to all the points. For n=50, it runs fast enough on a Core i7-7700.

I did like calculating the bounding box using just two `functools.reduce`
statements with `min` and `max`. Also used `collections.Counter` again, as well
as `functools.takewhile`.

_"What is the size of the region containing all locations which have a total
distance to all given coordinates of less than 10000?"_ – not aware of any
algorithms here so went with brute force again.

[6.1]: https://en.m.wikipedia.org/wiki/Voronoi_diagram
[6.2]: https://en.m.wikipedia.org/wiki/Fortune%27s_algorithm

## Day 7: The Sum of Its Parts

_"In what order should the steps in your instructions be completed?"_ – this
one was rather painful. I tried [Depth-First Search][7.1] recursively as well
as iteratively, with the edges pointing from or to the dependencies, and got
the wrong order every time. Found out I wanted a [Topological Sorting][7.2]
instead, which I implemented using **Kahn's Algorithm**.

At least `itertools.chain` and `itertools.groupby` lessened the pain somewhat.

_"With 5 workers and the 60+ second step durations described above, how long
will it take to complete all of the steps?"_ – said "Fuck it", and hacked at
Kahn's Algorithm until I got the right answer, but off by one. Said "Fuck it"
again, added a `-1` in the code, and AoC accepted the answer. Not my proudest
moment.

Had to drag in `collections.defaultdict` again, to hold extremely hacky lambda
function closures.

[7.1]: https://en.m.wikipedia.org/wiki/Depth-first_search
[7.2]: https://en.wikipedia.org/wiki/Topological_sorting

## Day 8: Memory Maneuver

_"What is the sum of all metadata entries?"_ – this was made really easy by
Python's iterators, which can be consumed only once. The recursive Tree
constructor uses `itertools.islice` to pluck values from the iterator.

_"What is the value of the root node?"_ – could basically add the rules without
too much thinking.

## Day 9: Marble Mania

_"What is the winning Elf's score?"_ – pretty straightforward implementation
using a standard list.

_"What would the new winning Elf's score be if the number of the last marble
were 100 times larger?"_ – it turns out using `list.insert` and `list.pop`
doesn't scale due to all the copying. Got referred to the `blist` package that
acts as a fast drop-in replacement for Python's list. That one did get the job
done. It did throw some warnings though and it's not compatible with PyPy, so I
did the work to implement a [Doubly-linked List][9.1]. I opted for the 'hash
linking' method, which cost me half an hour of pen-and-paper debugging. Also,
it does take a good 5s to run...

Update: The solution from the reddit solution thread using `collections.deque`
runs in 1.05s and reads much cleaner.

[9.1]: https://en.m.wikipedia.org/wiki/Linked_list#Hash_linking

## Day 10: The Stars Align

_"What message will eventually appear in the sky?"_ – Implemented using an
iterator. No unit tests, so I'll just link a screenshot:

![day 10 output](doc/aoc2018-day10.png)

_"Exactly how many seconds would they have needed to wait for that message to
appear?"_ – That's the number of iterations minus two...

## Day 11: Chronal Charge

_"What is the X,Y coordinate of the top-left fuel cell of the 3x3 square with
the largest total power?"_ – just `sum` with two loops.

_"What is the X,Y,size identifier of the square witoh the largest total
power?"_ – wouldn't complete with approach from part one, had to implement a
[Summed-area table][11.1].

[11.1]: https://en.wikipedia.org/wiki/Summed-area_table

## Day 12: Subterranean Sustainability

_"After 20 generations, what is the sum of the numbers of all pots which
contain a plant?"_ – `collections.defaultdict` and `itertools.islice`, again.

_"After fifty billion (50000000000) generations, what is the sum of the numbers
of all pots which contain a plant?_" – visualisation based on `print()`, and
add 499999999000 to every grown plant position on iteration #1000.

## Day 13: Mine Cart Madness

_"To help prevent crashes, you'd like to know the location of the first
crash."_ – parsed the text into a `defaultdict` (again) with a complex number
for the coordinate as key, and the grid (without carts) as the value. Also
parse the carts into a dictionary with a complex number as the key, and a tuple
of (direction vector, next turn), both as complex numbers. This made it really
ease to code the main loop.

_"What is the location of the last cart at the end of the first tick where it
is the only cart left?"_– I think it's a bug to clear the crash site at the
beginning of each iteration, but the bug would only manifest if three carts
crash in the same tick.

## Day 14: Chocolate Charts

_"What are the scores of the ten recipes immediately after the number of
recipes in your puzzle input?"_

_"How many recipes appear on the scoreboard to the left of the score sequence
in your puzzle input?"_
