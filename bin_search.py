def binary_search(seq, x, lo=0, hi=None):
    # Highest search point
    hi = hi or len(seq)
    # Middle search point
    mid = (lo+hi)//2

    # Try is it correctly given the points
    try:
        val = seq[mid]
    except IndexError:
        return False

    # If we have got found the x we return it
    if x == val:
        return mid
    # Otherwise appoint lowest to middle point, if current value bigger than searched value
    lo = mid+1 if val < x else lo
    # Highest appoint to valuew if current valuew bigger than searched value
    hi = mid if val > x else hi
    # And repeat with shifted data
    return binary_search(seq, x, lo, hi)
