CREATE TABLE IF NOT EXISTS markets (
    marketTicker TEXT PRIMARY KEY,
    eventTicker TEXT NOT NULL,

    economicVariable TEXT NOT NULL,
    operator TEXT NOT NULL,
    strike NUMERIC NOT NULL,

    referenceYear INTEGER NOT NULL,
    referenceMonth INTEGER NOT NULL,

    closeTime TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS marketSnapshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    marketTicker TEXT NOT NULL,
    snapshotTime TEXT NOT NULL,

    yesBid NUMERIC NOT NULL,
    yesAsk NUMERIC NOT NULL,
    noBid NUMERIC NOT NULL,
    noAsk NUMERIC NOT NULL,

    yesBidSize NUMERIC NOT NULL,
    yesAskSize NUMERIC NOT NULL,

    volume NUMERIC NOT NULL,
    openInterest NUMERIC NOT NULL,

    FOREIGN KEY (marketTicker)
        REFERENCES markets(marketTicker),

    UNIQUE (marketTicker, snapshotTime)
);