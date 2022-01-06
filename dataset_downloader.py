import pandas as pd
print('Checking for SkillCraft1_Dataset.csv file in current directory...')
try:
  data_df = pd.read_csv('SkillCraft1_Dataset.csv')    
  print('Data already in current directory!')
except:
  print('Data not found, proceeding to download necessary files...')
  data_url ='http://archive.ics.uci.edu/ml/machine-learning-databases/00272/SkillCraft1_Dataset.csv'
  data_df = pd.read_csv(data_url)  
  print('Data succesfully downloaded!, proceeding to save data in current folder...')
  data_df.to_csv('SkillCraft1_Dataset.csv',index = False)
  data_df = pd.read_csv('SkillCraft1_Dataset.csv')  
  print('Data succesfully saved!')

  print('Exiting program.')