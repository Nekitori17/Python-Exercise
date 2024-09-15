from tien_ich.truy_van_so import rut_gon

def chuyen_phan_so_thanh_tuple(phan_so):
  tu, mau = str(phan_so).split("/", 1)
  return int(eval(tu)), int(eval(mau))

def in_dau_ra(text, object):
  if isinstance(object, tuple):
    print(str(text).format(f"{object[0]}/{object[1]}"))
  else:
    print(str(text).format(object))

def lay_tuple_hay_so(so_bi_chia, so_chia):
  if so_bi_chia % so_chia != 0:
    return rut_gon(so_bi_chia, so_chia)
  else:
    return so_bi_chia / so_chia