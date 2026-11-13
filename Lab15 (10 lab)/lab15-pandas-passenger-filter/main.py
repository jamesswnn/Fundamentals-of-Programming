import pandas as pd

df = pd.read_csv('data.csv')

min_age = input()
max_age = input()
survived = input()

if min_age != "-":
    df = df[df["Age"] >= int(min_age)]

if max_age != "-":
    df = df[df["Age"] <= int(max_age)]
    
if survived != '-':
    df = df[df["Survived"] == int(survived)]
    
print(len(df))
    
    

