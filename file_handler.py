import json
import os

FILE_NAME = "volunteers.json"

def save_volunteers(volunteer_data: list):
    with open(FILE_NAME, 'w') as f:
        json.dump(volunteer_data, f, indent=4)
    print("💾 Volunteers saved successfully.")

def load_volunteers():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as f:
        return json.load(f)
