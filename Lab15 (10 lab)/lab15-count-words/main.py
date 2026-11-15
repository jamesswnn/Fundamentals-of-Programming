# lab15-count-words
import pandas as pd

df = pd.read_csv('data.csv')

word = input()
word_count = df['text'].str.count(word).sum()

print(word_count)
