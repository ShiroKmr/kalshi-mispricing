# Kalshi Mispricing

A research project for comparing **model-estimated probabilities** with **Kalshi market prices** and identifying potential mispricing opportunities.

The project combines economic/news information, machine learning probability estimates, and market data. The final goal is to evaluate whether a trade has positive expected value after accounting for fees, liquidity, and risk.

## Current Status

The data collection layer is currently implemented.

- Fetch Kalshi market data through the Kalshi API
- Standardize API responses with Pydantic
- Store market snapshots in a local SQL database
- Save current market prices and related market information using `saveSnap.py`

Snapshots will later be used both for training models and for evaluating historical trading decisions.

## Next Steps

The next development stages will focus on:

1. Collecting a larger historical dataset of Kalshi snapshots.
2. Adding external economic and news information.
3. Using Nemotron to convert unstructured news into structured features.
4. Building a logistic regression baseline for fair probability estimation.
5. Training an XGBoost model and comparing it with the baseline.
6. Comparing model probabilities with Kalshi market prices.
7. Adding fees, arbitrage checks, liquidity, and risk calculations.
8. Building a paper-trading system to evaluate the strategy without real capital.
9. Measuring profitability, calibration, and prediction quality over time.

## Tools

- **httpx** — Kalshi API requests
- **Pydantic** — validation and standardization of API responses
- **SQL** — direct database operations
- **python-dotenv** — environment variable management
- **pytest** — automated testing
- **uv** — Python dependency and environment management

## Running Snapshot Collection

```bash
uv run python -m src.saveSnap
```

Environment variables required by the project should be stored in `.env`.

`.env.example` contains the expected configuration without private credentials.
