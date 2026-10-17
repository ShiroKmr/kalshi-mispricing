import httpx
from src.config import KALSHI_MARKETS_API
from src.marketStandard import Market, MarketsResponse

params = {
    "series-ticker": "KXCPI",
    "status": "open"
}

request = httpx.get(KALSHI_MARKETS_API, params=params)
request.raise_for_status()

data = request.json()
marketsResponse = MarketsResponse.model_validate(data)

print(marketsResponse.markets)