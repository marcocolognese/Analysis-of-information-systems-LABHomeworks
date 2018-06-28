import unittest
from irpef import irpef_calculation


class test_irpef(unittest.TestCase):

    def test_irpef_calculation(self):
        self.assertEqual(3720.0, irpef_calculation(16000))
        self.assertEqual(161.0, irpef_calculation(700))
        self.assertEqual(8100.0, irpef_calculation(31000))
        self.assertEqual(22960.0, irpef_calculation(69000))
        self.assertEqual(34020.0, irpef_calculation(95000))


if __name__ == '__main__':
    unittest.main()
