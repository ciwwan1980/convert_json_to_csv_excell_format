import os
import json
import pandas as pd

def read_json_files(directory):
    data_frames = []

   
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return pd.DataFrame()

    
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            print(file_path, "file_path is here ----------")
        
            with open(file_path, 'r') as file:
                data = json.load(file)
                print(data, "data is here ------")
                data_frames.append(pd.json_normalize(data))

                # pd.json_normalize(data): This function from the pandas library normalizes semi-structured JSON data into a flat table. It's particularly useful when dealing with nested JSON structures. The result is a DataFrame.


                print(data_frames, "data_frames is here ----- ")
    # Concatenate the list of data frames into a single data frame
    result_df = pd.concat(data_frames, ignore_index=True)

    return result_df


def main():
   
    directory_path = 'json_files'

    table_data = read_json_files(directory_path)

  
    print("Table Format:")
    print(table_data)

   
    csv_filename = 'output_table1.csv'
    table_data.to_csv(csv_filename, index=False)
    print(f"\nTable saved to '{csv_filename}'")

    excel_filename = 'output_table.xlsx'
    table_data.to_excel(excel_filename, index=False, engine='openpyxl')
    print(f"\nTable saved to '{excel_filename}'")

if __name__ == "__main__":
    main()

