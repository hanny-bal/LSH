import unittest
import xxhash

from typing import Callable
from src.shingling import get_shingles
from src.hashing import hash_family_str_to_4bytes

class TestShingling(unittest.TestCase):
    """Tests for shingling.
    """

    def setUp(self) -> None:
        """Setup to be done before calling the test cases.
        """
        pass


    def test_shingling(self) -> None:
        """Test the shingling function without hashing.
        """
        test_str: str = 'The quick brown fox jumps over the lazy dog'
        k: int = 10
        actual_shingles: set = {'The quick ', 'he quick b', 'e quick br', ' quick bro', 'quick brow', 'uick brown', 'ick brown ',
                              'ck brown f', 'k brown fo', ' brown fox', 'brown fox ', 'rown fox j', 'own fox ju', 'wn fox jum', 
                              'n fox jump', ' fox jumps', 'fox jumps ', 'ox jumps o', 'x jumps ov', ' jumps ove', 'jumps over', 
                              'umps over ', 'mps over t', 'ps over th', 's over the', 's over the', ' over the ', 'over the l', 
                              'ver the la', 'er the laz', 'r the lazy', ' the lazy ', 'the lazy d', 'he lazy do', 'e lazy dog'}
        
        # produce some shingles
        computed_shingles: set = get_shingles(document=test_str, k=k, compressed=False)
        
        # test if the computed shingles are equivalent to the actual shingles
        self.assertEqual(actual_shingles, computed_shingles)


    def test_hashing(self) -> None:
        """Test hashing a string to 4 bytes. 
        """
        seed: int = 4
        h: Callable[[str], int] = hash_family_str_to_4bytes(i=seed)
        
        # test if identical strings hash to the same value and different ones don't
        self.assertNotEqual(h('hello'), h('world'))
        self.assertEqual(h('hello'), h('hello'))
        self.assertEqual(h('hello'), xxhash.xxh32('hello', seed=seed).intdigest())


    def test_compressed_shingling(self) -> None:
        """Test the shingling function with hashing each shingle to four bytes.
        """
        test_str: str = 'The quick brown fox jumps over the lazy dog'
        k: int = 10
        actual_shingles: set = {'The quick ', 'he quick b', 'e quick br', ' quick bro', 'quick brow', 'uick brown', 'ick brown ',
                              'ck brown f', 'k brown fo', ' brown fox', 'brown fox ', 'rown fox j', 'own fox ju', 'wn fox jum', 
                              'n fox jump', ' fox jumps', 'fox jumps ', 'ox jumps o', 'x jumps ov', ' jumps ove', 'jumps over', 
                              'umps over ', 'mps over t', 'ps over th', 's over the', 's over the', ' over the ', 'over the l', 
                              'ver the la', 'er the laz', 'r the lazy', ' the lazy ', 'the lazy d', 'he lazy do', 'e lazy dog'}
        
        # compress the actual shingles using some hash function
        actual_shingles_compressed = set()
        for shingle in actual_shingles:
            actual_shingles_compressed.add(xxhash.xxh32(shingle, seed=0).intdigest())
        
        # produce some shingles
        computed_shingles: set = get_shingles(document=test_str, k=k, compressed=True)
        
        # test if the computed shingles are equivalent to the actual shingles
        self.assertEqual(actual_shingles_compressed, computed_shingles)



if __name__ == '__main__':
    unittest.main()