import unittest
import finlogic as fl
from finlogic import fduckdb as fdb


class TestDatabase(unittest.TestCase):
    def test_info(self):
        """Test the info method of the Database module."""
        db_info = fdb.get_info()
        self.assertEqual(db_info["first_report"], "2009-01-31")
        self.assertTrue(db_info["number_of_rows"] > 2_000_000)

    def test_search_company(self):
        """Test the search_company method of the Database module."""
        search_result = fl.search_company("petrobras")
        """
            name_id                            cvm_id  tax_id
        0   PETROBRAS DISTRIBUIDORA S/A         24295  34.274.233/0001-02
        1   PETROLEO BRASILEIRO S.A. PETROBRAS   9512  33.000.167/0001-01
        """
        # Check the results
        self.assertEqual(set(search_result["cvm_id"]), {9512, 24295})


if __name__ == "__main__":
    unittest.main()
