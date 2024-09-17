so_dau_vao = int(input("Nhập một số: "))
la_so_nguyen_to = True

if so_dau_vao == 1:
    print("1 không phải là số nguyên tố cũng không phải là hợp số")
elif so_dau_vao == 2:
    print("2 là số nguyên tố")
else:
    for i in range(2, so_dau_vao):
        if so_dau_vao % i == 0:
            la_so_nguyen_to = False
            break
    print(f"{so_dau_vao} là một {'số nguyên tố' if la_so_nguyen_to else 'hợp số'}")