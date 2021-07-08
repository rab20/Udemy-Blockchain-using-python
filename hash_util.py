import hashlib as hl
import json


def hash_srting_256(string):
    return hl.sha256(string).hexdigest()

def hash_block(block):
    """Hashes a block and returns a string representation of it.

    Arguments:
        :block: The block that should be hashed.
    """
    # sort_keys = True as we are converting a dictionary to string here. But dictionaries are not ordered and hence even for the exact
    # same dictionary, a different string can be created if the order gets changed for some reason.
    return hash_srting_256(json.dumps(block, sort_keys=True).encode())