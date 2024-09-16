import re
from UTILS.fraction_operation import *
from UTILS.get_output import *

regex_phan_so = r"([+-]?\d+([+\-*/]\d+)*)\/([+-]?\d+([+\-*/]\d+)*)"

phan_so_1_dau_vao = str(input("Nhập số thứ nhất (vd: 5/6): "))

while not re.match(regex_phan_so, phan_so_1_dau_vao):
  print("Vui lý nhap lai!")
  phan_so_1_dau_vao = str(input("Nhập số thứ nhất (vd: 5/6): "))

phan_so_1 = phan_so_thanh_tuple(phan_so_1_dau_vao)

while phan_so_1[1] == 0:
  print("Vui lý nhap lai. Không thể để mẫu bằng 0!")
  phan_so_1_dau_vao = str(input("Nhập số thứ nhất (vd: 5/6): "))
  phan_so_1 = phan_so_thanh_tuple(phan_so_1_dau_vao)

phan_so_2_dau_vao = str(input("Nhập số thứ hai (vd: 5/6): "))

while not re.match(regex_phan_so, phan_so_2_dau_vao):
  print("Vui lý nhap lai!")
  phan_so_2_dau_vao = str(input("Nhập số thứ hai (vd: 5/6): "))

phan_so_2 = phan_so_thanh_tuple(phan_so_2_dau_vao)

while phan_so_2[1] == 0:
  print("Vui lý nhap lai. Không thể được mẫu bằng 0!")
  phan_so_2_dau_vao = str(input("Nhập số thứ nhất (vd: 5/6): "))
  phan_so_2 = phan_so_thanh_tuple(phan_so_2_dau_vao)


if phan_so_1[1] == phan_so_2[1]:
  ket_qua = tuple_hay_so(phan_so_1[0] + phan_so_2[0], phan_so_1[1])
  in_ra_phan_so("Tổng hai phân số là: {0}", ket_qua)
else:
  ket_qua = tuple_hay_so((phan_so_1[0] * phan_so_2[1]) + (phan_so_2[0] * phan_so_1[1]), phan_so_1[1] * phan_so_2[1])
  in_ra_phan_so("Tổng hai phân số là: {0}", ket_qua)

