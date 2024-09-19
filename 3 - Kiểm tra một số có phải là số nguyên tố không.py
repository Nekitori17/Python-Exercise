from UTILS.number_operation import *

so_dau_vao = int(input("Nhập một số: "))
la_so_nguyen_to = True

if so_dau_vao == 1:
    print("1 không phải là số nguyên tố cũng không phải là hợp số")
elif so_dau_vao == 2:
    print("2 là số nguyên tố")
else:
    print(f"{so_dau_vao} là một {'số nguyên tố' if kiem_tra_so_nt(so_dau_vao) else 'hợp số'}")