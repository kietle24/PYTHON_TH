def them_khach_hang(ds_khach: list, ten: str, loai: str) -> list:
    """
    Hàm thêm khách hàng mới vào danh sách
    ds_khach: list các tuple (tên, loại phòng)
    ten: tên khách hàng
    loai: loại phòng (VIP/Thường)
    """
    ds_khach.append((ten, loai))
    return ds_khach
