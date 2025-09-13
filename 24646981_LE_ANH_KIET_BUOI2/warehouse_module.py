# warehouse_module.py
def update_stock(stock_dict, product, order_qty):
    """
    stock_dict: dict {sản phẩm: số lượng tồn}
    product: tên sản phẩm
    order_qty: số lượng đặt

    Trả về stock_dict đã cập nhật sau khi trừ hàng (nếu đủ).
    """
    if product in stock_dict:
        if stock_dict[product] >= order_qty:
            stock_dict[product] -= order_qty
        else:
            print(f"Không đủ hàng cho {product}.")
    else:
        print(f"Sản phẩm {product} không tồn tại trong kho.")
    return stock_dict
