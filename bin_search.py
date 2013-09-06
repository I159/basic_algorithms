def binary_search(seq, x, lo=0, hi=None):
    """Binary search on Python. Recursive approach"""
    # Highest search point
    hi = hi or len(seq)
    # Middle search point
    mid = (lo+hi)//2

    # Appoint a current value
    try:
        val = seq[mid]
    except IndexError:
        return False
        
    # Check whether the current value is match to the desired value
    # If we found the x we return it
    if x == val:
        return mid
    # Otherwise, if the current value greater than desired value, appoint lowest to middle point
    lo = mid+1 if val < x else lo
    # Highest appoint to the value if the current value greater than desired value
    hi = mid if val > x else hi
    # And repeat with shifted data
    return binary_search(seq, x, lo, hi)
