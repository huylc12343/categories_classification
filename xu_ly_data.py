import os
import pandas as pd
from pyvi import ViTokenizer
from pyvi import ViPosTagger
from pyvi import ViUtils
import csv

import re

def remove_punctuation(text):

    # Define a regular expression pattern to match unnecessary punctuation
    pattern = r'[.!?(){}\/~`""“”:\']+(?!\S)'
    
    # Use re.sub() to replace all matches with an empty string
    cleaned_text = re.sub(pattern, '', text)
    
    return cleaned_text


# Set the directory where the "Data" folder is located
data_dir = 'Data'
data = []

# Iterate through the folders and files in the "Data" directory
for folder in os.listdir(data_dir):
    folder_path = os.path.join(data_dir, folder)
    if os.path.isdir(folder_path):
        label = folder
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if file.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-16') as f:
                    text = f.read()
                    tokenized_text = ViTokenizer.tokenize(text)
                    new_string = tokenized_text.replace("\n" ,"")
                    new_string = remove_punctuation(new_string)
                data.append([new_string, label])

# Create the CSV file
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(['text', 'label'])
    writer.writerows(data)

print("Done")