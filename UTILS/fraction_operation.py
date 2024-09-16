from typing import *

def tim_uoc(x: int) -> List[int] | None:
  cac_uoc = []
  if x == 0:
    return []
  for i in range(1, abs(x) + 1):
    if x % i == 0:
      cac_uoc.append(i)
  return cac_uoc

def ucln(a: int, b: int) -> int:
  cac_uoc_a = tim_uoc(a)
  cac_uoc_b = tim_uoc(b)
  so_nhieu_uoc_nhat = cac_uoc_a if len(cac_uoc_a) > len(cac_uoc_b) else cac_uoc_b

  nth = len(so_nhieu_uoc_nhat) - 1
  while nth >= 0:
    if so_nhieu_uoc_nhat[nth] in cac_uoc_a and so_nhieu_uoc_nhat[nth] in cac_uoc_b:
      return so_nhieu_uoc_nhat[nth]
    nth -= 1
    
def rut_gon(tu: int, mau: int) -> Tuple[int, int]:
  uoc_chung_ln = ucln(tu, mau)
  return tu / uoc_chung_ln, mau / uoc_chung_ln

