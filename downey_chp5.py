# @author: Kristin Dahl
# December 28, 2020
# Think Python, 2nd ed., Chapter 5

import time

def  get_time():
    cur_time = time.time()
    seconds_in_day = 60*60*24

    days = cur_time // seconds_in_day
    remainder = cur_time % seconds_in_day

    hours = remainder // (60*60)
    remainder = remainder % (60*60)

    minutes = remainder // (60)
    seconds = remainder % (60)

    print(f'Days since epoch: {days}  Current Time: {hours}:{minutes}:{seconds:.2f}')

#get_time()

def check_fermat(a, b, c, n):
    if n > 2:
        if (a^n + b^n == c^n):
            print("Fermat was wrong!")
        else:
            print("no, that doesn't work")
    else:
        print("n must be greater than 2")


def get_user_input():
    prompt = "Please enter a value for a:"
    a = int(input(prompt))

    prompt = "Please enter a value for b:"
    b = int(input(prompt))

    prompt = "Please enter a value for c:"
    c = int(input(prompt))

    prompt = "Please enter a value for n:"
    n = int(input(prompt))

    check_fermat(a, b, c, n)

get_user_input()