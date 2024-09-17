import os

tong_den = int(input("Nhập số để tính tổng: "))
  
while tong_den <= 2:
  os.system("cls")
  tong_den = int(input("Không thể để số nhỏ hoặc bằng hai: "))
      
tong = 0
for i in range(1, tong_den + 1):
  tong += i
  
print(f"Tổng từ 1 đến {tong_den} là: {tong}")