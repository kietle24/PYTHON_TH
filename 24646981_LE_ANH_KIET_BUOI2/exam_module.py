def pass_rate(scores):
    """
    Hàm tính tỷ lệ đậu
    Input: dictionary {tên: điểm}
    Output: phần trăm học viên đậu
    """
    total = len(scores)
    if total == 0:
        return 0
    passed = sum(1 for s in scores.values() if s >= 5)
    return (passed / total) * 100
