### 1. WRITE A PROGRAM GIVEN A PIECE OF TEXT, WE WANT TO SPLIT THE TEXT AT ALL SPACES (INCLUDING NEW LINE CHARACTERS AND CARRIAGE RETURNS) AND PUNCTUATION MARKS.
```python
import re
text = "Hello, world!\nHow are you?"
print(re.split(r'[\s\W]+', text))
```

### 2. Write a regex pattern to extract all dates in the format DD/MM/YYYY from a paragraph of text.
```python
import re
text = "Dates: 12/03/2020 and 25/12/2021"
print(re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text))
```

### 3. How would you use regular expressions to identify all phone numbers in a text document?
```python
text = "Call me at 123-456-7890 or (987) 654-3210"
print(re.findall(r'(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}', text))
```

### 4. WRITE A PROGRAM TO REMOVE THE FIRST AND LAST CHARACTERS IF THEY ARE NOT LETTERS OR NUMBERS FROM A GIVEN SENTENCE.
```python
text = "#Hello world!"
print(re.sub(r'^\W+|\W+$', '', text))
```

### 5. Write a program to count the number of characters that are not letters or numbers in a given sentence.
```python
text = "Hello! How are you?"
print(len(re.findall(r'\W', text)))
```

### 6. Write a program to replace all characters that are not letters or numbers in a sentence with a specified character.
```python
text = "Hey! You@there."
print(re.sub(r'\W', '-', text))
```

### 7. WRITE A PROGRAM TO SPLIT A WORD INTO PAIR’S AT ALL POSSIBLE POSITIONS.
```python
word = "carried"
print([(word[:i], word[i:]) for i in range(1, len(word))])
```

### 8. Write a program to generate all possible prefixes and suffixes of a given word.
```python
word = "text"
print([word[:i] for i in range(1, len(word)+1)])
print([word[i:] for i in range(len(word))])
```

### 9. Write a program to split a word into two parts at random positions and print all splits.
```python
import random
word = "random"
print([(word[:i], word[i:]) for i in random.sample(range(1, len(word)), len(word)-1)])
```

### 10. WRITE A PROGRAM TO FIND OUT THE FREQUENCIES OF DISTINCT WORDS, GIVEN A SENTENCE USING N-GRAMS.
```python
from nltk import ngrams
from collections import Counter
text = "the cat in the hat"
print(Counter(ngrams(text.split(), 2)))
```

### 11. Write a program to calculate the probabilities of each n-gram in a sentence or text.
```python
from nltk import ngrams
from collections import Counter
text = "the cat in the hat"
words = text.split()
grams = list(ngrams(words, 2))
c = Counter(grams)
total = sum(c.values())
print({k: v/total for k, v in c.items()})
```

### 12. Write a program to generate n-grams in reverse order.
```python
from nltk import ngrams
text = "the cat in the hat"
print(list(ngrams(text.split()[::-1], 2)))
```

### 13. WRITE A PROGRAM TO REMOVE DIGITS FROM A GIVEN SENTENCE USING GREEDY TOKENIZER.
```python
text = "Th3 qu1ck br0wn fox."
print(re.sub(r'\d+', '', text))
```

### 14. Write a program to count how many digits are present in a given sentence.
```python
text = "Th3 qu1ck br0wn fox."
print(len(re.findall(r'\d', text)))
```

### 15. Write a program to extract and print all digits from a sentence using a greedy tokenizer.
```python
text = "Th3 qu1ck br0wn fox."
print(re.findall(r'\d+', text))
```

### 16. DEMONSTRATE NOISE REMOVAL FOR ANY TEXTUAL DATA AND REMOVE REGULAR EXPRESSION PATTERN SUCH AS HASHTAG FROM TEXTUAL DATA.
```python
text = "#hello @world! This is #cool."
print(re.sub(r'#\w+', '', text))
```

### 17. Write a program to detect and remove emoticons or emojis from textual data.
```python
import emoji
text = "I love 🍕 and 😂"
print(emoji.replace_emoji(text, replace=''))
```

### 18. Write a program to normalize text by removing extra whitespace and converting all text to lowercase.
```python
text = "  Hello   World!   "
print(' '.join(text.lower().split()))
```

### 19. Write a python program to extract all dates in various formats.
```python
text = "12/12/2020, Dec 12, 2020, 12-12-2020"
print(re.findall(r'(\d{2}[-/]\d{2}[-/]\d{4}|\b\w+ \d{1,2}, \d{4})', text))
```

### 20. Write a python program to extract phone numbers and standardize format.
```python
text = "123-456-7890, (123)456-7890"
phones = re.findall(r'(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}', text)
print([''.join(re.findall(r'\d', p)) for p in phones])
```

### 21. PERFORM LEMMATIZATION AND STEMMING USING PYTHON LIBRARY NLTK
```python
from nltk.stem import WordNetLemmatizer, PorterStemmer
w = "running"
print(PorterStemmer().stem(w), WordNetLemmatizer().lemmatize(w, 'v'))
```

### 22. Write a custom tokenizer with stemming and lemmatization.
```python
import re
from nltk.stem import PorterStemmer, WordNetLemmatizer
text = "@john #fun https://t.co Wow!!! running fast."
tokens = re.findall(r'\b\w+\b', text.lower())
ps, lm = PorterStemmer(), WordNetLemmatizer()
print([(ps.stem(w), lm.lemmatize(w)) for w in tokens])
```

### 23. NER system and normalize text.
```python
import spacy
text = "Apple was founded on April 1, 1976 by Steve Jobs."
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
print([(ent.text, ent.label_) for ent in doc.ents])
```

### 24. Replace social media slangs.
```python
text = "brb, I'll ttyl. lol!"
d = {'brb':'be right back','ttyl':'talk to you later','lol':'laughing out loud'}
print(' '.join([d.get(w, w) for w in text.lower().split()]))
```

### 25. Replace slangs/emojis, normalize punctuation.
```python
slangs = {'u':'you','lol':'laugh','brb':'be right back'}
emojis = {':)':'smile',':(':'sad'}
text = "lol u :)!!!"
for k,v in {**slangs, **emojis}.items(): text = text.replace(k,v)
print(re.sub(r'!+', '!', text))
```

### 26. Normalize case, slang, punctuation.
```python
text = "OMG!!! u r awesome!!!"
d = {'omg':'oh my god','u':'you','r':'are'}
text = ' '.join([d.get(w, w) for w in re.sub(r'[!]+', '!', text.lower()).split()])
print(text)
```

### 27. POS tagging.
```python
import nltk
nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')
print(nltk.pos_tag(nltk.word_tokenize("Dogs bark loudly")))
```

### 28-36. NLP pipeline with POS, dependency, NER, chunking, multilingual.
```python
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Barack Obama was born in Hawaii.")
print([(w.text, w.pos_) for w in doc])
print([(w.text, w.dep_, w.head.text) for w in doc])
print([chunk.text for chunk in doc.noun_chunks])
print([(ent.text, ent.label_) for ent in doc.ents])
spacy.displacy.render(doc, style='dep', jupyter=False)
```

### 37. Text classification using HMM.
```python
from hmmlearn import hmm
import numpy as np
X = np.array([[0], [1], [2], [1]]); lengths = [4]
model = hmm.MultinomialHMM(n_components=2).fit(X, lengths)
print(model.predict(X))
```

### 38-42. Train HMM on one domain, test on another.
```python
# Placeholder: Just reuse HMM model across two fake datasets
X1 = np.array([[0], [1]]); X2 = np.array([[1], [0]]);
model = hmm.MultinomialHMM(n_components=2).fit(X1, [2])
print(model.score(X2))
```

### 43-47. Hybrid HMM + Naive Bayes.
```python
from sklearn.naive_bayes import GaussianNB
X = np.array([[0], [1], [1]]); y = [0, 1, 1]
posteriors = hmm.MultinomialHMM(n_components=2).fit(X, [3]).predict_proba(X)
clf = GaussianNB().fit(posteriors, y)
print(clf.predict(posteriors))
```
