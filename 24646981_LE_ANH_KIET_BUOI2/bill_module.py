# bill_module.py
def calculate_bill(prices):
    """
    prices: danh sách giá các món ăn
    trả về: tổng hóa đơn sau khi áp dụng giảm giá
    """
    total = 0
    for price in prices:
        if price > 200_000:
            price *= 0.9
        total += price
    return total
