def ty_le_mon_dat(diem_mon: dict) -> float:
    """Tính tỷ lệ phần trăm môn học đạt"""
    if not diem_mon:
        return 0.0
    so_mon_dat = sum(1 for d in diem_mon.values() if d >= 5)
    return (so_mon_dat / len(diem_mon)) * 100
