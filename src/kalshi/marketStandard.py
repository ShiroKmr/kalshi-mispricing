from pydantic import BaseModel, ConfigDict
from enum import Enum
from pydantic.alias_generators import to_snake
from decimal import Decimal
from datetime import datetime, date

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
    floorStrike: Decimal | None = None #bottom
    capStrike: Decimal | None = None #upper
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

class ComparisonOperator(Enum):
    GREATER = ">"
    LESS = "<"

class ReferencePeriod(BaseModel):
    year: int
    month: int

class EconomicContract(BaseModel):
    economicVariable: str
    operator: ComparisonOperator
    strike: Decimal
    referencePeriod: ReferencePeriod

class EconomicMarket(BaseModel):
    market: Market
    contract: EconomicContract

class orderBook(BaseModel):
    yesBidDollars: Decimal | None = None
    yesAskDollars: Decimal | None = None
    noBidDollars: Decimal | None = None
    noAskDollars: Decimal | None = None

    yesBidSizeFp: Decimal | None = None
    yesAskSizeFp: Decimal | None = None