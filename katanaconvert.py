import json
import os

# Ask for file location and name
file_location = input("Enter the file location (e.g., /path/to/folder/): ").strip()
file_name = input("Enter the file name (e.g., domain.txt): ").strip()

# Construct full path
input_path = os.path.join(file_location, file_name)

# Define output file
output_name = "katana.jsonl"
output_path = os.path.join(file_location, output_name)

# Check if file exists
if not os.path.isfile(input_path):
    print("Error: The specified file does not exist.")
    exit(1)

# Convert to katana.jsonl format
with open(input_path, "r") as infile, open(output_path, "w") as outfile:
    for line in infile:
        line = line.strip()
        if line:
            json.dump({"url": f"https://{line}"}, outfile)
            outfile.write("\n")

print(f"Conversion successful! File saved as: {output_path}")
