import re
from UTILS.get_output import *

regex_phan_so = r"([+-]?\d+([+\-*/]\d+)*)\s+([+-]?\d+([+\-*/]\d+)*)"

phan_so_1_dau_vao = str(input("Nhập số bị trừ (vd: 5 6): "))

while not re.match(regex_phan_so, phan_so_1_dau_vao):
  phan_so_1_dau_vao = str(input("Nhập lại số bị trừ (vd: 5 6): "))

phan_so_1 = phan_so_thanh_tuple(phan_so_1_dau_vao, regex_phan_so)

while phan_so_1[1] == 0:
  phan_so_1_dau_vao = str(input("Vui lý số bị trừ. Không thể để mẫu bằng 0! (vd: 5 6): "))
  phan_so_1 = phan_so_thanh_tuple(phan_so_1_dau_vao, regex_phan_so)

phan_so_2_dau_vao = str(input("Nhập số trừ (vd: 5 6): "))

while not re.match(regex_phan_so, phan_so_2_dau_vao):
  phan_so_2_dau_vao = str(input("Nhập lại số trừ (vd: 5 6): "))

phan_so_2 = phan_so_thanh_tuple(phan_so_2_dau_vao, regex_phan_so)

while phan_so_2[1] == 0:
  phan_so_2_dau_vao = str(input("Vui lý nhập lại so trừ. Không thể được mẫu bằng 0! (vd: 5 6): "))
  phan_so_2 = phan_so_thanh_tuple(phan_so_2_dau_vao, regex_phan_so)


if phan_so_1[1] == phan_so_2[1]:
  ket_qua = tuple_hay_so(phan_so_1[0] - phan_so_2[0], phan_so_1[1])
  in_ra_phan_so("Hiệu hai phân số là: {0}", ket_qua, " ")
else:
  ket_qua = tuple_hay_so((phan_so_1[0] * phan_so_2[1]) - (phan_so_2[0] * phan_so_1[1]), phan_so_1[1] * phan_so_2[1])
  in_ra_phan_so("Hiệu hai phân số là: {0}", ket_qua, " ")

