import json

def load_json(file_path):
    """Load the JSON data from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_output(output_file, formatted_output):
    """Save the formatted output to a file."""
    with open(output_file, 'w', encoding='utf-8') as out_f:
        out_f.write(formatted_output)
