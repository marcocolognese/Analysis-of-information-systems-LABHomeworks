import unittest
from codiceFiscale import estrai_nome, estrai_cognome, genera_mese, codice_comune, genera_giorno, genera_codice_controllo

class test_codiceFiscale(unittest.TestCase):

	def test_estrai_nome(self):
		self.assertEqual("gfr", estrai_nome("gianfranco"))
		self.assertEqual("lax", estrai_nome("al"))
        
	def test_estrai_cognome(self):
		self.assertEqual("drs", estrai_cognome("derossi"))
		self.assertEqual("fox", estrai_cognome("fo"))

	def test_genera_mese(self):
		self.assertEqual("d", genera_mese("4"))

	def test_codice_comune(self):
		self.assertEqual("e512", codice_comune("legnago"))
        
	def test_genera_giorno(self):
		self.assertEqual("16", genera_giorno("16", "m"))
		self.assertEqual("52", genera_giorno("12", "f"))

	def test_genera_codice_controllo(self):
		self.assertEqual("k", genera_codice_controllo("rssmra80a01l781"))


if __name__ == '__main__':
	unittest.main()
