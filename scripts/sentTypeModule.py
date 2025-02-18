def get_sentence_type(sentence_data):
    """Determine the sentence type based on the presence of 'nahIM' in wx_word."""
    for entry in sentence_data['parser_output']:
        if 'nahIM' in entry.get('wx_word', ''):
            return 'negative'  # If "nahIM" is found, sentence type is negative
        if '?' in entry.get('original_word', ''):
            return 'interrogative'
        if '!' in entry.get('original_word', ''):
            return 'imperative'
    return 'affirmative'  # Otherwise, sentence type is affirmative
