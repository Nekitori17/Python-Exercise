import re

cu_phap_ma_tran = r"^\d+ \d+ \d+ \d+$"

chuoi_ma_tran_1 = str(input("Nhập mảng hàng 1: ")).strip()
while not re.fullmatch(cu_phap_ma_tran, chuoi_ma_tran_1):
  chuoi_ma_tran_1 = str(input("Nhập lại mảng hàng 1: ")).strip()
ma_tran_1 = [int(i) for i in chuoi_ma_tran_1.split()]

chuoi_ma_tran_2 = str(input("Nhập mảng hàng 2: ")).strip()
while not re.fullmatch(cu_phap_ma_tran, chuoi_ma_tran_2):
  chuoi_ma_tran_2 = str(input("Nhập lại mảng hàng 2: ")).strip()
ma_tran_2 = [int(i) for i in chuoi_ma_tran_2.split()]

chuoi_ma_tran_3 = str(input("Nhập mảng hàng 3: ")).strip()
while not re.fullmatch(cu_phap_ma_tran, chuoi_ma_tran_3):
  chuoi_ma_tran_3 = str(input("Nhập lại mảng hàng 3: ")).strip()
ma_tran_3 = [int(i) for i in chuoi_ma_tran_3.split()]

print(f"Tổng hàng 1 là: {sum(ma_tran_1)}")
print(f"Tổng hàng 2 là: {sum(ma_tran_2)}")
print(f"Tổng hàng 3 là: {sum(ma_tran_3)}")

ma_tran_3x4 = [ma_tran_1] + [ma_tran_2] + [ma_tran_3]

for cot_so in range(4):
  tong = 0
  for hang_so in ma_tran_3x4:
    tong += hang_so[cot_so]
  print(f"Tổng của cột {cot_so}: {tong}")
