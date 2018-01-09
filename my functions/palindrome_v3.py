def is_palindrome_v3(s):
    '''(str) -> bool

    Return True and only if s is a palindrome.
    
    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>>is_palindrome_v3('dented')
    False
    '''
    i = 0
    j = len(s) - 1
    
    # The characters in s[:i] have been successfully compared to those in s[j:].
    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    # If we exited because we successfully compared all pairs of characters,
    # then j <= i.
    return j <= i
