from UTILS.number_operation import *

danh_sac_dau_vao = str(input("Nhập danh sách số nguyên phân cách bằng phím cách: ")).strip()
phan_cach = ", "

while not danh_sac_dau_vao:
  danh_sac_dau_vao = str(input("Nhập lại danh sách không thể để trống: "))

danh_sach_so = [int(i) for i in danh_sac_dau_vao.split()]

print(f"Tổng các số lẻ là {tinh_tong(danh_sach_so, "le")}")
print(f"Tổng các số chẵn là {tinh_tong(danh_sach_so, "chan")}")
print(f"Danh sách được sắp xếp: {phan_cach.join(map(str, sorted(danh_sach_so)))}")


