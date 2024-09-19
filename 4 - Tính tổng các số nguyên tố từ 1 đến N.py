import os
from UTILS.number_operation import *

tong_den = int(input("Nhập số cần tính tổng các số nguyên tố đến: "))

while tong_den <= 2:
  os.system("cls")
  tong_den = int(input("Không thể để số nhỏ hơn hoặc bằng hai: "))

tong = 0
for i in range(1, tong_den + 1):
  if kiem_tra_so_nt(i):
     tong += i
  
print(f"Tổng các số nguyên tố từ 1 đến {tong_den} là: {tong}")

