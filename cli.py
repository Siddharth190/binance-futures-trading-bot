import click

from bot.orders import OrderManager

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


@click.command()

@click.option(
    "--symbol",
    required=True,
    help="Example: BTCUSDT"
)

@click.option(
    "--side",
    required=True,
    type=click.Choice(
        ["BUY", "SELL"],
        case_sensitive=False
    )
)

@click.option(
    "--order_type",
    required=True,
    type=click.Choice(
        ["MARKET", "LIMIT"],
        case_sensitive=False
    )
)

@click.option(
    "--quantity",
    required=True,
    type=float
)

@click.option(
    "--price",
    required=False,
    type=float
)

def main(
    symbol,
    side,
    order_type,
    quantity,
    price
):

    try:

        validate_symbol(symbol)

        validate_side(side)

        validate_order_type(order_type)

        validate_quantity(quantity)

        order_manager = OrderManager()

        print("\n========== ORDER REQUEST ==========")

        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")

        if order_type.upper() == "LIMIT":
            print(f"Price      : {price}")

        print("===================================")

        if order_type.upper() == "MARKET":

            response = (
                order_manager.place_market_order(
                    symbol,
                    side,
                    quantity
                )
            )

        else:

            if price is None:

                raise ValueError(
                    "LIMIT order requires --price"
                )

            validate_price(price)

            response = (
                order_manager.place_limit_order(
                    symbol,
                    side,
                    quantity,
                    price
                )
            )

        print("\nORDER SUCCESSFUL")

        print(
            f"Order ID      : "
            f"{response.get('orderId')}"
        )

        print(
            f"Status        : "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty  : "
            f"{response.get('executedQty')}"
        )

        avg_price = response.get("avgPrice", "0.00")

        print(
            f"Average Price : {avg_price}"
        )

    except Exception as e:

        print(
            f"\nORDER FAILED: {e}"
        )


if __name__ == "__main__":
    main()