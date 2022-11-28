#!/usr/bin/python

global DEPTHS_LIST_FILE
DEPTHS_LIST_FILE =  open("depths.txt","r").read().splitlines()


def main():
    depth_increase_count = 0
    i = 4
    while i < len(DEPTHS_LIST_FILE):
        if get_value_for_position(i) > get_value_for_position(i-1):
            depth_increase_count = depth_increase_count + 1
        i = i + 1
    print(depth_increase_count)

def get_value_for_position(position):
    i = 0
    return_value = 0
    while i < 3:
        return_value = return_value + int(DEPTHS_LIST_FILE[position - i])
        i = i + 1
    return return_value

main()