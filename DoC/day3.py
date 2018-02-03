#! /usr/bin/python3

def main():
    i = 4
    d = 4.0
    s = 'HackerRank '

    int2 = int(input().strip())
    double2 = float(input().strip())
    string2 = str(input().strip())

    sol1 = i + int2
    sol2 = d + double2
    sol3 = s + string2

    print(sol1)
    print(sol2)
    print(sol3)

if __name__ == '__main__':
    main()