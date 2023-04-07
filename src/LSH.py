from random import randint
from typing import Callable

from src.hashing import hash_str_to_4bytes

class LSH:
    """A class that to implement locality-sensitive hashing for documents.
    """

    def __init__(self, h: int, r: int, b: int) -> None:
        """Constructor for the LSH class.

        Args:
            h (int): The length of the (input) minhash signatures.
            r (int): The number of rows per band (such that rb=h).
            b (int): The number of bands (such that rb=h).
        """
        if r*b != h:
            raise Exception('Number of bands and rows does not fulfill rb=h!')
        self.h: int = h
        self.r: int = r
        self.b: int = b

        # create a dictionary containing one dictionary for each band which, subsequently, contains a set for each bucket
        self.hashes: dict[dict[set[int]]] = {}
        for i in range(b):
            self.hashes[i] = {}

        # initialize a family of hash functions, one for each band
        self.hash_functions: dict[Callable[[str],int]] = {}
        for i in range(b):
            seed: int = randint(0, (2**32) -1 ) # choose a random seed for the hash function
            self.hash_functions[i] = hash_str_to_4bytes(i=seed)


    def insert(self, id: int, signature: list[int]) -> None:
        """Insert a document into the LSH datastructure.

        Args:
            id (int): The id of the document.
            signature (list[int]): The minhash signature of the document.
        """
        # iterate through each band
        for i in range(self.b):
            # get the rows of the respective band
            band: list[int] = signature[self.r*i:self.r*(i+1)]
            
            # compute the hash value of the band
            hash_val: int = self.hash_functions[i](str(band))
            
            # insert the document id into the respective bucket
            if hash_val in self.hashes[i].keys():
                self.hashes[i][hash_val].add(id)
            else:
                self.hashes[i][hash_val] = set([id])


    def query(self, signature: list[int]) -> set[int]:
        """Takes a document signature and returns the set of stored candidate documents.

        Args:
            signature (list[int]): The minhash signature of the document

        Returns:
            set[int]: The set of candidate document ids.
        """
        candidates: set[int] = set()
        
        # iterate through each band
        for i in range(self.b):
            band: list[int] = signature[self.r*i:self.r*(i+1)]
            
            # compute the hash value of the band
            hash_val: int = self.hash_functions[i](str(band))

            # get candidate documents
            if hash_val in self.hashes[i].keys():
                candidates = candidates.union(self.hashes[i][hash_val])

        return candidates