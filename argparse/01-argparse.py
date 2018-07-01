import argparse

# Creating a parser
parser = argparse.ArgumentParser(description='Process some integers.')

# Adding arguments
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulate')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers(default: find the max)')

# Parsing arguments // parse_args()
args = parser.parse_args()

print(args.accumulate(args.integers))


'''

$ python3 01-argparse.py -h
usage: 01-argparse.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
  N           an integer for the accumulate

optional arguments:
  -h, --help  show this help message and exit
  --sum       sum the integers(default: find the max)


$ python3 01-argparse.py 10 20 30
30


$ python3 01-argparse.py 10 20 30 --sum
60

'''