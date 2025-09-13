# bmi_module.py
def classify_bmi(bmi):
    """
    Trả về phân loại theo BMI:
    - < 18.5: gầy
    - 18.5 – 24.9: bình thường
    - >= 25: thừa cân
    """
    if bmi < 18.5:
        return "Gầy"
    elif 18.5 <= bmi < 25:
        return "Bình thường"
    else:
        return "Thừa cân"
