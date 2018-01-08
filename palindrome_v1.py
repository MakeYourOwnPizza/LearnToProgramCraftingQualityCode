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
    s.reverse()
    
# helper function
def reserve(s):
    '''(str) -> str
    >>> reserve('hello')
    'olleh'
    >>> reserve('a')
    'a'
    '''
