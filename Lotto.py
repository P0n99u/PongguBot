import random

def Get_Lotto():
    s=""
    lotto_numbers = random.sample(range(1,46),30)
    lotto_numbers.sort()

    for i in range(0,30):
        if(i>=5):
           s= s + "\n"
        
        s= s+f" {lotto_numbers[i]}"

    return s
