import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulate')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers(default: find the max)')

args = parser.parse_args()

print(args.accumulate(args.integers))


'''
$python3 01.py 10 20 30
30

$python3 01.py 10 20 30 --sum
60
'''