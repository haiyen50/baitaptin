a=int(input("nhập số:"))
b=0
def kiem_tra_so_hoan_hao(a,b):
    for i in range(1, a):
        if a%i==0:
            b+=i
    return b
kiem_tra_so_hoan_hao(a,b)