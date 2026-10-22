from src.kalshi.client import KalshiClient
from src.database.snapshot import saveSnapshot

kalshiClient = KalshiClient()

markets = kalshiClient.getEconomicMarkets()
saveSnapshot(markets)