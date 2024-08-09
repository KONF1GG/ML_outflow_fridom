import pandas as pd

# of an excel file  
read_file = pd.read_excel ("MyDataset_month.xlsx") 
  
# Write the dataframe object 
# into csv file 
read_file.to_csv ("MyDataset_month.csv",  
                  index = None, 
                  header=True) 
    
# read csv file and convert  
# into a dataframe object 
# df = pd.DataFrame(pd.read_csv("Test.csv")) 
  
# # show the dataframe 
# print(df)