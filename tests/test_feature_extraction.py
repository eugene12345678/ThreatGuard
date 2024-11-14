import unittest
from src.feature_extraction import extract_features
import pandas as pd

class TestFeatureExtraction(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('../data/processed_data.csv')

    def test_extract_features(self):
        features = extract_features(self.df)
        self.assertEqual(features.shape[1], 2)  # Should have two features

if __name__ == '__main__':
    unittest.main()
