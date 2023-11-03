#doing this thow the console

# from rearrange import rearrange_name
# rearrange_name("Lovelace, Ada")


# ejemplo de test unitario simple
from rearrange import rearrange_name
import unittest

class testRearrange(unittest.TestCase): #hacemos que herede de unittest.TestCase
    def test_basic(self):
        testcase = "Lovelace, Ada"
        excepted = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase),excepted) #assertEqual ambos argumentos son iguales

# vamos a probar los edge cases 
    def test_empty(self):
        testcase = ""
        excepted = ""
        self.assertEqual(rearrange_name(testcase),excepted)

# vamos a añadir test adicionales

    def test_double(self): #probamos con alguien con nombre conmpuesto
        testcase = "Hopper, Grace M."
        excepted = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase),excepted)

    def test_one_name(self):
        testcase = "Voltaire"
        excepted = "Voltaire"
        self.assertEqual(rearrange_name(testcase),excepted)

unittest.main() 