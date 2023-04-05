from typing import Union

from typing import Callable
from src.hashing import hash_family_str_to_4bytes

def get_shingles(document: str, k: int, compressed: bool = True) -> Union[set, None]:
    """Given an input string and the length of the shingles, the function produces
    the set of k-character shingles of the document.

    Args:
        document (str): The input string.
        k (int): The length of the shingles.
        compressed (bool): Indicator whether the shingles should be compressed using some hash function.

    Returns:
        Union[set, None]: The set of k-shingles for the given document.
    """
    # check if the document is valid
    if len(document) < k:
        print("Document is too short for shingle length k!")
        return None
    if k <= 0:
        print("Shingle length must be positive!")
        return None
    
    # get some hash function for compressing the shingles, we just use seed 0
    h: Callable[[str],int] = hash_family_str_to_4bytes(i=0)

    # produce the actual results
    shingle_set: set = set()
    for i in range((len(document)-k+1)):
        shingle: str = document[i:i+k]

        # add compressed or fully shingle to the result set
        if compressed:
            shingle_set.add(h(shingle))
        else:
            shingle_set.add(shingle)
    
    return shingle_set