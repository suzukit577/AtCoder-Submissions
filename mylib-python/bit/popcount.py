def popcount(x: int) -> int:
    """
    Examples:
    popcount(3)  == 2 (3  = 0b11)
    popcount(7)  == 3 (7  = 0b111)
    popcount(10) == 2 (10 = 0b1010)
    """
    return bin(x).count("1")


if __name__ == "__main__":
    print(f"popcount(3) == 2 equals to {popcount(3) == 2} (3 = {bin(3)})")
    print(f"popcount(7) == 2 equals to {popcount(7) == 3} (7 = {bin(7)})")
    print(f"popcount(10) == 2 equals to {popcount(10) == 2} (10 = {bin(10)})")
