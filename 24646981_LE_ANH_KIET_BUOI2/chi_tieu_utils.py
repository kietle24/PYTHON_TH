def tinh_trung_binh(danh_sach):
    if len(danh_sach) == 0:
        return 0
    return sum(danh_sach) / len(danh_sach)
