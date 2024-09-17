import os

tong_den = int(input("Nhập số cần tính tổng các số nguyên tố đến: "))

while tong_den <= 2:
    os.system("cls")
    tong_den = int(input("Không thể để số nhỏ hơn hoặc bằng hai: "))


def kiem_tra_so_nguyen_to(so: int) -> bool:
    la_so_nguyen_to = True
    if so == 1:
        return False
    elif so == 2:
        return True
    else:
        for i in range(2, so):
            if so % i == 0:
                la_so_nguyen_to = False
                break
    return la_so_nguyen_to


tong = 0
for i in range(1, tong_den + 1):
    if kiem_tra_so_nguyen_to(i):
        tong += i

print(f"Tổng các số nguyên tố từ 1 đến {tong_den} là: {tong}")
