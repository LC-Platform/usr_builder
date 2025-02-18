def get_rp_word(parser_output):
    """Extract the RP word based on the head index."""
    rp_head_index = None
    rp_word = None

    for entry in parser_output:
        pos_tag = entry.get('pos_tag', '-')
        if pos_tag == "RP":
            rp_head_index = entry.get('head_index', '-')
            rp_word = entry.get('wx_word', '-')
            break  # Assuming only one RP word per sentence

    if rp_head_index and rp_head_index != '-':
        try:
            rp_head_index_int = int(rp_head_index)
            for entry in parser_output:
                entry_index = entry.get('index', '-')
                if entry_index != '-' and int(entry_index) == rp_head_index_int:
                    return rp_word
        except ValueError:
            pass

    return None
