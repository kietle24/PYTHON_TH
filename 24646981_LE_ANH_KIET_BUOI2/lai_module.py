# c - lai_module.py
def tinh_lai(tien_gui):
    """
    Hàm tính lãi suất dựa trên số tiền gửi
    :param tien_gui: số tiền gửi (float)
    :return: tiền lãi (float)
    """
    lai_suat = 0.05
    if tien_gui > 100_000_000:
        lai_suat += 0.01
    return tien_gui * lai_suat
