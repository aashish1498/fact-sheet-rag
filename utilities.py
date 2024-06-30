import json
import random
import string

alphabet = string.ascii_lowercase + string.digits

def generate_id():
    return ''.join(random.choices(alphabet, k=16))


def save_to_json(jsonObject, filepath):
    with open(filepath, 'w', encoding='utf-8') as output_file:
        json.dump(jsonObject, output_file, indent=4)
