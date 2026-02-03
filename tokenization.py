import nltk
nltk.download('punkt_tab')
text="I love pizza!"
tokens=nltk.word_tokenize(text)
print(tokens)  