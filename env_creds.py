import os
import json


def get_credentials(data):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_directory, 'creds','creds.json')
    with open(full_path, 'r', encoding='utf-8') as file:
        json_content = file.read()
        python_data = json.loads(json_content)
        return python_data[data]


USER_NAME = get_credentials('user_name')
PASSWORD = get_credentials('password')
