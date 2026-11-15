# lab15-count-passenger-embark-class
import pandas as pd

df = pd.read_csv('data.csv')

embarked = ['S', 'C', 'Q', 'UNK']

for i in embarked:
    df_filter = df[df['Embarked'] == i]
    df_filter = df_filter.sort_values(by=['Pclass', 'Fare'], ascending=[True, False])
    print(f"Embarked: {i}")
    print(df_filter.head()[['Pclass','Fare','Embarked']])
    print(df_filter.tail()[['Pclass','Fare','Embarked']])
