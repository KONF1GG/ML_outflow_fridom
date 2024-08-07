import pandas as pd

# of an excel file  
read_file = pd.read_excel ("combined_file_123.xlsx") 
  
# Write the dataframe object 
# into csv file 
read_file.to_csv ("combined_file_123.csv",  
                  index = None, 
                  header=True) 
    
# read csv file and convert  
# into a dataframe object 
# df = pd.DataFrame(pd.read_csv("Test.csv")) 
  
# # show the dataframe 
# print(df)