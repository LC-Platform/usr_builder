# # import sys, os
# # sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
# from scripts.file_utils import load_json, save_output
# from scripts.add_tag import format_sentence

# def format_parser_output(file_path, discourse_path, output_file):
#     """Main function to format parser output from a JSON file."""
#     data = load_json(file_path)
#     discourse_data = load_json(discourse_path)

#     results = []
#     for sentence_data in data['response']:
#         results.append(format_sentence(sentence_data, discourse_data, all_sentence_data))

#     formatted_output = '\n'.join(results)
#     save_output(output_file, formatted_output)

# if __name__ == "__main__":
#     # File path to the JSON input
#     file_path = "IO/updated_parser_output.json"
#     output_file = "IO/usr_output.txt"
#     discourse_path = "IO/discourse_output.txt"

#     # Call the function to format and save the output
#     format_parser_output(file_path, discourse_path, output_file)



# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from scripts.file_utils import load_json, save_output
from scripts.add_tag import format_sentence

def format_parser_output(file_path, discourse_path, output_file):
    """Main function to format parser output from a JSON file."""
    data = load_json(file_path)
    discourse_data = load_json(discourse_path)
    all_sentence_data = data['response']  # Include all sentence data for context

    results = []
    for sentence_data in all_sentence_data:
        # Pass all_sentence_data as the third argument
        results.append(format_sentence(sentence_data, discourse_data))

    formatted_output = '\n'.join(results)
    save_output(output_file, formatted_output)

if __name__ == "__main__":
    # File path to the JSON input
    file_path = "IO/updated_parser_output.json"
    output_file = "IO/usr_output.txt"
    discourse_path = "IO/discourse_output.txt"

    # Call the function to format and save the output
    format_parser_output(file_path, discourse_path, output_file)
