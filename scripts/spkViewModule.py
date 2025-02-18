from constants.constantList import RANJAK_LIST

def get_spk_view_info(entry, parser_output, index):
    morph_info = entry.get('morph_info', {})
    root = morph_info.get('root', '-')
    wx_word = entry.get('wx_word', '-')
    pos_tag = entry.get('pos_tag', '-')

    if pos_tag == 'VM' and index + 1 < len(parser_output):
        next_entry = parser_output[index]
        next_morph_info = next_entry.get('morph_info', {})
        next_root = next_morph_info.get('root', '-')

        if wx_word == root and next_root in RANJAK_LIST:
            return f'[shade:{next_root}_1]'

    
    if root == 'yaha':
        return 'proximal'
    if root == 'vaha':
        return 'distal'
    return '-'



