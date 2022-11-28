#!/usr/bin/python

global DIAGNOSTIC_DATA 
DIAGNOSTIC_DATA =  open("input.txt","r").read().splitlines()

def main():
    count_of_zeros = []
    count_of_ones = []
    
    for line in DIAGNOSTIC_DATA:
        for iteration,char in enumerate(line):
            #Build this to scale with arbitrarily large binary values.
            if iteration >= len(count_of_zeros):
                count_of_zeros.append(0)
            if iteration >= len(count_of_ones):
                count_of_ones.append(0)
            if int(char) == 0:
                count_of_zeros[iteration] = count_of_zeros[iteration] + 1
            if int(char) == 1:
                count_of_ones[iteration] = count_of_ones[iteration] + 1
    gamma_output = ""
    epsilon_output = ""

    for iteration,value in enumerate(count_of_zeros):
        if count_of_zeros[iteration] > count_of_ones[iteration]:
            gamma_output = gamma_output + "0"
            epsilon_output = epsilon_output + "1"
        else:
            gamma_output = gamma_output + "1"
            epsilon_output = epsilon_output + "0"
    print("Gamma output = " + gamma_output)
    print("Epsilon output = " + epsilon_output)
    print(int(gamma_output,base=2) * int(epsilon_output,base=2))

main()