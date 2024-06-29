import os
import json
import datetime
import uuid

def get_facts_from_text(file_path):
        facts = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    fact = {
                        'content': line,
                        'timestamp': datetime.datetime.now().isoformat(),
                        'id': str(uuid.uuid4())
                    }
                    facts.append(fact)
        return facts


def extract_facts_from_directory(facts_folder):
    fact_list = {}
    for filename in os.listdir(facts_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(facts_folder, filename)
            facts = get_facts_from_text(file_path)
            fact_type = filename.replace('_template', '').replace('.txt', '')
            fact_list[fact_type] = facts

    output_file ='facts.json'
    with open(output_file, 'w', encoding='utf-8') as output_file:
        json.dump(fact_list, output_file, indent=4)


facts_folder = 'fact-sheets-txt'
extract_facts_from_directory(facts_folder)
