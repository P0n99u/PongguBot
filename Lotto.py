import random

def Get_Lotto():
    s=""
    lotto_numbers = random.sample(range(1,46),7)
    lotto_numbers.sort()

    for i in range(0,6):
        
        s= s+f" {lotto_numbers[i]}"

    return s
