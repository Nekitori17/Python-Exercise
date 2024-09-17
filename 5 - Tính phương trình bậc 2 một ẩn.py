from UTILS.fraction_operation import *
from UTILS.get_output import *
import math

print("Biểu Thức: ax² + bx + c = 0")

a, b, c = int(input("Nhập a: ")), int(input("Nhập b: ")), int(input("Nhập c: "))

if a == 0:
    print("Phương trình vô nghiệm")

elif a + b + c == 0:
    ket_qua = tuple_hay_so(c, a)

    print("Nghiệm x1 là: 1")
    in_ra_phan_so("Nghiệm x2 là: {0}", ket_qua)

elif a - b + c == 0:
    ket_qua = tuple_hay_so(-c, a)

    print("Nghiệm x1 là: 1")
    in_ra_phan_so("Nghiệm x2 là: {0}", ket_qua)

elif b**2 - 4 * a * c < 0:
    print("Phương trình vô nghiệm")

elif b**2 - 4 * a * c == 0:
    ket_qua = tuple_hay_so(-b, (2 * a))

    in_ra_phan_so("Nghiệm kép x1 và x2 là: {0}", ket_qua)

else:
    delta = b**2 - 4 * a * c

    ket_qua_nghiem_1 = tuple_hay_so(-b + math.sqrt(delta), 2 * a)
    ket_qua_nghiem_2 = tuple_hay_so(-b - math.sqrt(delta), 2 * a)

    in_ra_phan_so("Nghiệm x1 là: {0}", ket_qua_nghiem_1)
    in_ra_phan_so("Nghiệm x2 là: {0}", ket_qua_nghiem_2)
