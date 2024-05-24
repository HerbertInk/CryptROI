# ROI calculator script
# Takes in an instruments variables and
# provides a ROI and Profit_loss/Loss for the invested amount on execution

# Function to write print contents to file
def write_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)

while True:
    try:
        # cryptocurrency
        cryptocurrency = input("Cryptocurrency: ")

        # Check if cryptocurrency input is not empty 'contains at least one character'
        if not cryptocurrency: # or not any(char.isalpha() for char in cryptocurrency):
            print("Cryptocurrency is required")
            continue  # Allow user retry

        current_price = float(input("Current price: "))
        target_price = float(input("Target price: "))
        investment_amount = float(input("Investment amount: "))

        # ROI calculator
        percentage_change = ((target_price - current_price) / current_price) * 100
        coins_tokens_available = investment_amount / current_price

        unrealized_bal = target_price * coins_tokens_available
        roi = ((unrealized_bal - investment_amount) / investment_amount) * 100

        profit_loss = (roi * investment_amount) / 100

        # Prints
        print("\n-----CURRENCY--COMMODITY--BAL--ROI--P/L-----")
        print(f"Cryptocurrency: {cryptocurrency}")
        print(f"Price change in %: Open {current_price} Close {target_price} ({percentage_change:.2f}%)")
        print(f"{cryptocurrency} balance: {coins_tokens_available:.8f}")
        print(f"Investment Amount: ${investment_amount:.2f}")
        print("----------------------------------------------")
        print(f"Unrealized Balance: {unrealized_bal:.2f}")
        print(f"ROI: {roi:.2f}%")
        print(f"P/L: ${profit_loss:.2f}")
        print("----------------------------------------------")
        print("--Risk disclosure: Not financial advice--")
        print("----------------------------------------------")

        # Results as a string
        result_str = f"\n-----CURRENCY--COMMODITY--BAL--ROI--P/L-----\n" \
                     f"Cryptocurrency: {cryptocurrency}\n" \
                     f"Price change in %: Open {current_price} Close {target_price} ({percentage_change:.2f}%)\n" \
                     f"{cryptocurrency} balance: {coins_tokens_available:.8f}\n" \
                     f"Investment Amount: ${investment_amount:.2f}\n" \
                     f"----------------------------------------------\n" \
                     f"Unrealized Balance: ${unrealized_bal:.2f}\n" \
                     f"ROI: {roi:.2f}%\n" \
                     f"P/L: ${profit_loss:.2f}\n" \
                     f"----------------------------------------------\n" \
                     f"--Risk disclosure: Not financial advice--\n"

        # Write results to a file
        file_path = "roi_results.txt"  # Adjust the file path as needed
        write_to_file(file_path, result_str)

        print("Results saved to 'roi_results.txt'.")
        break # Exit on successful execution

    except ValueError:
        print("Please enter valid numeric values")
        continue # Allow user retry

# ROI is Return On Investment
# P/L is Profit/Loss