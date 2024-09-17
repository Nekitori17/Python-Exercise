import os

tong_den = int(input("Nhập một số để tính tổng: "))

while tong_den <= 2:
    os.system("cls")
    tong_den = int(input("Không thể để số nhỏ hơn hoặc bằng hai: "))

tong_le = 0
tong_chan = 0

for i in range(1, tong_den + 1):
    if i % 2 == 0:
        tong_chan += i
    if i % 2 != 0:
        tong_le += i

print(f"Tổng các số lẻ là: {tong_le}")
print(f"Tổng các số chẵn là: {tong_chan}")
