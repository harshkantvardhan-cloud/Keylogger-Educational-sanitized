import io
import sys
import unittest

from safe_demo import print_simulated_events, get_simulated_events


class TestPrintOutput(unittest.TestCase):
    def test_print_simulated_events_outputs_lines(self):
        captured = io.StringIO()
        old = sys.stdout
        try:
            sys.stdout = captured
            events = print_simulated_events()
        finally:
            sys.stdout = old

        output = captured.getvalue().strip().splitlines()
        # There should be one printed line per event
        self.assertEqual(len(output), len(events))
        # Each output line should contain the word 'Simulated event:'
        for line in output:
            self.assertIn('Simulated event:', line)


if __name__ == '__main__':
    unittest.main()
