from tien_ich.lay_dau_ra import *
import math

print("Biểu Thức: ax² + bx + c = 0")

a, b, c = int(input("Nhập a: ")), int(input("Nhập b: ")), int(input("Nhập c: "))

if a == 0:
  print("Phương trình vô nghiệm")

elif a + b + c == 0:
  ket_qua = lay_tuple_hay_so(c, a)

  print("Nghiệm x1 là: 1")
  in_dau_ra("Nghiệm x2 là: {0}", ket_qua)

elif a - b + c == 0:
  ket_qua = lay_tuple_hay_so(-c, a)

  print("Nghiệm x1 là: 1")
  in_dau_ra("Nghiệm x2 là: {0}", ket_qua)

elif b**2 - 4 * a * c < 0:
  print("Phương trình vô nghiệm")

elif b**2 - 4 * a * c == 0:
  ket_qua = lay_tuple_hay_so(-b, (2 * a))

  in_dau_ra("Nghiệm kép x1 và x2 là: {0}", ket_qua)

else:
  delta = b**2 - 4 * a * c

  ket_qua_nghiem_1 = lay_tuple_hay_so(-b + math.sqrt(delta), 2 * a)
  ket_qua_nghiem_2 = lay_tuple_hay_so(-b - math.sqrt(delta), 2 * a)

  in_dau_ra("Nghiệm x1 là: {0}", ket_qua_nghiem_1)
  in_dau_ra("Nghiệm x2 là: {0}", ket_qua_nghiem_2)