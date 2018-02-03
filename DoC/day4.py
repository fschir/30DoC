#! /usr/bin/python3

import numbers


def check(number):
    try:
        if number.is_integer():
            return True
    except AttributeError:
        return False

def main():
    N = int(input().strip())
    N_test = N/2
    if check(N_test):
        if (N>1 and N<6):
            print("Not Weird")
        elif(N>6 and N<21):
            print("Weird")
        elif(N>21):
            print("Not Weird")
    else:
        print("Weird")


if __name__ == '__main__':
    main()
