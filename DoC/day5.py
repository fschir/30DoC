#!/bin/python3

import sys


def main():
    n = int(input().strip())
    for i in range(1, 11):
        print(str(n) + " x " + str(i) + " = " + str(n*i))

if __name__ == "__main__":
    main()