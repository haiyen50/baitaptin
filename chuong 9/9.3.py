import math
def tinh_bmi(can_nang, chieu_cao):
    bmi = can_nang/math.pow(chieu_cao*chieu_cao,1)
    return bmi
a=float (input("nhập cân nặng(kg):"))
b=float (input("nhập chiều cao(m):"))
print("chỉ số bmi của bạn là: %0.2f"%(tinh_bmi(a,b)))
tinh_bmi(a,b)
if a<18.5:
    print("gầy")
if a>=25:
    print("Thừa cân")
if a>18.5 and a<24.99:
    print("Bình thường")