from random import randint

def fermat_test(n: int, k: int) -> bool:
    assert n > 0
    if n <= 3:
        return True
    while k > 0:
        a = randint(2, n-2)
        if pow(a, n-1, n) != 1:
            return False
        k -= 1
    return True

if __name__ == "__main__":
    test_cases = [
        ([2, 4], True),
        ([3, 4], True),
        ([5, 5], True),
        ([7, 10], True),
        ([4, 4], False),
        ([6, 4], False),
        ([9, 5], False),
        ([10, 7], False),
        ([101, 10], True),
        ([103, 10], True),
        ([100, 10], False),
        ([104, 8], False),
        ([111, 15], False),
        ([1, 5], True),
        ([999983, 50], True),
        ([999984, 50], False),
    ]
    for input, expected in test_cases:
        n, k = input
        assert fermat_test(n, k) == expected, f"Error: {n} is prime ? Expected {expected}"