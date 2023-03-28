# Calculate-FIFO-Profit-Loss

This script is designed to calculate the FIFO (first-in, first-out) profit or loss for a given set of cryptocurrency transactions. The script reads a text file of transaction data, with each line of the file representing a single transaction.

## Usage
To use the script, simply run it with Python and provide the name of the input file as a command-line argument. For example:

```
python3 fifo.py crypto_tax.txt
```

## Input File Format
The input file should contain one transaction per line, with each transaction represented by four space-separated values:

* The transaction type ('B' for buy or 'S' for sell)
* The coin symbol (e.g. BTC, ETH, etc.)
* The price per coin at the time of the transaction
* The quantity of coins involved in the transaction

For example:

```
 B BTC 680000.0 2.5 
 B ETH 43000.0 12.0 
 B BTC 690000.0 2.5 
 S BTC 695000.0 3.0 
 B ETH 43500.0 23.5 
 S BTC 695000.0 1.0 
 S ETH 45000.0 30.0
```

## Output
The script calculates the FIFO profit/loss for the transactions and prints the result to the console in the following format:

```
FIFO Profit: 96000.00
```

## Notes
* The script assumes that the transactions in the input file are sorted chronologically, with the oldest transactions first.
* The script raises an error if there is an attempt to sell a coin that has not been purchased, or if there is not enough quantity of the coin to sell.