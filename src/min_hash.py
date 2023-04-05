from random import randint

class MinHash:
    """Class that implements min-hashing.
    """

    def __init__(self, K: int, max_shingle_id: int = (2**32)-1, prime: int = 4294967311) -> None:
        """Constructor for initializing a min-hash instance.

        Args:
            K (int): The number of hash functions to use, i.e. the length of the signature.
            max_shingle_id (int): The maximum hash ID of the compressed shingles. Defaults to (2**32)-1 representing a 32-bit hash value.
            prime (int): The largest prime number above max_shingle_id to use for the permuting hash function(s). 
                A prime number will greatly reduce the number of collisions.
        """
        self.K: int = K
        self.max_shingle_id: int = max_shingle_id
        self.prime = prime

        # create K tuples of hash function parameters a,b used for generating permutations
        self.hashing_params: tuple = [ (randint(0, self.max_shingle_id), randint(0, self.max_shingle_id)) for i in range(self.K)]


    def minhash(self, shingles: set[int]) -> list[int]:
        """Compute a min-hash signature for the given vector.

        Args:
            shingles (set[int]): The set of compressed shingles of the given document.

        Returns:
            list[int]: A minhash signature vector for the given set of shingles.
        """
        # initialize a vector of length K to hold the min-hash values
        sig: list[int] = [float('inf') for i in range(self.K)]

        # for each shingles of the document
        for shingle in shingles:
            # then for each hash permutation hash function
            for hash_idx, params in enumerate(self.hashing_params):
                a, b = params

                # compute the value of the shingle id passed through the i-th permutation function
                out: int = (a * shingle + b) % self.prime

                # conditionally update the i-th value of the signature vector if the permutation yields a lower value
                if out < sig[hash_idx]:
                    sig[hash_idx] = out

        return sig