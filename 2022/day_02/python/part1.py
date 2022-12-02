#!/usr/bin/python

rps_strategy =  open("input.txt","r").read().splitlines()


#A = X (1) (Rock)
#B = Y (2) (Paper)
#C = Z (3) (Scissors)
#Tie is 3 points, win is 6
#A/X > B/Y
#B/Y > C/Z
#C/Z > A/X


def main():
    score = 0
    for line in rps_strategy:
        score = score + shape_score(line)
        score = score + win_loss_tie(line)
    print(score)

def shape_score(line):
    if "X" in line:
        return 1
    if "Y" in line:
        return 2
    if "Z" in line:
        return 3

def win_loss_tie(line):
    if "X" in line:
        if "A" in line:
            return 3
        if "B" in line:
            return 0
        if "C" in line:
            return 6
    if "Y" in line:
        if "A" in line:
            return 6
        if "B" in line:
            return 3
        if "C" in line:
            return 0
    if "Z" in line:
        if "A" in line:
            return 0
        if "B" in line:
            return 6
        if "C" in line:
            return 3

main()
