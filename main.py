import unittest
from app import app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_dg0(self):
        resp = self.app.post('/answer', data={'coef_a': 1, 'coef_b': -5, 'coef_c': 6})
        assert b'x_1 = 3.0' in resp.data
        assert b'x_2 = 2.0' in resp.data

    def test_de0(self):
        resp = self.app.post('/answer', data={'coef_a': 1, 'coef_b': -4, 'coef_c': 4})
        assert b'x = 2.0' in resp.data

    def test_dl0(self):
        resp = self.app.post('/answer', data={'coef_a': 1, 'coef_b': -5, 'coef_c': 7})
        assert b'$-3.0$' in resp.data

if __name__ == "__main__":
    unittest.main()