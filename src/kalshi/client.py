import httpx
from datetime import datetime
from src.kalshi.config import KALSHI_MARKETS_API, SUPPORTED_SERIES
from src.kalshi.marketStandard import MarketsResponse, Market, EconomicMarket, EconomicContract, ComparisonOperator, ReferencePeriod

# Get the list of all the markets that pass to the params
class KalshiClient:
    # Create the base client to speed up the requests
    def __init__(self):
        self.httpClient = httpx.Client(base_url=KALSHI_MARKETS_API)

    def getMarkets(self, status: str, seriesTicker: str) -> list[Market]:
        markets = []

        # Create the first request and save the response
        request = self.httpClient.get("", params={"status": status,
                                                  "series_ticker": seriesTicker
                                                  })
        request.raise_for_status()
        data = request.json()
        response = MarketsResponse.model_validate(data)

        # Fetch the first page
        cursor = response.cursor
        markets.extend(response.markets)

        # If there're further markets, save them until there're none
        while cursor:
            request = self.httpClient.get("", params={"status": status,
                                                      "series_ticker": seriesTicker,
                                                      "cursor": cursor})
            request.raise_for_status()
            data = request.json()
            response = MarketsResponse.model_validate(data)
            markets.extend(response.markets)
            cursor = response.cursor

        return markets

    # Get ALL the needed markets (CPI, core CPI and unemployment)
    def getEconomicMarkets(self) -> list[EconomicMarket]:
        economicMarkets = []

        for economicVariable, seriesTickers in SUPPORTED_SERIES.items():
            for seriesTicker in seriesTickers:
                seriesMarkets = self.getMarkets(status="open", seriesTicker=seriesTicker)
            
                for market in seriesMarkets:    
                    if market.strikeType == "greater":
                        operator = ComparisonOperator.GREATER
                        strike = market.floorStrike
                    elif market.strikeType == "less":
                        operator = ComparisonOperator.LESS
                        strike = market.capStrike
                    else:
                        raise ValueError(f"Unsupported strike type: {market.strikeType}")

                    # Split the event ticker NAME-TIME by -
                    periodCode = market.eventTicker.split("-")[-1]

                    # Take the time period from the eventTicker
                    period = datetime.strptime(periodCode, "%y%b")

                    periodMarket = ReferencePeriod(year=period.year,
                                                   month=period.month)

                    economicMarkets.append(EconomicMarket(market=market,
                                                            contract=EconomicContract(economicVariable=economicVariable, 
                                                                                      operator=operator, 
                                                                                      strike=strike,
                                                                                      referencePeriod=periodMarket)))
        
        return economicMarkets
