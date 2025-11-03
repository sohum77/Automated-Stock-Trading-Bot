# diagnostic_show_buy_sell.py — safe simulation showing one BUY then one SELL
import time, logging
from datetime import datetime, timezone

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger()

# ---- Stub MA and a synthetic price sequence ----
MA = 686.695
# prices: starts below MA, goes above (buy), then falls below (sell)
price_sequence = [685.50, 686.50, 687.10, 688.00, 687.50, 686.80, 686.20, 685.90]

symbol = "DEMO"
position = 0        # 0 = no shares, 1 = holding shares
position_qty = 0
prev_last = None
prev_ma = None

for i, last in enumerate(price_sequence):
    # compute ma (constant in this demo)
    ma = MA
    acct = {'cash': 1000.0, 'buying_power': 1000.0}

    logger.info("DEBUG %s | last=%s | ma=%s | prev_last=%s | prev_ma=%s | pos=%s",
                datetime.now(timezone.utc).isoformat(), last, ma, prev_last, prev_ma, position)

    # true crossover detection
    buy_signal = prev_last is not None and prev_ma is not None and prev_last <= prev_ma and last > ma
    sell_signal = prev_last is not None and prev_ma is not None and prev_last >= prev_ma and last < ma

    # allow a single forced initial buy if no prev exists and price moves above MA
    if prev_last is None and last > ma and position == 0:
        logger.info("BOOTSTRAP: initial condition met -> simulating BUY")
        buy_signal = True

    if buy_signal and position == 0:
        qty = max(1, int(float(acct['cash']) / last))
        logger.info("SIMULATED ORDER -> side=BUY qty=%s price=%s", qty, last)
        position = 1
        position_qty = qty

    elif sell_signal and position == 1:
        qty = position_qty
        logger.info("SIMULATED ORDER -> side=SELL qty=%s price=%s", qty, last)
        position = 0
        position_qty = 0

    else:
        logger.info("No trade this iteration.")

    prev_last, prev_ma = last, ma
    time.sleep(0.8)
