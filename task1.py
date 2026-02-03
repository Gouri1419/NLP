# ---------- IMPORTS ----------
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

# ---------- TASK 1: CLEAN AND PROCESS ----------
def clean_and_process(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-z\s]', '', sentence)
    tokens = sentence.split()
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return tokens

# ---------- MAIN ----------
print("----- TASK 1: CLEAN AND PROCESS -----")
text = "The quick, BROWN foxes...they are JUMPING over 10 lazy dogs!"
print("Original Sentence:")
print(text)
print("Processed Tokens:")
print(clean_and_process(text))
