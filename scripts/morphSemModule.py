def get_num(entry):
    """
    Extract the 'num' field from the morph_info of the entry.
    Return 'p' if plural, otherwise return '-'.
    If 'dependency_relation' is 'main', return '-'.
    """
    if entry.get('dependency_relation') == 'main':
        return '-'  

    morph_info = entry.get('morph_info', {})
    num = morph_info.get('num', '-')
    return 'pl' if num == 'p' else '-'
