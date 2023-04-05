def jaccard_similarity(A: set, B: set) -> float:
    """Compute the Jaccard similarity between two sets.

    Args:
        A (set): Set A.
        B (set): Set B.

    Returns:
        float: The Jaccard similarity, is in [0,1].
    """
    return len(A.intersection(B)) / len(A.union(B))

def signature_similarity(s1: list[int], s2: list[int]) -> float:
    """Compute the similarity between two signature vectors.

    Args:
        s1 (list[int]): Signature vector 1.
        s2 (list[int]): Signature vector 2.

    Returns:
        float: The similarity of the two signature vectors, i.e. the estimated similarity between the two underlying documents.
    """
    if len(s1) != len(s2):
        print('Signature vectors need to have equal length!')
        return 0
    
    else:
        equal_entries: int = 0

        # go through each vector entry and compare
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                equal_entries += 1
        
        # compute final similarity
        return equal_entries / len(s1)