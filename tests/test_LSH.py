import unittest

from src.shingling import get_shingles
from src.min_hash import MinHash
from src.LSH import LSH

class TestMinHash(unittest.TestCase):
    """Tests for the LSH class.
    """

    def setUp(self) -> None:
        """Setup to be done before calling the test cases.
        """
        pass


    def test_init(self) -> None:
        """Test the initialization of the LSH class.
        """
        # check if a wrong number of rows and bands raises an exception
        self.assertRaises(Exception, LSH, 100, 5, 6)
        
        # check initialization and length of the empty dictionary
        lsh: LSH = LSH(h=100, r=5, b=20)
        self.assertEqual(len(lsh.hashes), 20)
        
    def test_insert(self) -> None:
        pass

    def test_insert(self) -> None:
        """Test an insertion of an element into the LSH data structure.
        """
        lsh: LSH = LSH(h=10, r=2, b=5)

        # choose two artificial signatures to insert
        sig1: list[int] = [1,2,3,4,5,6,7,8,9,10]
        sig2: list[int] = [1,2,9,8,7,5,6,3,4,11]
        lsh.insert(1, sig1)
        lsh.insert(2, sig2)

        # the first band should now only contain one bucket with the two document ids
        for key in lsh.hashes[0].keys():
            self.assertIn(1, lsh.hashes[0][key])
            self.assertIn(2, lsh.hashes[0][key])

    def test_query(self) -> None:
        """Test a query using the LSH data structure.
        """
        lsh: LSH = LSH(h=10, r=2, b=5)

        # choose two artificial signatures to insert
        sig1: list[int] = [1,2,3,4,5,6,7,8,9,10]
        sig2: list[int] = [13,100,9,8,7,5,6,3,4,11]
        lsh.insert(1, sig1)
        lsh.insert(2, sig2)

        # the first band should now only contain one bucket with the two document ids
        q: list[int] = [1,2,95,13,51,132,51,15,99,14]
        candidates: set[int] = lsh.query(q)
        
        # document 1 should be a candidate
        self.assertIn(1,candidates)


if __name__ == '__main__':
    unittest.main()