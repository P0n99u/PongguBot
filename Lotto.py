import random

def Get_Lotto():
    s=""
    lotto_numbers = random.sample(range(1,46),7)
    lotto_numbers.sort()

    for i in range(0,7):
        if(i>=6):
           s= s + f" 보너스 : {lotto_numbers[:-1]}"
        
        s= s+f" {lotto_numbers[i]}"

    return s