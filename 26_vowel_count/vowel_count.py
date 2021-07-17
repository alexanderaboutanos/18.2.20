def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiouAEIOU'
    return_dict = {}
    for char in phrase:
        if vowels.count(char) != 0:
            return_dict[char.lower()] = phrase.count(char.upper()) + phrase.count(char.lower())
    return return_dict

    ##DONE