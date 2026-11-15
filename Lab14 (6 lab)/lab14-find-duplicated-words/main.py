#lab14-find-duplicated-words
words = str(input())
words = words.split(" ")

previous_word = []
count_for_find = 0

for i in range(len(words)):
    same_words = words[i]
    same_words_count = words.count(same_words)
    
    if same_words not in  previous_word:
        if same_words_count > 1:
            result = f"{same_words}: {same_words_count}"
            print(result)
            count_for_find = 1
            previous_word.append(same_words)
    else:
        continue
    
if count_for_find == 0:
    print("no duplicated word")

