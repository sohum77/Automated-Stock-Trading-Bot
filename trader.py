# trader.py (Final Robust Version for Paper Trading)
import os
import time
import logging
import numpy as np
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame

# ------------------------------------------------------------
# Logging setup
# ------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

# ------------------------------------------------------------
# Read Paper Trading API credentials (environment variables)
# ------------------------------------------------------------
PUB_KEY = os.getenv("APCA_API_KEY_ID")
SEC_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"  # Paper trading endpoint

# ------------------------------------------------------------
# Create API connection
# ------------------------------------------------------------
api = tradeapi.REST(PUB_KEY, SEC_KEY, BASE_URL, api_version="v2")

SYM = "SPY"  # Change to another stock (AAPL, TSLA, etc.)
pos_held = False


# ------------------------------------------------------------
# Function to fetch close prices safely
# ------------------------------------------------------------
def fetch_close_list(symbol: str, limit: int = 5):
    """
    Robustly fetch last `limit` one-minute close prices from Alpaca's IEX feed.
    Handles DataFrame and bar-list formats safely.
    """
    try:
        # Use 'iex' feed (free for paper trading)
        bars_obj = api.get_bars(symbol, TimeFrame.Minute, limit=limit, feed="iex")

        # Try to extract close prices from dataframe
        df = getattr(bars_obj, "df", None)
        if df is not None and not df.empty:
            if "close" in df.columns:
                return df["close"].astype(float).tolist()
            # Handle multi-index or tuple columns
            for col in df.columns:
                if (isinstance(col, tuple) and col[-1] == "close") or (
                    isinstance(col, str) and "close" in col
                ):
                    return df[col].astype(float).tolist()

        # Fallback: iterate over bar objects
        return [float(bar.c) for bar in bars_obj]

    except Exception as e:
        logging.warning(f"Could not fetch bars for {symbol}: {e}")
        return []


# ------------------------------------------------------------
# Main trading loop
# ------------------------------------------------------------
while True:
    try:
        logging.info("Checking Price...")
        close_list = fetch_close_list(SYM, limit=5)

        if len(close_list) < 1:
            logging.warning(
                "No bars returned (market closed or no data). Skipping this cycle."
            )
            time.sleep(60)
            continue

        ma = np.mean(close_list)
        last_price = float(close_list[-1])
        logging.info(f"MA: {ma:.4f} | Last: {last_price:.4f}")

        # Buy logic
        if ma + 0.1 < last_price and not pos_held:
            logging.info("Buying 1 share...")
            try:
                api.submit_order(
                    symbol=SYM, qty=1, side="buy", type="market", time_in_force="gtc"
                )
                pos_held = True
            except Exception as e:
                logging.error(f"Buy order failed: {e}")

        # Sell logic
        elif ma - 0.1 > last_price and pos_held:
            logging.info("Selling 1 share...")
            try:
                api.submit_order(
                    symbol=SYM, qty=1, side="sell", type="market", time_in_force="gtc"
                )
                pos_held = False
            except Exception as e:
                logging.error(f"Sell order failed: {e}")

    except Exception as e:
        logging.exception(f"Error in main loop: {e}")

    # Wait 1 minute before checking again
    time.sleep(60)
