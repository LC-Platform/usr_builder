from constants.constantList import NE_TAG, CALENDARIC_UNITS, DOW_UNITS, MEAS_UNITS

def get_original_word_info(entry, parser_output, index):
    """Check for 'per', 'loc', 'org' in the original_word and include them in the third column if present."""
    original_word = entry.get('original_word', '')
    wx_word = entry.get('wx_word', '')
    pos_tag = entry.get('pos_tag', '')
    morph_info = entry.get('morph_info', {})
    gender = morph_info.get('gen', '-')
    gen = '-'

    if wx_word.isdigit() and index + 1 < len(parser_output):
        next_entry = parser_output[index]
        next_word = next_entry.get('wx_word', '')
        
        if next_word in CALENDARIC_UNITS:
            return 'dom'
        elif next_word in MEAS_UNITS:
            return 'meas'
        elif next_word == 'baje':
            return 'clocktime'
        else: 
            return 'numex'

    if (wx_word.isdigit() or pos_tag == 'QC') and index + 1 < len(parser_output):
        next_entry = parser_output[index]
        next_word = next_entry.get('wx_word', '')

        if next_word == 'baje':
            return 'clocktime'
        elif next_word == 'saxi':
            return 'era'

    if pos_tag in ('NNP', 'NNPC'):
        if gender == 'm':
            gen = 'male'
        if gender == 'f':
            gen = 'female'
        return gen
    
    if wx_word in CALENDARIC_UNITS:
        return 'moy'
    
    if wx_word in DOW_UNITS:
        return 'dow'

    matches = []
    for tag in NE_TAG:
        if tag in original_word:
            if tag == 'loc':
                matches.append('place')
            else:
                matches.append(tag)
    return ','.join(matches) if matches else '-'  # Join matches with commas or return '-'
