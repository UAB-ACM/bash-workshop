import sys
from time import sleep, time
from random import randrange

def main():
    for counter in range(30):
        sleep(.5)
        if randrange(0, 10) == 0:
            print( "Error on {}".format(counter), file=sys.stderr )
            continue
        print(counter)

try:
    main()
except KeyboardInterrupt:
    pass