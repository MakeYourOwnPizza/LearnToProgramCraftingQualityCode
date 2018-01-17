import palindrome_v1

def is_palindrome_v2(s):
    '''(str) -> bool

    Return True and only if s is a palindrome.
    
    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>>is_palindrome_v2('dented')
    False
    '''
    # The number of chars in s.
    n = len(s)
    # Compare the first half of s to the reverse of the second half.
    # Omit the middle character of an odd-length string.
    return s[:n//2] == palindrome_v1.reverse(s[n - n//2:])
    
# helper function
def reverse(s):
    '''(str) -> str
    >>> reserve('hello')
    'olleh'
    >>> reserve('a')
    'a'
    '''

    rev = ''

    # For each character is s, add that char to the beginning of rev.
    for ch in s:
        rev = ch + rev

    return rev

print('In version 2, the module name is', __name__)
