import os
from dotenv import load_dotenv

load_dotenv()

KALSHI_MARKETS_API = os.getenv("KALSHI_MARKETS_API")

SUPPORTED_SERIES = {
    "CPI": ["KXCPI"],
    "CORE_CPI": ["KXCPICORE"],
    "UNEMPLOYMENT": ["KXU3"]
}