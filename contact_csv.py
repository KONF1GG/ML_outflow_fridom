import pandas as pd

# Загрузка CSV-файлов в DataFrame
df1 = pd.read_csv('filtered_file_MyDataset_12_not_twice.csv')
df2 = pd.read_csv('filtered_file_MyDataset_month.csv')

# Объединение DataFrame по столбцам
df_combined = pd.concat([df1, df2], axis=1)

# Сохранение объединенного DataFrame в новый CSV-файл
df_combined.to_csv('MYDATASET_3_1.csv', index=False)

# Вывод первых нескольких строк объединенного DataFrame для проверки
print(df_combined.head())
# import pandas as pd

# # Загрузка исходного CSV-файла в DataFrame
# df = pd.read_csv('MyDataset_12_twice.csv')

# # # Выбор только нужных столбцов
# # columns_to_keep = ['failCount', 'lifeTime', 'activeLife']
# # df_filtered = df[columns_to_keep]

# # # Сохранение изменённого DataFrame в новый CSV-файл
# # df_filtered.to_csv('filtered_file_MyDataset_month.csv', index=False)

# df = df[~((df['year'] == 2022) & (df['mounth'] == 2))]

# df.to_csv('filtered_file_MyDataset_12_not_twice.csv', index=False)

# # Вывод первых нескольких строк для проверки
# print(df_filtered.head())