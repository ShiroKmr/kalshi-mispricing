from datetime import datetime, timezone
from src.kalshi.marketStandard import EconomicMarket

import sqlite3

DATABASE_PATH = "data/kalshi.db"

def saveSnapshot(economicMarkets: list[EconomicMarket]):
    snapshotTime = datetime.now(timezone.utc).replace(hour=0,minute=0,second=0,microsecond=0).isoformat()

    connection = sqlite3.connect(DATABASE_PATH)
    connection.execute("PRAGMA foreign_keys = ON")

    for emarket in economicMarkets:
        market = emarket.market
        contract = emarket.contract

        connection.execute(
            """
                INSERT OR IGNORE INTO markets 
                (marketTicker,
                eventTicker,
                economicVariable,
                operator,
                strike,
                referenceYear,
                referenceMonth,
                closeTime)

                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (market.ticker, market.eventTicker, contract.economicVariable, contract.operator.value, str(contract.strike), 
                  contract.referencePeriod.year, contract.referencePeriod.month, market.closeTime.isoformat())
        )

        connection.execute(
            """
                INSERT OR IGNORE INTO marketSnapshots
                (marketTicker,
                snapshotTime,
                yesBid,
                yesAsk,
                noBid,
                noAsk,
                yesBidSize,
                yesAskSize,
                volume,
                openInterest)

                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (market.ticker, snapshotTime, str(market.yesBidDollars), str(market.yesAskDollars), str(market.noBidDollars), str(market.noAskDollars),
                  str(market.yesBidSizeFp), str(market.yesAskSizeFp), str(market.volumeFp), str(market.openInterestFp))
        )

    connection.commit()
    connection.close()