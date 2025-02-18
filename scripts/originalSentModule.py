def get_sentence_text(sentence_data):
    """Extract the original sentence from the JSON data."""
    return sentence_data.get('sentence', '-')  # Default to '-' if 'sentence' key is missing
