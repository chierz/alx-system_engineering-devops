#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("https://www.reddit.com/dev/api/#GET_subreddits_mine_subscriber")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
