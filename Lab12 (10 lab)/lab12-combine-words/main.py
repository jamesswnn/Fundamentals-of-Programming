'''
lab12-combine-words
'''

'''
kwargs = {
    "position": position_text,
    "extra": extra_text
}
'''

def combine_words(word, **kwargs):
    # ---Your Python code goes here---#
    position = kwargs.get("position", "")
    extra = kwargs.get("extra", "")

    if position == 'prefix':
        return extra + word
    elif position == 'suffix':
        return word + extra
    else:
        return word


# Given this code, please fill-in the content in combine_words function
input_text = input()  # work
position_text = input()  # prefix
extra_text = input()  # home

print(combine_words(input_text, position=position_text, extra=extra_text))  # homework