import xxhash
from typing import Callable

def hash_str_to_4bytes(i: int) -> Callable[[str],int]:
    """Instanciate a hash function that hashes a string to 4 bytes using seed i.

    Args:
        i (int): The seed of the hash family.
    """
    def hash_func(x: str) :
        return xxhash.xxh32(x, seed=i).intdigest()
    return hash_func