import random

def Get_Lotto():
    loto_num=[]
    for i in range(1,31):
        loto_num.append(random.randint(1,46))
    
    s="☆★☆★ 로또 번호  ★☆★☆\n────────────────\n"
    for i in range(0,5):
        for j in range(0,6):
            s= s+f" [{loto_num[i+5*j]}]"
        s= s+ f"\n"
    s= s+ f"────────────────\n☆★☆ 로또 번호  ★☆★\n────────────────\n"
    return s
