import os
import json
import csv

# Path to the directory containing JSON files
json_dir = r'C:\TESTCPP\Datasci\Final_project\Data 2018-2023\Project\2018'
output_csv = r'C:\TESTCPP\Datasci\Final_project\target3.csv'

# Open the CSV file for writing
with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header
    csv_writer.writerow(['filename','scopus_link','citedby_link'])

    # Loop through all JSON files in the directory
    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(json_dir, filename)
            
            # Open and read each JSON file
            with open(file_path, 'r', encoding='utf-8') as json_file:
                try:
                    data = json.load(json_file)

                    # Extract fields from JSON
                    coredata = data.get('abstracts-retrieval-response', {}).get('coredata', {})
                    links = coredata.get('link', [])  # `link` is a list of dictionaries
                    
                    scopus_link = None
                    citedby_link = None
                    for link in links:
                        if link.get('@rel') == "scopus":
                            scopus_link = link.get('@href', None)
                        elif link.get('@rel') == "scopus-citedby":
                            citedby_link = link.get('@href', None)

                    # Write row to CSV
                    csv_writer.writerow([filename, scopus_link, citedby_link])
                
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {file_path}")

print(f"Data from all JSON files has been extracted and saved to {output_csv}.")