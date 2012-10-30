"Implementation of generators for parsing file"

import re

def iter_lines(fd):
    "iterates file lines"
    line = ""
    while True:
        char = fd.read(1)
        if char == '':
            break
        if char == '\n':
            yield line
            line = ""
        else:
            line += char
    yield line

def strip_spaces(itr):
    "strips spaces"
    for line in itr:
        yield line.strip()

def drop_empty(itr):
    "drops empty lines"
    for line in itr:
        if line != "":
            yield line

def is_int(value):
    "determines if value is integer"
    try:
        int(value)
        return str(value).find(".") < 0
    except ValueError:
        return False

def is_float(value):
    "determines if value is float"
    try:
        float(value)
        return True
    except ValueError:
        return False

def split_items(itr):
    "splits items by int,float,string sequence"
    for line in itr:
        arr = re.split(" |\n|\t", line)
        for item in arr:
            if is_int(item):
                yield int(item)
            elif is_float(item):
                yield float(item)
            else:
                yield item

def get_ints(itr):
    "returns only integers"
    for item in itr:
        if is_int(item):
            yield item

def my_sum(itr):
    "calculates sum of numbers in iterator"
    res = 0
    for item in itr:
        res += item
    return res

fd = open("hello.c")

#print list(get_ints(split_items(drop_empty(strip_spaces(iter_lines(fd))))))
print my_sum(get_ints(split_items(drop_empty(strip_spaces(iter_lines(fd))))))

#hello.c:
#
##include <stdio.h>
#
#int main()
#{
#    printf("Hello, world");    
#
#    return 0;
#}
#
#1 2 3 3.45 abra_cadabra   
#
#12