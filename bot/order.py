from binance.exceptions import BinanceAPIException
import time

from bot.client import BinanceClient
from bot.logging_config import get_logger

logger = get_logger()


class OrderManager:

    def __init__(self):
        self.client = BinanceClient().get_client()

    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):

        try:

            logger.info(
                f"REQUEST -> "
                f"Type=MARKET "
                f"Symbol={symbol} "
                f"Side={side} "
                f"Qty={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(
                f"INITIAL RESPONSE -> {response}"
            )

            # Wait for Binance to process order
            time.sleep(1)

            order_info = self.client.futures_get_order(
                symbol=symbol,
                orderId=response["orderId"]
            )

            logger.info(
                f"FINAL ORDER INFO -> {order_info}"
            )

            return order_info

        except BinanceAPIException as e:

            logger.error(
                f"Binance API Error: {e}"
            )

            raise

        except Exception as e:

            logger.error(
                f"Unexpected Error: {e}"
            )

            raise

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        try:

            logger.info(
                f"REQUEST -> "
                f"Type=LIMIT "
                f"Symbol={symbol} "
                f"Side={side} "
                f"Qty={quantity} "
                f"Price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(
                f"RESPONSE -> {response}"
            )

            return response

        except BinanceAPIException as e:

            logger.error(
                f"Binance API Error: {e}"
            )

            raise

        except Exception as e:

            logger.error(
                f"Unexpected Error: {e}"
            )

            raise
