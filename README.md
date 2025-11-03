# 🤖 Automated Stock Trading Bot

### 📘 About the Project
This project is a **fully automated stock trading bot** built using **Python** and the **Alpaca Trading API**.  
It is designed to **analyze market data**, make **buy/sell decisions** based on moving averages, and **execute simulated trades** automatically.

The bot runs in both:
- 🧠 **Simulation mode** (safe testing using dummy market data)
- 💼 **Paper trading mode** (optional real-time trading using Alpaca’s demo account)

> ⚠️ **Important Note:**  
> The U.S. stock market operates from **Monday to Friday**, typically from **9:30 AM to 4:00 PM EST**,  
> which corresponds to **7:00 PM to 1:30 AM (Indian Standard Time)**.  
> Therefore, **live paper trading using Alpaca will only function during this time window.**  
> Outside of these hours, the bot will not receive live market data and will remain inactive.

---

### 🌍 Real-World Use Cases

This project represents how **algorithmic trading systems** work in professional environments.  
Here are a few real-world applications where this type of bot is useful:

1. 💹 **Retail & Institutional Trading**
   - Used by traders and firms to automate repetitive buy/sell decisions.
   - Helps eliminate emotional trading and ensures consistency in market actions.

2. 📊 **Hedge Funds & Quant Firms**
   - Algorithms like this are the foundation of quantitative trading strategies (e.g., momentum, mean reversion).
   - Can be expanded to manage multiple stocks and optimize portfolio returns.

3. ⏱️ **High-Frequency Trading (HFT) Simulations**
   - The logic used here (price tracking, moving averages, and signals) forms the base of many HFT systems used on global exchanges.

4. 💼 **Financial Education & Research**
   - Perfect for learning how to connect data-driven algorithms with real broker APIs.
   - Helps students and analysts understand algorithmic decision-making and risk management.

5. 📈 **Personal Finance Automation**
   - Can be adapted to help individuals automatically invest, rebalance portfolios, or trigger alerts based on price thresholds.

---

## 🚀 Features

✅ **Automated Decision Making** – Buys and sells stocks based on moving average crossover strategy  
✅ **Real-Time Monitoring** – Continuously checks market prices and updates every minute  
✅ **Simulation Mode** – Safely simulates trades (BUY & SELL) without using real money  
✅ **Paper Trading Ready** – Can connect to Alpaca’s paper trading API for real executions  
✅ **Logging System** – Displays trade decisions, current prices, and actions in the console  

---

## ⚙️ How It Works

1. The bot calculates a **moving average (MA)** for the selected stock.  
2. When the **current price crosses above the MA**, it **buys** the stock.  
3. When the **price drops below the MA**, it **sells** the stock.  
4. In simulation mode, it logs trades instead of executing them live.

---

## 🧩 Project Structure

```
D:\Data Science Projects\Automated Stock Trading Bot
│
├── Screenshots/                     # Contains all proof images (simulation & dashboard)
│   ├── alpaca_paper_trading_dashboard.png       # Alpaca paper trading setup
│   ├── api_connection_output.png                # API connection or testing proof
│   ├── bot_running_output (1).png               # Bot running live output 1
│   ├── bot_running_output (2).png               # Bot running live output 2
│   ├── project_structure.png                    # Screenshot of this folder structure
│   └── trading_bot_buy_sell_simulation.png      # Simulation showing buy/sell trade logic
│
├── venv/                            # Virtual environment (Python dependencies)
│
├── .gitignore                       # Ignores venv, cache, and unnecessary files
│
├── diagnostic_show_buy_sell.py      # Simulation script showing buy & sell logic
│
├── README.md                        # Detailed project documentation
│
├── Requirements.txt                 # Python dependencies list
│
└── trader.py                        # Main live trading bot logic (price monitoring & trade conditions)
```

---

## 🧪 Simulation Output Example

Example log output from `diagnostic_show_buy_sell.py`:

```
2025-10-28 22:35:47,937 INFO SIMULATED ORDER -> side=BUY qty=1 price=687.1
2025-10-28 22:35:51,139 INFO SIMULATED ORDER -> side=SELL qty=1 price=686.2
```

This confirms the bot **successfully detects trading signals** and performs both **BUY and SELL** operations under simulated market conditions.

📸 Screenshot proof:  
**File:** `trading_bot_buy_sell_simulation.png`  
> “Simulated trading output — bot automatically executes buy/sell decisions based on moving average logic.”

---

## 💼 Paper Trading Setup (Future Scope)

You can integrate this bot with a **real Alpaca Paper Trading account** to test in real-time using virtual money.

📸 Screenshot:  
**File:** `alpaca_paper_trading_dashboard.png`  
> “Alpaca Paper Trading Dashboard – confirming connection to simulated trading environment (no real money used).”

### 🔑 How to Enable Paper Trading
1. Create an account at [https://app.alpaca.markets](https://app.alpaca.markets).  
2. Switch to **Paper Trading** mode.
3. Go to **Account Management**.  
4. Generate your **API Key ID** and **Secret Key**.  
5. Add them to your environment variables or configuration file.  

Once connected, the same trading logic in `trader.py` will automatically place **real simulated trades** in your Alpaca paper account.

---

## 🧠 Technologies Used

- **Python 3.10+**
- **Alpaca Trade API**
- **Pandas / NumPy**
- **Logging / Time Libraries**

---

## 🏁 How to Run the Project

### Step 1 – Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2 – Activate environment
```bash
.\venv\Scripts\activate
```

### Step 3 – Run simulation (safe mode)
```bash
python diagnostic_show_buy_sell.py
```

### Step 4 – Run live bot (optional)
```bash
python trader.py
```

---

## 📈 Future Improvements

- Add **multi-stock trading** support  
- Integrate **advanced indicators** (RSI, MACD)  
- Implement **email or Telegram notifications**  
- Build a **dashboard UI** for visualization  

---

## 🧾 Credits

Developed by **Sohum Patil**  
NHITM (Thane): B.E in Computer Science and Design  
(2022 Project Submission)

---

### ❤️ Project Summary

> “An automated stock trading bot that analyzes live market data, simulates buy/sell actions using intelligent logic, and can integrate with Alpaca’s paper trading environment for real-time execution — demonstrating a complete trading automation workflow with real-world applications in finance, education, and data-driven decision making.”

---

### 📬 Feedback
💌 For suggestions or collaboration:  
**sohum7even@gmail.com**
