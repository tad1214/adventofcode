#!/usr/bin/python

depths_list_file =  open("depths.txt","r").read().splitlines()

def main():
    depth_increase_count = 0
    for iteration,line in enumerate(depths_list_file):
        if iteration > 0:
            if int(line) > int(depths_list_file[iteration-1]):
                depth_increase_count = depth_increase_count + 1
                print(line + " is greater than " + depths_list_file[iteration-1] + ", number of increases is " + str(depth_increase_count))
            else:
                print(line + " is less than " + depths_list_file[iteration-1])
    print(str(depth_increase_count) + " out of " + str(iteration+1)) 
 
main()