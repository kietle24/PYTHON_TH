# c - calo_module.py
def tinh_tong_calo(danh_sach_nguyen_lieu):
    """
    Hàm tính tổng calo từ danh sách nguyên liệu
    :param danh_sach_nguyen_lieu: list chứa tuple (tên, calo)
    :return: tổng calo (int)
    """
    return sum(calo for _, calo in danh_sach_nguyen_lieu)
