import os
import json
import pandas as pd

def process_json_files(directory):

    file_list = os.listdir(directory)
    print(f"List of files in '{directory} directory: {file_list}")

    # # Iterate through each file in the directory
    # for filename in file_list:
    #     # Print the current filename before checking for '.json' extension
    #     print(f"Checking filename: {filename}")

    # or the above for details 

    for filename in os.listdir(directory):
        # Check if the current file has a '.json' extension
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            # Print the full path to the current JSON file
            print(f"Processing file: {file_path} file pyth is here ------ ")
           


def main():
 
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    directory_path = os.path.join(script_directory, 'json_files')
    
    process_json_files(directory_path)

if __name__ == "__main__":
    main()
