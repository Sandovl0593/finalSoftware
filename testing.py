from app.models import *
import unittest

class Testing(unittest.TestCase):

    def __init__(self):
        self.gen_stubs()

    def test_returns_dictionary_with_keys(self):
        cuenta = Cuenta(Usuario("John Doe", "123456789"), 100, [])
        result = cuenta.historial()
        self.assertIsInstance(result, dict)
        self.assertIn("saldo", result)
        self.assertIn("owner", result)
        self.assertIn("operaciones", result)