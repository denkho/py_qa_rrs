# 3 ternary         https://www.codewars.com/kata/57202aefe8d6c514300001fd
def sale_hotdogs(n):
    return 100 * n if n < 5 else 90 * n if n >= 10 else n * 95 
# 4 lenStr          https://www.codewars.com/kata/58fa273ca6d84c158e000052
def digits(n):
    return len(str(n))

# 7 beads           https://www.codewars.com/kata/58712dfa5c538b6fc7000569

def count_red_beads(n):
    if n < 2: return 0
    return (n - 1) * 2
    