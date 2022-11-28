#!/usr/bin/python

global DIAGNOSTIC_DATA 
DIAGNOSTIC_DATA =  open("input.txt","r").read().splitlines()

def main():
    
    remaining_data_oxygen = DIAGNOSTIC_DATA
    i = 0
    while i < len(DIAGNOSTIC_DATA[0]):
        #First value for 0's, second for 1's
        bit_count = [0,0]
        
        for line in remaining_data_oxygen:
            if int(line[i]) == 0:
                bit_count[0] = bit_count[0] + 1
            else:
                bit_count[1] = bit_count[1] + 1
        new_remaining_data_oxygen = []
        if bit_count[0] > bit_count[1]:
            for line in remaining_data_oxygen:
                if int(line[i]) == 0:
                    new_remaining_data_oxygen.append(line)
        else:
            for line in remaining_data_oxygen:
                if int(line[i]) == 1:
                    new_remaining_data_oxygen.append(line)
        remaining_data_oxygen = new_remaining_data_oxygen
        i = i +1

    remaining_data_co2 = DIAGNOSTIC_DATA
    i = 0
    while i < len(DIAGNOSTIC_DATA[0]) and len(remaining_data_co2) > 1:
        #First value for 0's, second for 1's
        bit_count = [0,0]
        for line in remaining_data_co2:
            if int(line[i]) == 0:
                bit_count[0] = bit_count[0] + 1
            else:
                bit_count[1] = bit_count[1] + 1
        new_remaining_data_co2 = []
        if bit_count[0] <= bit_count[1]:
            print("Less 0's, keeping them")
            for line in remaining_data_co2:
                if int(line[i]) == 0:
                    new_remaining_data_co2.append(line)
        else:
            print("Less 1's, keeping them")
            for line in remaining_data_co2:
                if int(line[i]) == 1:
                    new_remaining_data_co2.append(line)
        remaining_data_co2 = new_remaining_data_co2
        print(remaining_data_co2)
        print(i)
        i = i + 1
    print(remaining_data_oxygen)
    print(remaining_data_co2)
    print(int(remaining_data_oxygen[0],base=2) * int(remaining_data_co2[0], base=2))

main()