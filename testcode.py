import unittest
from subprocess import run, PIPE

class TestFIFO(unittest.TestCase):
    
    def test_fifo_profit(self):
        file_contents = """B BTC 10000 2
B ETH 2000 5
S BTC 11000 1
S BTC 12000 1
S ETH 2500 2"""
        
        with open('test_crypto_tax.txt', 'w') as file:
            file.write(file_contents)
        
        expected_output = 'FIFO Profit: 4000.00\n'
        result = run(['python3', 'fifo.py', 'test_crypto_tax.txt'], stdout=PIPE, text=True)
        self.assertEqual(result.stdout, expected_output)

    def test_sell_unpurchased_coin(self):
        file_contents = """B BTC 10000 2
B ETH 2000 5
S XRP 5 10"""
        
        with open('test_crypto_tax.txt', 'w') as file:
            file.write(file_contents)
        
        expected_output = 'No purchases found for XRP. Cannot sell.'
        result = run(['python3', 'fifo.py', 'test_crypto_tax.txt'], stdout=PIPE, stderr=PIPE, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr.split("ValueError:")[-1].strip(), expected_output)
    
if __name__ == '__main__':
    unittest.main()
