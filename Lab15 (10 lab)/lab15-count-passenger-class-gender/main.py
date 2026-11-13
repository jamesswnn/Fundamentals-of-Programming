# Your Python code goes here
import pandas as pd

df = pd.read_csv('data.csv')

gender = ['male', 'female']

for i in gender:
    df_filter = df[(df['Sex'] == i) & (df['Age'] > 40)]
    
    counts = df_filter['Pclass'].value_counts().to_dict()
    
    print(f"{i} (age>40)")
    
    for pclass in [1, 2, 3]:
        print(f"Pclass {pclass}: {counts.get(pclass, 0)}")
    