# Given an integer as input, can you round it to the next (meaning, "higher") 5?

# Examples:

# input:    output:
# 0    ->   0
# 2    ->   5
# 3    ->   5

def round_to_next5(n):
    if n % 5 > 0 and n > 0 :
        n = int(n/5) + 1
        n = 5*n
    if n < 0 :
        n = int(n/5)
        n = 5*n
    return n
