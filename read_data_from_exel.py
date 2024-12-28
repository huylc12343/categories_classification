import pandas as pd
import re
import os 
from pyvi import ViTokenizer
from pyvi import ViPosTagger
from pyvi import ViUtils
import csv


def remove_punctuation(text):
    # sử dụng regular expression để loại bỏ các dấu câu
    # pattern = r'[!?(){}\/~`“”:\']+(?!\S)'
    # pattern = r'[.,!?(){}\/~`“”:"\']+(?!\S)'
    pattern = r'[*&-.,!?(){}\/~`’“”:""–\'\[\]]+(?!\S)'

    cleaned_text = re.sub(pattern, '', text)

    return cleaned_text

def read_data_from_excels(data_dir):
    data = []
    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)
        file_name = file
        label = file_name.replace(".xlsx", "")
        print(f"Đang xử lý file: {label}")
        if file.endswith('.xlsx'):
            try:
                df = pd.read_excel(file_path)
                for i in df.index:
                    text = df['Content'][i]
                    # new_string = remove_punctuation(new_string)
                    # tokenized_text = ViTokenizer.tokenize(text)
                    # new_string = tokenized_text.replace("\n" ,"")
                    tokenized_text = ViTokenizer.tokenize(text)
                    new_string = tokenized_text.replace("\n" ,"")
                    new_string = remove_punctuation(new_string)
                    data.append([new_string, label])
            except Exception as e:
                print(f"Lỗi khi xử lý file {file_name}: {e}")
    return data

# df = pd.read_excel("sohoa_new_test.xlsx")
# # truoc khi xu ly
# print(df['Content'][0]) 
# #sau khi xu ly
# print("Sau khi xu ly",remove_punctuation(df["Content"][0])) 

processed_data = read_data_from_excels("data_for_mongoDB")

output_file = "data_for_mongoDB.csv"
try:
    # Tạo DataFrame từ processed_data
    df = pd.DataFrame(processed_data, columns=["Content", "Label"])
    # Lưu vào file CSV
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Dữ liệu đã được lưu vào {output_file}")
except Exception as e:
    print(f"Lỗi khi lưu dữ liệu: {e}")