import unittest
import grp1_ASP_Project as prog


class testMyProgram(unittest.TestCase):
    def test_topTotals(self):
        self.assertEqual(5934194, prog.findCountries.top3_total)

    def test_topMean(self):
        self.assertEqual(1978066, prog.findCountries.top3_mean)


if __name__ == '__main__':
    unittest.main()
