s = input()


def palindrome(s1: str) -> bool:
    n = len(s1)
    for i in range(n // 2):
        if s1[i] != s1[-(i + 1)]:
            return False
    return True


half = len(s) // 2
if palindrome(s):
    if palindrome(s[:half]):
        if palindrome(s[half + 1:]):
            print('Yes')
            exit()
print('No')
