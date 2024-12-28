import os
import pandas as pd
data_dir = 'data_for_mongoDB'
data = []
# Iterate through the folders and files in the "Data" directory
for file in os.listdir(data_dir):
    file_path = os.path.join(data_dir, file)
    file_name = file
    label = file_name.replace(".xlsx", "")
    print(f"Đang xử lý file: {label}")
    if file.endswith('.xlsx'):
        try:
            df = pd.read_excel(file_path)
            text = df.to_string(index=False)
            data.append([text, label])
            i+=1
            if(i==100):
                break
        except Exception as e:
            print(f"Lỗi khi xử lý file {file_name}: {e}")

print(data[0])