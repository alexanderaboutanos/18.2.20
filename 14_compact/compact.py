def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    return [element for element in lst if element]

    lst_copy = []
    for element in lst:
        if bool(element) == True:
            lst_copy.append(element)
    return lst_copy

    ##DONE

    