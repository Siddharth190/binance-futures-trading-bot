import os
from pathlib import Path

from dotenv import load_dotenv
from binance.client import Client

# Load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

class BinanceClient:

    def __init__(self):

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        print("API Key Loaded:", bool(api_key))
        print("API Secret Loaded:", bool(api_secret))

        if not api_key or not api_secret:
            raise ValueError(
                "API credentials not found in .env"
            )

        self.client = Client(
            api_key=api_key,
            api_secret=api_secret,
            testnet=True
        )

    def get_client(self):
        return self.client