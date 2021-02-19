import unittest
import ASP_Project as prog

class testMyProgram(unittest.TestCase):
    def test_topTotals(self):
        self.assertEqual(prog.findCountries.top3_total, 5934194)

    def test_grandMean(self):
        self.assertEqual(prog.findCountries.grand_mean, 78875)


if __name__ == '__main__':
    unittest.main()