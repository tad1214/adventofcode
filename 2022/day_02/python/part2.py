#!/usr/bin/python

rps_strategy =  open("input.txt","r").read().splitlines()


#A = Rock (1)
#B = Paper (2)
#C = Scissors (3)
#X = lose (0)
#Y = draw (3)
#Z = win (6)

def main():
    score = 0
    for line in rps_strategy:
        score = score + win_loss_tie(line)
    print(score)

def win_loss_tie(line):
    score_return = 0
    if "X" in line:
        #keeping this score line here for consistency
        score_return = 0 
        if "A" in line:
            score_return = score_return + 3
        if "B" in line:
            score_return = score_return + 1
        if "C" in line:
            score_return = score_return + 2
    if "Y" in line:
        score_return = 3 
        if "A" in line:
            score_return = score_return + 1
        if "B" in line:
            score_return = score_return + 2
        if "C" in line:
            score_return = score_return + 3
    if "Z" in line:
        #keeping this score line here for consistency
        score_return = 6 
        if "A" in line:
            score_return = score_return + 2
        if "B" in line:
            score_return = score_return + 3
        if "C" in line:
            score_return = score_return + 1
    return score_return
main()
