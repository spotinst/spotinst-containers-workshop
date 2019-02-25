from time import sleep
from os import getenv
from time import time
NAME = getenv("NAME")

def main():
    index = 0

    while True:
        index += 1
        sleep(2)

        if NAME is not None:
            print("{}) Hello {} time".format(index, NAME))
        else:
            print("Hello World")

if __name__ == "__main__":
    main()