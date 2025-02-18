# # # import sys, os
# # # sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
# # from scripts.file_utils import load_json, save_output
# # from scripts.add_tag import format_sentence

# # def format_parser_output(file_path, discourse_path, output_file):
# #     """Main function to format parser output from a JSON file."""
# #     data = load_json(file_path)
# #     discourse_data = load_json(discourse_path)

# #     results = []
# #     for sentence_data in data['response']:
# #         results.append(format_sentence(sentence_data, discourse_data, all_sentence_data))

# #     formatted_output = '\n'.join(results)
# #     save_output(output_file, formatted_output)

# # if __name__ == "__main__":
# #     # File path to the JSON input
# #     file_path = "IO/updated_parser_output.json"
# #     output_file = "IO/usr_output.txt"
# #     discourse_path = "IO/discourse_output.txt"

# #     # Call the function to format and save the output
# #     format_parser_output(file_path, discourse_path, output_file)



# # import sys, os
# # sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
# from scripts.file_utils import load_json, save_output
# from scripts.add_tag import format_sentence

# def format_parser_output(file_path, discourse_path, output_file):
#     """Main function to format parser output from a JSON file."""
#     data = load_json(file_path)
#     discourse_data = load_json(discourse_path)
#     all_sentence_data = data['response']  # Include all sentence data for context

#     results = []
#     for sentence_data in all_sentence_data:
#         # Pass all_sentence_data as the third argument
#         results.append(format_sentence(sentence_data, discourse_data))

#     formatted_output = '\n'.join(results)
#     save_output(output_file, formatted_output)

# if __name__ == "__main__":
#     # File path to the JSON input
#     file_path = "IO/updated_parser_output.json"
#     output_file = "IO/usr_output.txt"
#     discourse_path = "IO/discourse_output.txt"

#     # Call the function to format and save the output
#     format_parser_output(file_path, discourse_path, output_file)
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
import requests
import time
from scripts.file_utils import load_json, save_output
from scripts.add_tag import format_sentence

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


def convert_sentences(data):
    """Convert input data to transformed sentences format."""
    try:
        sentences = []
        project_id = 1  # Fixed project_id as 1

        # Assuming 'data' is the raw input (in list form)
        for line in data:
            line = line.strip()
            if line:
                # Remove extra escape characters for quotes and split the line into sentence_id and sentence
                line = line.replace('\\"', '"')  # Remove escape for quotes
                parts = line.split('.', 1)
                if len(parts) == 2:
                    sentence_id = parts[0].strip()
                    sentence = parts[1].strip().strip('"')
                    sentences.append({
                        "project_id": project_id,
                        "sentence_id": sentence_id,
                        "sentence": sentence
                    })

        # Return the expected transformed format
        return {"sentences": sentences}

    except Exception as e:
        raise Exception(f"Error in convert_sentences: {e}")


def call_api(api_url, data):
    """Send POST request to the specified API."""
    try:
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API call failed. Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        raise Exception(f"Error in call_api: {e}")


def format_parser_output(data, discourse_data):
    """Main function to format parser output and return the response directly."""
    try:
        # print(type(data['response']))  # Check if it's a list or dict
        # print(data['response'])  # Print the actual data

        all_sentence_data = data['response']  # Include all sentence data for context
        print(all_sentence_data)

        results = []
        for sentence_data in all_sentence_data:
            results.append(format_sentence(sentence_data, discourse_data))

        formatted_output = '\n'.join(results)

        return True, formatted_output
    except Exception as e:
        return False, f"Error in format_parser_output: {str(e)}"


@app.route('/usr_builder', methods=['POST'])
def process_usr_builder():
    """
    Step 1: Convert `output.json` to `transformed.json`.
    Step 2: Send `transformed.json` to discourse and morph APIs.
    Step 3: Process and format the responses.
    """
   
    try:
        # Step 1: Receive input data
        input_data = request.json
        if not input_data:
            return jsonify({"status": "error", "message": "No input data provided"}), 400

        # Step 2: Convert sentences
        # transformed_data = convert_sentences(input_data)
        discourse_data = call_api("http://10.2.8.12:8000/discourse_process", input_data)
        morph_data = call_api("http://10.2.8.12:7005/morph", input_data)
        

        # Step 3: Format parser output
        success, message = format_parser_output(morph_data, discourse_data)
    
        if success:
            return jsonify({"status": "success", "message": message}), 200
        else:
            return jsonify({"status": "error", "message": message}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    






if __name__ == "__main__":
    if not os.path.exists('IO'):
        os.makedirs('IO')
    app.run(debug=True, host='0.0.0.0', port=5001)
