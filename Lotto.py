import random

def Get_Lotto():
    s="☆★☆★ 로또 번호  ★☆★☆\n─────────────\n"
    loto_num = []
    for i in range(0,5):
    for j in range(0,6):
        loto_num[i*5+j]=random.randint(1,46)
        s= s + f"{loto_num[i+5*j]}"
    
    s= s+ f"\n─────────────\n☆★☆ 로또 번호  ★☆★\n─────────────\n"
    return s
