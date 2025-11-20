import unittest
from safe_demo import get_simulated_events, print_simulated_events


class TestSafeDemo(unittest.TestCase):
    def test_get_simulated_events(self):
        events = get_simulated_events()
        self.assertIsInstance(events, list)
        self.assertGreaterEqual(len(events), 1)
        self.assertIn("[esc]", events)

    def test_print_simulated_events_returns_list(self):
        events = print_simulated_events()
        self.assertEqual(events, get_simulated_events())


if __name__ == "__main__":
    unittest.main()
