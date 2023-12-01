from app.models import *
import unittest

class Testing(unittest.TestCase):

    def __init__(self):
        self.gen_stubs()

    def test_historial(self):
        cuenta = Cuenta(Usuario("John Doe", "123456789"), 100, [])
        result = cuenta.historial()
        self.assertIsInstance(result, dict)
        self.assertIn("saldo", result)
        self.assertIn("owner", result)
        self.assertIn("operaciones", result)

    def test_valid_contact_sufficient_balance(self):
        cuenta = Cuenta(Usuario("John", "1234567890"), 100, [Cuenta(Usuario("Jane", "0987654321"), 0, [])])
        result = cuenta.pagar("0987654321", 50)
        self.assertEqual(result, "Realizado en 17/03/2023")


    def test_nonexistent_contact(self):
        cuenta = Cuenta(Usuario("John", "1234567890"), 100, [Cuenta(Usuario("Jane", "0987654321"), 0, [])])
        result = cuenta.pagar("9876543210", 50)
        self.assertEqual(result, "El destinatario no existe")

    def test_telefono_inexist(self):
        cuenta = Cuenta(Usuario("John", "123456789"), 100, [Contacto(Usuario("Jane", "987654321"))])
        result = cuenta.find_contactocuenta_telefono(None)
        self.assertFalse(result)