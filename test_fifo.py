import unittest
from subprocess import run, PIPE


class TestFIFO(unittest.TestCase):

    # Test FIFO profit/loss calculation
    def test_fifo_profit(self):
        file_contents = """B BTC 680000.0 2.5 
B ETH 43000.0 12.0 
B BTC 690000.0 2.5 
S BTC 695000.0 3.0 
B ETH 43500.0 23.5 
S BTC 695000.0 1.0 
S ETH 45000.0 30.0"""
        
        with open('test_crypto_tax.txt', 'w') as file:
            file.write(file_contents)
        
        expected_output = 'FIFO Profit: 96000.00\n'
        result = run(['python3', 'fifo.py', 'test_crypto_tax.txt'], stdout=PIPE, text=True)
        self.assertEqual(result.stdout, expected_output)

    # Test selling unpurchased coin
    def test_sell_unpurchased_coin(self):
        file_contents = """B BTC 10000 2
B ETH 2000 5
S XRP 5 10"""
        
        with open('test_crypto_tax.txt', 'w') as file:
            file.write(file_contents)
        
        expected_output = 'No purchases found for XRP. Cannot sell.'
        result = run(['python3', 'fifo.py', 'test_crypto_tax.txt'], stdout=PIPE, stderr=PIPE, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr.split("AssertionError:")[-1].strip(), expected_output)

    # Test selling more coin than purchased
    def test_sell_not_enough_purchased_coin(self):
        file_contents = """B BTC 10000 2
S BTC 20000 5"""
        
        with open('test_crypto_tax.txt', 'w') as file:
            file.write(file_contents)
        
        expected_output = 'Not enough purchases for BTC. Cannot sell.'
        result = run(['python3', 'fifo.py', 'test_crypto_tax.txt'], stdout=PIPE, stderr=PIPE, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr.split("AssertionError:")[-1].strip(), expected_output)

      
if __name__ == '__main__':
    unittest.main()
