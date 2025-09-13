def add_item(cart, price):
    """
    Thêm món hàng vào giỏ và trả về giỏ hàng cập nhật
    """
    cart.append(price)
    return cart

def calculate_total(cart):
    """
    Tính tổng chi phí giỏ hàng
    """
    return sum(cart)
