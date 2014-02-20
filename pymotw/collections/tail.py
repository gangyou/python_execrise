from collections import deque
import argparse

parser = argparse.ArgumentParser(description="tail util implement by python")
parser.add_argument('filename', type=str, help="Filename")
parser.add_argument('lines', type=int, default=10, help="an integer specify the lines to be displayed.", nargs="?")

arg = parser.parse_args()
filename = arg.filename
lines = arg.lines

for line in deque(open(filename), lines):
    print line