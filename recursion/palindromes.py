def isPalindrome(s):
    if len(s) <= 1:
        return True
    elif s[:1] != s[-1:]:
        return False
    return isPalindrome(s[1:-1])


st = isPalindrome("rotor")
assert st, "Should be True"
print("Rotor is a palindrome" if isPalindrome(
    "rotor") else "Rotor is not a palindrome")
