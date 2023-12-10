import os
import json
import pandas as pd

def read_json_files(directory, num_files=10):
    data_frames = []


    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return pd.DataFrame()

 
    file_count = 0

  
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
 
            with open(file_path, 'r') as file:
                data = json.load(file)
                data_frames.append(pd.json_normalize(data))

            file_count += 1

 
            if file_count >= num_files:
                break

 
    result_df = pd.concat(data_frames, ignore_index=True)

    return result_df

def main():
    # Replace 'your_directory' with the path to your directory containing JSON files
    directory_path = 'json_files'

   
    table_data = read_json_files(directory_path, num_files=10)


    print("Table Format:")
    print(table_data)


    excel_filename = 'output_table.xlsx'
    table_data.to_excel(excel_filename, index=False, engine='openpyxl')
    print(f"\nTable saved to '{excel_filename}'")

if __name__ == "__main__":
    main()
