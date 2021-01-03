# @author: Kristin Dahl
# December 28, 2020
# Think Python, 2nd ed., Exercise 3

def right_justify(s):
    # Exercise 3-1 pg. 32
    space_count = 70 - len(s)
    newstr = ' ' * space_count + s
    print(newstr)


right_justify('monty')

# Exercise 3-2 pg. 33
def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_twice(f, v):
    f(v)
    f(v)

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)



