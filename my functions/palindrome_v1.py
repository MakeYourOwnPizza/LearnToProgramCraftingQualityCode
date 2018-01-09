def is_palindrome_v1(s):
    '''(str) -> bool

    Return True and only if s is a palindrome.
    
    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>>is_palindrome_v1('dented')
    False
    '''
    return reverse(s) == s
    
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
