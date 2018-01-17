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

# not execute this code when we run this module, not when importing it.

if __name__ == '__main__':
    print('In version 1, the module name is', __name__)

    word = input('Enter a word: ')
    if is_palindrome_v1(word):
        print(word, 'is a palindrome.')
    else:
        print(word, 'is not a palindrome.')
