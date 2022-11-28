#!/usr/bin/python

movement_list_file =  open("directions.txt","r").read().splitlines()

def main():
    #first value has been updated to be used as "aim", second is foward position, third is depth overall

    position = [0,0,0]
    for line in movement_list_file:
        if "forward" in line:
            print("Moving forwards " + str(line.split(" ")[1]) + " at an aim of " +str(position[0]))
            position[1] = position[1] + int(line.split(" ")[1])
            position[2] = position[2] + position[0] * int(line.split(" ")[1])
            print("New Forwards: " + str(position[1]))
            print("New Depth: " + str(position[2]))
        if "down" in line:
            position[0] = position[0] + int(line.split(" ")[1])
            print("Pointing further down to " + str(position[0]))
        if "up" in line:
            position[0] = position[0] - int(line.split(" ")[1])
            print("Pointing further up to " + str(position[0]))

    print("Final Multiple: " + str(position[1] * position[2]))
    print("Final Forwards: " + str(position[1]))
    print("Final Depth: " + str(position[2]))
    
main()