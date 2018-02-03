#! /bin/python3

import sys
import array
import numpy

def sortchar(teststring):
    print(teststring[::2], teststring[1::2])

def main():
    testlines = int(input().strip())
    linearr = []
    for n in range(0, testlines):
        linearr.append(input())
    for x in range(0, testlines):
        print(linearr[x][::2], linearr[x][1::2])



