#!/usr/bin/python

movement_list_file =  open("directions.txt","r").read().splitlines()

def main():
    #first value is left/right (x), second is forward, backwards (y), third is depth (z)
    #ignoring that "depth" would typically be exclaimed as a negative here, and left/right wont be used, future proofing.
    position = [0,0,0]
    for line in movement_list_file:
        if "forward" in line:
            position[1] = position[1] + int(line.split(" ")[1])
        if "down" in line:
            position[2] = position[2] + int(line.split(" ")[1])
        if "up" in line:
            position[2] = position[2] - int(line.split(" ")[1])
    print("Final Multiple: " + str(position[1] * position[2]))
    print("Final Forwards: " + str(position[1]))
    print("Final Depth: " + str(position[2]))
    
main()