# booking_module.py
def add_booking(booked_times, new_time):
    """
    Thêm giờ đặt bàn vào tuple nếu chưa có.
    Trả về tuple mới đã cập nhật.
    """
    if new_time in booked_times:
        return booked_times  # không thay đổi vì đã tồn tại
    else:
        return booked_times + (new_time,)
