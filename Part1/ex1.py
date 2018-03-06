from nltk.tokenize import sent_tokenize, word_tokenize

ex_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is blue!"

print(sent_tokenize(ex_text))
print(word_tokenize(ex_text))

for i in word_tokenize(ex_text):
    print(i)