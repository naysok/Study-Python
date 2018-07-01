import argparse

# Creating a parser
parser = argparse.ArgumentParser()

# Parsing arguments // parse_args()
parser.add_argument('keyPressed_Data')

args = parser.parse_args()

print('Key preessed :', args.keyPressed_Data)


'''

$ python3 00.py g
Key preessed : g


$ python3 02-argparse.py ggg
Key preessed : ggg


$ python3 00.py --h
usage: 00.py [-h] keyPressed_Data

positional arguments:
  keyPressed_Data

optional arguments:
  -h, --help       show this help message and exit

'''