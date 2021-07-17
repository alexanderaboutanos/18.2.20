def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    return phrase.title()
    
    split_words = phrase.split(' ')
    rtn_str = ''
    for word in split_words:
        rtn_str += f"{word.capitalize()} "
    return rtn_str
    
    


