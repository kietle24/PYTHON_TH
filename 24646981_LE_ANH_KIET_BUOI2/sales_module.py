# sales_module.py
def calculate_sales(prices):
    """
    prices: danh sách giá gốc của sản phẩm
    trả về: tổng doanh số sau thuế
    Quy tắc thuế:
        - > 1,000,000 VND: 10%
        - <= 1,000,000 VND: 5%
    """
    total = 0
    for p in prices:
        if p > 1_000_000:
            total += p * 1.10
        else:
            total += p * 1.05
    return total
