import pandas as pd

# Загрузка данных из первого файла
file1 = 'data/backup3/21.xls'
df1 = pd.read_excel(file1)

# Загрузка данных из второго файла
file2 = 'data/backup3/22.xls'
df2 = pd.read_excel(file2)

file3 = 'data/backup3/23.xls'
df3 = pd.read_excel(file3)

file4 = 'data/backup3/24.xls'
df4 = pd.read_excel(file4)

# Объединение данных
combined_df = pd.concat([df1, df2, df3, df4])

# Сохранение объединенных данных в новый файл
output_file = 'MyDataset.xlsx'
combined_df.to_excel(output_file, index=False)

print(f"Данные успешно объединены и сохранены в {output_file}")