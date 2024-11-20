def popcount(x: int) -> int:
    """
    Examples:
    popcount(3)  = 2 (3  = 0b11)
    popcount(7)  = 3 (7  = 0b111)
    popcount(10) = 2 (10 = 0b1010)
    """
    return bin(x).count("1")
