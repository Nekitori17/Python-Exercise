from typing import *

def tinh_tong(danh_sach: List[int], loai: Literal["chan", "le", "nguyen_to", "thuong"]) -> int:
  match loai:
    case "chan":
      tong = 0
      for so in danh_sach:
        if so % 2 == 0:
          tong += so
      return tong
    case "le":
      tong = 0
      for so in danh_sach:
        if not so % 2 == 0:
          tong += so
      return tong
    case "nguyen_to":
      tong = 0
      for so in danh_sach:
        if kiem_tra_so_nt(so):
          tong += so
      return tong

def kiem_tra_so_nt(so: int) -> bool:
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