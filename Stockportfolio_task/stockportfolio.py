# ---------------------------------------
# Stock Portfolio Tracker (Auto Save)
# ---------------------------------------

# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

portfolio = {}

print("📊 Welcome to Stock Portfolio Tracker\n")
print("Available Stocks & Prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
print(38*"-")

# Step 1: User Input
while True:
    stock_name = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not found! Choose from the list.")
        continue

    qty = int(input(f"Enter quantity for {stock_name}: "))
    portfolio[stock_name] = portfolio.get(stock_name, 0) + qty

# Step 2: Calculate Total Investment
print("\n--- Your Portfolio Summary ---")
total_value = 0

summary_lines = []  # For saving into file

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    line = f"{stock} → Qty: {qty} | Price: ${price} | Value: ${value}"
    summary_lines.append(line)
    print(line)

print(38*"-")
print(f"💰 Total Investment Value = ${total_value}")

# Step 3: Auto Save to Text File
with open("portfolio_result.txt", "w",encoding="utf-8") as f:
    f.write("Stock Portfolio Summary\n")
    f.write("------------------------\n")
    for line in summary_lines:
        f.write(line + "\n")
    f.write(f"\nTotal Investment: ${total_value}\n")


