import sys
from collections import deque


def sell_coin( coin, price, quantity, inventory):
    fifo_profit_curr_trade = 0

    # Raise error if there is no coin to sell
    assert coin in inventory, f"No purchases found for {coin}. Cannot sell."

    # Calculate FIFO profit
    while quantity > 0:

        # Raise error if not enough coin to sell
        assert inventory[coin], f"Not enough purchases for {coin}. Cannot sell."

        # Get data for first purchase in the inventory
        row1 = inventory[coin][0]
        price_row1 = row1[0]
        quantity_row1 = row1[1]

        # Calculate FIFO profit for the quantity being sold
        if quantity >= quantity_row1:
            fifo_profit_curr_trade += (price - price_row1) * quantity_row1
            quantity -= quantity_row1
            inventory[coin].popleft()

        # If not enough quantity in the first purchase, update the quantity
        elif quantity < quantity_row1:
            fifo_profit_curr_trade += (price - price_row1) * quantity
            quantity_left = quantity_row1 - quantity
            quantity = 0
            row1[1] = quantity_left

    return inventory, fifo_profit_curr_trade


def calculate_fifo_profit(data):
    # Store inventory and fifo_profit 
    inventory = {}
    fifo_profit = 0

    for trans in data:
        # Skip empty lines
        if not trans.strip():
            continue
            
        # Split the line into four values
        values = trans.split()
        
        # Raise error if there are not four values 
        assert len(values) == 4, f"Expected 4 values, got {len(values)}"      
        transaction_type, coin, price, quantity = values  
        price = float(price)
        quantity = float(quantity)
        
        # Store buying data to calculate later
        if transaction_type == 'B':
            if coin not in inventory:
                inventory[coin] = deque()
            inventory[coin].append([price, quantity])
        
        # Selling data
        elif transaction_type == 'S':
            inventory, fifo_profit_curr_trade = sell_coin(coin, price, quantity, inventory)
            fifo_profit += fifo_profit_curr_trade  

    return fifo_profit


def get_data_from_file():
    # Get the file name from command line arguments
    if len(sys.argv) < 2:
        print("Please provide a file name")
        sys.exit()

    file_name = sys.argv[1]

    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read the contents of the file
        contents = file.read()

    # Prepare data from text file to list
    data = contents.split("\n")
    return data

                  
def main():
    data = get_data_from_file()

    # Calculate the FIFO profit
    fifo_profit = calculate_fifo_profit(data)

    # Print the FIFO profit
    print(f"FIFO Profit: {fifo_profit:.2f}")


if __name__ == '__main__':
    main()
        