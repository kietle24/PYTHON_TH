# overtime_module.py
def calculate_overtime(work_hours, wage_per_hour=50000):
    """
    work_hours: danh sách số giờ làm việc mỗi ngày
    wage_per_hour: lương giờ (mặc định 50,000 VND)
    Trả về (tổng giờ overtime, tổng tiền thưởng)
    """
    total_hours = 0
    total_pay = 0
    for h in work_hours:
        if h > 8:
            overtime = h - 8
            total_hours += overtime
            total_pay += overtime * wage_per_hour * 1.5
    return total_hours, total_pay
