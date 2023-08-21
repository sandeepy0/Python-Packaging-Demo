#!/usr/bin/python3

import sys
from doraemonsay import doraemon

def say():
    doraemon.say(" ".join(sys.argv[1:]))

def main():
    say()

if __name__ == '__main__':
    main()
