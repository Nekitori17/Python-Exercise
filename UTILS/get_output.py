from UTILS.fraction_operation import *
from typing import *
import re

def in_ra_phan_so(text: str, object: any, decimal: str = "/"):
  if isinstance(object, tuple):
    print(str(text).format(f"{object[0]}{decimal}{object[1]}"))
  else:
    print(str(text).format(object))

def tuple_hay_so(so_bi_chia: int, so_chia: int) -> Tuple[int, int] | int:
  if so_bi_chia % so_chia != 0:
    return rut_gon(so_bi_chia, so_chia)
  else:
    return so_bi_chia / so_chia

_regex_phan_so = r"([+-]?\d+([+\-*/]\d+)*)\/([+-]?\d+([+\-*/]\d+)*)"

def phan_so_thanh_tuple(phan_so: str, regex: str = _regex_phan_so) -> Tuple[int, int] | None:
    fullmatch = re.fullmatch(regex, phan_so)
    if fullmatch:
        return eval(fullmatch.group(1)), eval(fullmatch.group(3))
    return None