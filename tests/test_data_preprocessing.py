import unittest
from src.data_preprocessing import load_data, preprocess_data

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.df = load_data('../data/sample_logs.csv')
    
    def test_preprocess_data(self):
        processed_df = preprocess_data(self.df)
        self.assertIn('hour', processed_df.columns)
        self.assertIn('day_of_week', processed_df.columns)

if __name__ == '__main__':
    unittest.main()
