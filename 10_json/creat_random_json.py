import json
import random
import os

def generate_random_data():
    data = {
        "name": random.choice(["Alice", "Bob", "Charlie", "David"]),
        "age": random.randint(20, 50),
        "city": random.choice(["New York", "Los Angeles", "Chicago", "San Francisco"])
    }
    return data

def create_json_file(filename):
    data = generate_random_data()
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def create_random_json_files(directory, num_files=10):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(1, num_files + 1):
        filename = os.path.join(directory, f"sample{i}.json")
        create_json_file(filename)
        print(f"Created: {filename}")

if __name__ == "__main__":
    output_directory = 'json_files'
    create_random_json_files(output_directory, num_files=10)
