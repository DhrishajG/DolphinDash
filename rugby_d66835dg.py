import sys

# to take the input file and arrange the scores in appropriate lists
def takeScore():
    lines = input_file.readlines()
    for line in lines:
        pos = 2
        while pos < len(line):
            if line[(pos-2):pos] == "T1":
                t1_scores.append(line[pos])
            elif line[(pos-2):pos] == "T2":
                t2_scores.append(line[pos])
            pos += 3

def calScore(arr):
    tot = 0
    for i in range(len(arr)):
        if arr[i] == "t":
            tot += 5
        elif arr[i] == "c":
            tot += 2
        elif arr[i] == "p":
            tot += 3
        elif arr[i] == "d":
            tot += 3
    return tot

t1_scores = []
t2_scores = []

f_in = sys.argv[1]
f_out = sys.argv[2]

input_file = open(f_in, "r")
output_file = open(f_out, "w")
takeScore()

tot_t1 = calScore(t1_scores)
tot_t2 = calScore(t2_scores)

output_message = str(tot_t1) + ":" + str(tot_t2)

output_file.write(output_message)
