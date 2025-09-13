def tao_bao_cao(tien_do: dict) -> str:
    """
    Hàm tạo báo cáo tiến độ dự án.
    Input: dictionary {nhiệm vụ: % hoàn thành}
    Output: chuỗi báo cáo
    """
    report = "BÁO CÁO TIẾN ĐỘ DỰ ÁN\n"
    report += "------------------------\n"
    for task, percent in tien_do.items():
        status = "Hoàn thành" if percent == 100 else "Chưa hoàn thành"
        report += f"{task}: {percent}% - {status}\n"
    return report
