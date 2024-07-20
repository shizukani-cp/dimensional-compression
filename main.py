def dimensional_compression(x: int, y: int) -> int:
    n = x + y - 1
    return (((n + 1) * n) // 2) - (y - 1)
