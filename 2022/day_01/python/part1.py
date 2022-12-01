#!/usr/bin/python

elf_cal_list =  open("elf_cals.txt","r").read().splitlines()

def main():
    top_elf = 0
    second_elf = 0
    third_elf = 0
    current_elf = 0
    for line in elf_cal_list:
        if line != '':
            current_elf = current_elf + int(line)
        else:
            if current_elf > top_elf:
                third_elf = second_elf
                second_elf = top_elf
                top_elf = current_elf
                
            current_elf = 0
    print("Top Elf: " + str(top_elf))
    print("Sum Top Three: " + str(int(top_elf+second_elf+third_elf)) )

main()