import os
import json
import datetime
import uuid


def text_to_JSON(facts_path):
    result = {}

    # Iterate over all files in the directory
    for filename in os.listdir(facts_path):
        if filename.endswith('.txt'):
            # Extract fact_type from filename
            fact_type = filename.replace('_template', '').replace('.txt', '')
            file_path = os.path.join(facts_path, filename)
            
            facts = []

            # Read and process the file
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:  # Ensure the line is not empty
                        fact = {
                            'content': line,
                            'timestamp': datetime.datetime.now().isoformat(),
                            'id': str(uuid.uuid4())
                        }
                        facts.append(fact)

            # Store the list of facts under the fact_type key
            result[fact_type] = facts

    # Write the result to a JSON file
    output_path = os.path.join(facts_path, 'facts.json')
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(result, output_file, indent=4)

    print(f"Output JSON file created at: {output_path}")

# Example usage
facts_folder = 'fact-sheets'
text_to_JSON(facts_folder)
