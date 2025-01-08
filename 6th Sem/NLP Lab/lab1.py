import nltk
import re

text = """Hello, world!
This is a sample text.

Let's split this text at spaces, new lines, and punctuation marks!"""

pattern = r'[^\w]+'
words = re.split(pattern,text)
words.remove('')

print(words)
