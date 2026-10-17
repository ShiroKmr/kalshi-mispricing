from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_snake
from decimal import Decimal
from datetime import datetime

# Expected relevant values of the market
class Market(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_snake
    )

    ticker: str # Name of the ticker
    eventTicker: str #name of the parent event

    title: str # normal name of the market
    subtitle: str | None = None #subtitle of the market

    openTime: datetime 
    closeTime: datetime
    expirationTime: datetime

    strikeType: str | None = None #>,< or =
    floorStrike: float | None = None #bottom
    capStrike: float | None = None #upper
    functionalStrike: str | None = None # if the settlement value is determined based on a function

    yesBidDollars: Decimal | None = None # sell yes
    yesAskDollars: Decimal | None = None # buy yes
    noBidDollars: Decimal | None = None
    noAskDollars: Decimal | None = None

    yesBidSizeFp: Decimal | None = None #number of possible contracts sell
    yesAskSizeFp: Decimal | None = None

    volumeFp: Decimal #all deals
    volume24hFp: Decimal #all deals in the last 24h
    openInterestFp: Decimal #open deals


# Filter markets from cursor
class MarketsResponse(BaseModel):
    markets: list[Market]
    cursor: str | None = None