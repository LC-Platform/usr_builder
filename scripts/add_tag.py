from scripts.format import format_entry
from scripts.sentTypeModule import get_sentence_type
from scripts.originalSentModule import get_sentence_text
from scripts.hinWxConvertor import devanagari_to_wx
from constants.constantList import CXN_VALUE

def format_sentence(sentence_data, discourse_data):
    """Format the parser output for a single sentence."""
    result = []
    sentence_id = sentence_data['sentence_id']
    result.append(f"<sent_id={sentence_id}>")
    sentence_type = get_sentence_type(sentence_data)
    sentence_text = get_sentence_text(sentence_data)
    result.append(f'#{sentence_text}')

    parser_output = sentence_data['parser_output']
    sent_1_id = None
    # Find the relevant discourse entry for this sentence_id (if any)
    relevant_discourse = next(
        (discourse for discourse in discourse_data 
         if discourse['sent_2_id'] == sentence_id),
        None
    )

    # Check if discourse_marker exists in discourse data
    discourse_marker_match = relevant_discourse and relevant_discourse['discourse_marker'] != 'None'
    
    for i, entry in enumerate(parser_output):
        if relevant_discourse and entry.get('dependency_relation', '-') == 'main' and discourse_marker_match:
            dis_head = entry.get('index', '-')
            
        discourse_info = (
            f"{relevant_discourse['sent_1_id']}.{dis_head}:{devanagari_to_wx(relevant_discourse['discourse_relation'])}"
            if relevant_discourse and discourse_marker_match and entry.get('dependency_relation', '-') == 'main' and entry.get('cnx_component', '-') not in CXN_VALUE
            else '-'
        )

        # Pass discourse_info directly to format_entry
        formatted_entry = format_entry(entry, parser_output, i, discourse_info)
        if formatted_entry:
            result.append(formatted_entry)

    result.append(f"%{sentence_type}")
    result.append(f"</sent_id>")
    result.append("\n\n")  # Blank line for separation
    return '\n'.join(result)

