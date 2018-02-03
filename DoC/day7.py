#!/bin/python

import sys

def main():
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.reverse()
    tmpstr = ''
    for i in range(0, n):
        print(arr[i], end=' ')

if __name__ == '__main__':
    main()