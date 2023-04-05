import unittest
import xxhash

from typing import Callable
from src.shingling import get_shingles
from src.min_hash import MinHash
from src.metrics import jaccard_similarity, signature_similarity

class TestMinHash(unittest.TestCase):
    """Tests for min-hashing.
    """

    def setUp(self) -> None:
        """Setup to be done before calling the test cases.
        """
        pass


    def test_minhash(self) -> None:
        """Test the minhash function.
        """
        test_strings: str = ['The quick brown fox jumps over the lazy dog', 'The quick brown cat jumps over the lazy dog']
        k: int = 5 # shingle length
        
        # shingling and minhashing
        minhash: MinHash = MinHash(K=5)
        signatures: list[list[int]] = []
        shingles: list[set[int]] = []

        for doc in test_strings:
            shingled_doc: set[int]= get_shingles(document=doc, k=k)
            shingles.append(shingled_doc)
            signatures.append(minhash.minhash(shingled_doc))

        # compare the Jaccard similarity of the sentences to the expected similarity of the signatures
        absolute_similarity: float = jaccard_similarity(shingles[0], shingles[1])
        print(f'Jaccard similarity of the sentences: {absolute_similarity}')

        N: int = 1000
        similarity_estimates: list[int] = []
        for i in range(N):
            minhash: MinHash = MinHash(K=10)
            minhash_0: list[int] = minhash.minhash(shingles[0])
            minhash_1: list[int] = minhash.minhash(shingles[1])
            similarity_estimates.append(signature_similarity(minhash_0, minhash_1))
        
        estimated_similarity: float = sum(similarity_estimates) / N
        print(f'Estimated similarity using signatures: {estimated_similarity}')

        self.assertAlmostEqual(estimated_similarity, absolute_similarity, places=2)

if __name__ == '__main__':
    unittest.main()