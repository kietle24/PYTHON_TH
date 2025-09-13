def tinh_chi_phi(km: float) -> float:
    """Hàm tính chi phí 1 chuyến đi"""
    don_gia = 10000
    chi_phi = km * don_gia
    if km > 100:
        chi_phi *= 0.9
    return chi_phi

def tong_chi_phi(ds_khoang_cach: list) -> float:
    """Hàm tính tổng chi phí cho danh sách chuyến đi"""
    return sum(tinh_chi_phi(km) for km in ds_khoang_cach)
