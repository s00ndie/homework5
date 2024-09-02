import string
text = input('Enter your text:')
punc = str.maketrans('', '', string.punctuation )
clean_text = text.translate(punc)
clean_text= clean_text.title().replace(' ', '')
if len(clean_text) > 140:
    clean_text=clean_text[:140]
print(clean_text)
print(len(clean_text))