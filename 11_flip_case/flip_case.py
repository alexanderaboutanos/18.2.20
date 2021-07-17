def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newstr = ''
    for char in phrase:
        if char.upper() == to_swap.upper():
            newstr += char.swapcase()
        else: newstr += char
    return newstr

    ## Done!
