import pandas as pd

# Загрузка данных из первого файла
file1 = 'data/backup2/21ds.xls'
df1 = pd.read_excel(file1)

# Загрузка данных из второго файла
file2 = 'data/backup2/22ds.xls'
df2 = pd.read_excel(file2)

file3 = 'data/backup2/23ds.xls'
df3 = pd.read_excel(file3)

file4 = 'data/backup2/24ds.xls'
df4 = pd.read_excel(file4)

# Объединение данных
combined_df = pd.concat([df1, df2, df3, df4])

# Сохранение объединенных данных в новый файл
output_file = 'MyDataset_12_twice.xlsx'
combined_df.to_excel(output_file, index=False)

print(f"Данные успешно объединены и сохранены в {output_file}")