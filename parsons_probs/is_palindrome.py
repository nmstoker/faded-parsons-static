def is_palindrome(text, remove_spaces = False):
    """is_palindrome returns True if input string is a palindrome whereby the
       string when reversed matches the string in normal order
       It is case-insensitive and optionally will remove spaces

    >>> is_palindrome('Abba')
    True
    >>> is_palindrome('Toot')
    True
    >>> is_palindrome('Backhand')
    False
    >>> is_palindrome('Roasted')
    False
    >>> is_palindrome('A man a plan a canal Panama')
    False
    >>> is_palindrome('A man a plan a canal Panama', True)
    True
    >>> is_palindrome('A man a plan a canal Panama', remove_spaces = True)
    True
    """