r=float(input("nhập số r:"))
a=float(input("nhập số a:"))
b=float(input("nhập số b:"))
s=lambda r_diện_tích_hình_tròn:3.14*(r**2)
p=lambda r_chu_vi_hình_tròn: 3.14*2*r
S=lambda a,b_diện_tích_hcn: a*b
P=lambda a,b_chu_vi_hcn: (a+b)*2
print("diện tích hình tròn:",s(r))
print("chu vi hình tròn:",p(r))
print("diện tích hcn:",S(a,b))
print("chu vi hcn:",P(a,b))
