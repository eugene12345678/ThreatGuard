import unittest
from src.real_time_monitor import fetch_new_logs

class TestRealTimeMonitor(unittest.TestCase):
    def test_fetch_new_logs(self):
        logs = fetch_new_logs()
        self.assertGreater(len(logs), 0)  # Check if logs are fetched

if __name__ == '__main__':
    unittest.main()
