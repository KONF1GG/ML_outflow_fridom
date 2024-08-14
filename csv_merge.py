import pandas as pd

df1 = pd.read_excel('DATASET/backup/afp21.xls')

df2 = pd.read_excel('DATASET/backup/afp22.xls')

df3 = pd.read_excel('DATASET/backup/afp23.xls')

df4 = pd.read_excel('DATASET/backup/afp24.xls')

df5 = pd.read_excel('DATASET/backup/il21.xls')

df6 = pd.read_excel('DATASET/backup/il22.xls')

df7 = pd.read_excel('DATASET/backup/il23.xls')

df8 = pd.read_excel('DATASET/backup/il24.xls')

df9 = pd.read_excel('DATASET/backup/ur21.xls')

df10 = pd.read_excel('DATASET/backup/ur22.xls')

df11 = pd.read_excel('DATASET/backup/ur23.xls')

df12 = pd.read_excel('DATASET/backup/ur24.xls')

df13 = pd.read_excel('DATASET/backup/vas21.xls')

df14 = pd.read_excel('DATASET/backup/vas22.xls')

df15 = pd.read_excel('DATASET/backup/vas23.xls')

df16 = pd.read_excel('DATASET/backup/vas24.xls')
# Объединение данных
combined_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16 ])

# Сохранение объединенных данных в новый файл
output_file = 'DATASET/MyDataset.xlsx'
combined_df.to_excel(output_file, index=False)

print(f"Данные успешно объединены и сохранены в {output_file}")