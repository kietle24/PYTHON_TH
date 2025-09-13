def forecast(temps):
    """
    Hàm dự báo thời tiết
    Trả về "Nóng" nếu có ngày nào > 30°C, ngược lại "Bình thường"
    """
    if any(t > 30 for t in temps):
        return "Nóng"
    return "Bình thường"