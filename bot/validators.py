def validate_symbol(symbol):

    if not symbol:
        raise ValueError(
            "Symbol cannot be empty"
        )

    if not symbol.endswith("USDT"):
        raise ValueError(
            "Only USDT futures pairs are supported"
        )


def validate_side(side):

    if side.upper() not in [
        "BUY",
        "SELL"
    ]:
        raise ValueError(
            "Side must be BUY or SELL"
        )


def validate_order_type(order_type):

    if order_type.upper() not in [
        "MARKET",
        "LIMIT"
    ]:
        raise ValueError(
            "Order type must be MARKET or LIMIT"
        )


def validate_quantity(quantity):

    quantity = float(quantity)

    if quantity <= 0:
        raise ValueError(
            "Quantity must be greater than 0"
        )


def validate_price(price):

    price = float(price)

    if price <= 0:
        raise ValueError(
            "Price must be greater than 0"
        )