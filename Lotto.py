import random

def Get_Lotto():
    s="☆★☆★ 로또 번호  ★☆★☆\n─────────────\n"
    for i in range(0,5):
        lotto_numbers[6] = random.sample(range(1,46),6)
        lotto_numbers.sort()
        for j in range(0,5):
           s= s+f" {lotto_numbers[i]}"
    
    s= s+ f"\n─────────────\n☆★☆ 로또 번호  ★☆★\n─────────────\n"
    return s
