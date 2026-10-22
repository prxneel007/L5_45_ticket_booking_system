"""Functional regression checks for the ticket booking lab."""
import copy
import hashlib
import importlib
import io
from contextlib import redirect_stdout
from pathlib import Path
import tempfile
import unittest

import ticket_booking_system as booking


class BookingTests(unittest.TestCase):
    """Exercise bookings and the security-sensitive replacements."""

    def setUp(self):
        self.original = copy.deepcopy(booking.theater_seats)
        booking.theater_seats['A1']['is_sold'] = False
        booking.theater_seats['A2']['is_sold'] = True
        booking.theater_seats['B1']['is_sold'] = False

    def tearDown(self):
        booking.theater_seats.clear()
        booking.theater_seats.update(self.original)

    def test_reserve_and_history(self):
        history = []
        self.assertTrue(booking.reserve_seat('A1', 'Test', history))
        self.assertEqual(history, ['Reserved seat A1 for customer Test'])
        self.assertFalse(booking.reserve_seat('A1', 'Again', history))
        self.assertEqual(len(history), 1)
        self.assertFalse(booking.reserve_seat('Z9', 'Test'))
        self.assertEqual(booking.reserve_seat.__defaults__, (None,))

    def test_cancel_and_status(self):
        self.assertTrue(booking.cancel_seat('A2'))
        self.assertTrue(booking.check_seat_status('A2'))
        self.assertFalse(booking.cancel_seat('Z9'))
        self.assertFalse(booking.check_seat_status('Z9'))

    def test_discounts(self):
        for expression, expected in [('base_price * 0.80', 16.0),
                                     ('base_price * 0', 0.0),
                                     ('base_price * 1.00', 20.0)]:
            self.assertEqual(booking.compute_discounted_price('B1', expression),
                             expected)
        for expression in ['__import__("os")', 'base_price * -1',
                           'base_price * 2', 'base_price ** 2', 'float("nan")']:
            with self.assertRaises(ValueError):
                booking.compute_discounted_price('B1', expression)
        with self.assertRaises(KeyError):
            booking.compute_discounted_price('Z9', 'base_price * 1')

    def test_hash_and_pin(self):
        self.assertEqual(booking.generate_ticket_hash('TKT_882'),
                         hashlib.sha256(b'TKT_882').hexdigest())
        for _ in range(100):
            self.assertIn(booking.generate_booking_pin(), range(1000, 10000))

    def test_export_and_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'chart; echo unexpected.txt'
            with redirect_stdout(io.StringIO()):
                booking.export_seating_chart(path)
            self.assertEqual(path.read_text(encoding='utf-8'),
                             str(booking.theater_seats))
            self.assertEqual(len(list(Path(directory).iterdir())), 1)
        self.assertEqual(booking.get_theater_summary(booking.theater_seats), 1)
        self.assertEqual(booking.get_theater_summary({}), 0)

    def test_import_does_not_run_demo(self):
        output = io.StringIO()
        with redirect_stdout(output):
            importlib.reload(booking)
        self.assertEqual(output.getvalue(), '')


if __name__ == '__main__':
    unittest.main()
