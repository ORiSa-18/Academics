#Q1
text = """Hello, world!
This is a sample text.

Let's split this text at spaces, new lines, and punctuation marks!"""

pattern = r'[^\w]+'
words = re.split(pattern,text)
words.remove('')

print(words)

#Q1.Additional
import re

text = """
The project started on 15/03/2024 and is expected to end by 30/06/2024.
Some important milestones are on 01/04/2024 and 15/05/2024.
Invalid dates like 32/13/2024 or 00/00/2024 will not be matched.
"""

pattern = r"(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/([12]\d{3})"
dates = re.findall(pattern, text)
formatted_dates = [f"{day}/{month}/{year}" for day, month, year in dates]
print("Dates found:", formatted_dates)

#Q2.Additional
import re

text = """
Contact us at:
123-456-7890
(123) 456-7890
123.456.7890
1234567890
+1 123-456-7890
+1 (123) 456-7890
+44.123.456.7890
Invalid numbers: 123-45-678, 12-345-6789
"""

pattern = r"(?:\+\d{1,3}[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})|\b\d{10}\b|\+\d{1,3}\s\d{1,3}\s\d{3,4}\s\d{4}"
numbers = re.finditer(pattern, text)
found_numbers = [' '.join(match.group(0).split()) for match in numbers]

print("Phone numbers found:")
for i, number in enumerate(found_numbers, 1):
    print(f"{i}. {number}")
    
#Q1. WRITE A PROGRAM TO REMOVE THE FIRST AND LAST CHARACTERS IF THEY ARE NOT LETTERS OR NUMBERS FROM A GIVEN SENTENCE.
sentence = "*Hello, World!*"

if not re.match(r'^[a-zA-Z0-9]', sentence):
    sentence = sentence[1:]
if not re.match(r'[a-zA-Z0-9]$', sentence):
    sentence = sentence[:-1]

print(f"Original Sentence: *Hello, World!*")
print(f"Modified Sentence: {sentence}")

#Q1. Additional Question: Write a program to count the number of characters that are not letters or numbers in a given sentence.
import re

sentence = "Hello, world! 123."
pattern = r'[^a-zA-Z0-9]'
matches = re.findall(pattern, sentence)
count = len(matches)

print(f'The number of characters that are not letters or numbers: {count}')

#Q2. Additional Question: Write a program to replace all characters that are not letters or numbers in a sentence with a specified character.
 
import re

sentence = "Hello, World! 123."
replacement_char = '_'

modified_sentence = re.sub(r'[^a-zA-Z0-9]', replacement_char, sentence)
print(modified_sentence)

#Q1. WRITE A PROGRAM TO SPLIT A WORD INTO PAIR’S AT ALL POSSIBLE POSITIONS. FOR EXAMPLE, CARRIED WILL BE SPLIT INTO {C, ARRIED, CA ,RRIED, CAR, RIED, CARR, IED, CARRI, ED, CARRI, D}.

word = "CARRIED"
result = []
for i in range(1, len(word)):
    part1 = word[:i]
    part2 = word[i:]
    result.append((part1, part2))

for split in result:
    print(split)

# Additional Exercise: Q1.Write a program to generate all possible prefixes and suffixes of a given word.

word = "CARRIED"
prefixes = []
suffixes = []
for i in range(1, len(word) + 1):
    prefixes.append(word[:i])
    suffixes.append(word[-i:])

for prefix in prefixes:
    print(prefix)

for suffix in suffixes:
    print(suffix)

  
# Additional Exercise: Q1.Write a program to generate all possible prefixes and suffixes of a given word.

import random

word = "CARRIED"
positions = list(range(1, len(word)))
random.shuffle(positions)

result = []
for i in positions:
    part1 = word[:i]
    part2 = word[i:]
    result.append((part1, part2))

for split in result:
    print(split)
    
#Q1. WRITE A PROGRAM TO FIND OUT THE FREQUENCIES OF DISTINCT WORDS, GIVEN A SENTENCE USING N-GRAMS.

import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

def n_grams(text,n):
    words = word_tokenize(text)
    nGrams = ngrams(words, n)
    return list(nGrams)

text = "I love Python"

n=2

bigrams = n_grams(text, n)

hmap = Counter(bigrams)

for pair in hmap:
    print(pair," ",hmap[pair])

#Additional Exercise: Q1. WRITE A PROGRAM TO FIND OUT THE FREQUENCIES OF DISTINCT WORDS, GIVEN A SENTENCE USING N-GRAMS.

import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

def n_grams(text,n):
    words = word_tokenize(text)
    nGrams = ngrams(words, n)
    return list(nGrams)

text = "I love Python"

n=2

bigrams = n_grams(text, n)

hmap = Counter(bigrams)
total = len(bigrams)

for pair in hmap:
    print("P[",pair,"]=",hmap[pair]/total)

#Additional Exercise: Q2.Write a program to generate n-grams in reverse order (e.g., starting from the end of the sentence).

import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

def n_grams(text,n):
    words = word_tokenize(text)
    nGrams = ngrams(words, n)
    return list(nGrams)

text = "I love Python"

n=2

bigrams = n_grams(text, n)
bigrams = bigrams[::-1]

for gram in bigrams:
    print(gram[::-1])
    
#Q. Remove Digits from a Sentence

import re

def remove_digits(sentence):
    return re.sub(r'\d+', '', sentence)

# Example usage
sentence = "This is a test 123 with digits 4567."
result = remove_digits(sentence)
print(result)

#Q. Count Digits in a Sentence

import re

def count_digits(sentence):
    digits = re.findall(r'\d', sentence)
    return len(digits)

# Example usage
sentence = "This is a test 123 with digits 4567."
result = count_digits(sentence)
print(result)

#Q. Extract Digits from a Sentence
import re

def extract_digits(sentence):
    digits = re.findall(r'\d+', sentence)
    return digits

# Example usage
sentence = "This is a test 123 with digits 4567."
result = extract_digits(sentence)
print(result)


# Q Greedily Tokenize a Sentence Prioritizing Specific Patterns
import re

def greedy_tokenizer_with_priority(sentence):
    date_pattern = r'\d{1,2}/\d{1,2}/\d{2,4}'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    dates = re.findall(date_pattern, sentence)
    emails = re.findall(email_pattern, sentence)
    
    remaining_sentence = re.sub(date_pattern, '', sentence)
    remaining_sentence = re.sub(email_pattern, '', remaining_sentence)
    
    tokens = re.findall(r'\S+', remaining_sentence)
    
    return {
        "dates": dates,
        "emails": emails,
        "tokens": tokens
    }

# Example usage
sentence = "Contact me at example@example.com on 12/25/2025 for details."
result = greedy_tokenizer_with_priority(sentence)
print(result)

#Q. Remove Noise from Textual Data (e.g., Hashtags)
import re

def remove_noise_and_hashtags(text):
    cleaned_text = re.sub(r'#\w+', '', text)
    return cleaned_text

# Example usage
text = "This is a #test tweet with #hashtags."
result = remove_noise_and_hashtags(text)
print(result)

#Normalize Text by Removing Extra Whitespace and Converting to Lowercase

import re

def remove_noise_and_hashtags(text):
    cleaned_text = re.sub(r'#\w+', '', text)
    return cleaned_text

# Example usage
text = "This is a #test tweet with #hashtags."
result = remove_noise_and_hashtags(text)
print(result)

#Q. Normalize Text by Removing Extra Whitespace and Converting to Lowercase
def normalize_text(text):
    return ' '.join(text.split()).lower()

# Example usage
text = "   Hello   World   "
result = normalize_text(text)
print(result)

#Q. Extract Dates in Various Formats
import re

def extract_dates(text):
    date_patterns = [
        r'\d{1,2}/\d{1,2}/\d{2,4}',  # DD/MM/YYYY or MM/DD/YYYY
        r'\d{1,2}-\d{1,2}-\d{2,4}',  # DD-MM-YYYY or MM-DD-YYYY
        r'\w+ \d{1,2}, \d{4}'  # Month Day, Year
    ]
    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))
    return dates

# Example usage
text = "The meeting is on 12/25/2025 or 25-12-2025 and also on December 25, 2025."
result = extract_dates(text)
print(result)

#Q. Extract and Standardize Phone Numbers
import re

def extract_and_standardize_phone_numbers(text):
    phone_patterns = [
        r'\(\d{3}\) \d{3}-\d{4}',  # (123) 456-7890
        r'\d{3}-\d{3}-\d{4}',  # 123-456-7890
        r'\d{3}\.\d{3}\.\d{4}',  # 123.456.7890
        r'\d{10}'  # 1234567890
    ]
    phone_numbers = []
    for pattern in phone_patterns:
        phone_numbers.extend(re.findall(pattern, text))
    
    standardized_numbers = []
    for number in phone_numbers:
        # Remove non-digit characters
        digits = re.sub(r'\D', '', number)
        # Standardize to (123) 456-7890 format
        standardized_number = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        standardized_numbers.append(standardized_number)
    
    return standardized_numbers

# Example usage
text = "Call me at (123) 456-7890 or 123-456-7890 or 123.456.7890 or 1234567890."
result = extract_and_standardize_phone_numbers(text)
print(result)

#Q.Perform Lemmatization and Stemming
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Ensure necessary NLTK resources are downloaded
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

def lemmatize_and_stem(text):
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    
    words = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    
    lemmatized_words = []
    stemmed_words = []
    
    for word, pos in pos_tags:
        # Convert POS tag to WordNet format for lemmatization
        if pos.startswith('J'):
            pos = 'a'
        elif pos.startswith('V'):
            pos = 'v'
        elif pos.startswith('N'):
            pos = 'n'
        elif pos.startswith('R'):
            pos = 'r'
        else:
            pos = 'n'  # Default to noun
        
        lemmatized_word = lemmatizer.lemmatize(word, pos)
        stemmed_word = stemmer.stem(word)
        
        lemmatized_words.append(lemmatized_word)
        stemmed_words.append(stemmed_word)
    
    return lemmatized_words, stemmed_words

# Example usage
text = "Running runs run quickly."
result_lemmatized, result_stemmed = lemmatize_and_stem(text)
print("Lemmatized:", result_lemmatized)
print("Stemmed:", result_stemmed)

#Q.Custom Tokenizer Handling Multiple Noise Types
import re
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Ensure necessary NLTK resources are downloaded
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

def custom_tokenizer(text):
    # Remove URLs, hashtags, mentions
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # URLs
    text = re.sub(r'#\w+', '', text)  # Hashtags
    text = re.sub(r'@\w+', '', text)  # Mentions
    
    # Tokenize and remove punctuation
    tokens = nltk.word_tokenize(text)
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]
    
    # Lemmatize and stem tokens
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    
    pos_tags = nltk.pos_tag(tokens)
    
    lemmatized_tokens = []
    stemmed_tokens = []
    
    for token, pos in pos_tags:
        # Convert POS tag to WordNet format for lemmatization
        if pos.startswith('J'):
            pos = 'a'
        elif pos.startswith('V'):
            pos = 'v'
        elif pos.startswith('N'):
            pos = 'n'
        elif pos.startswith('R'):
            pos = 'r'
        else:
            pos = 'n'  # Default to noun
        
        lemmatized_token = lemmatizer.lemmatize(token, pos)
        stemmed_token = stemmer.stem(token)
        
        lemmatized_tokens.append(lemmatized_token)
        stemmed_tokens.append(stemmed_token)
    
    return lemmatized_tokens, stemmed_tokens

# Example usage
text = "Running runs run quickly! Check out https://example.com and #test."
result_lemmatized, result_stemmed = custom_tokenizer(text)
print("Lemmatized:", result_lemmatized)
print("Stemmed:", result_stemmed)

#Q.Named Entity Recognition (NER) System
import spacy

# Load English language model
nlp = spacy.load('en_core_web_sm')

def ner_system(text):
    doc = nlp(text)
    
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

# Example usage
text = "Apple is looking at buying U.K. startup for $1 billion."
result = ner_system(text)
print(result)


#Q.Replace Social Media Slangs
def replace_slangs(text):
    slangs = {
        "btw": "by the way",
        "imo": "in my opinion",
        "tbh": "to be honest"
    }
    
    for slang, full_form in slangs.items():
        text = text.replace(slang, full_form)
    
    return text

# Example usage
text = "I think btw we should go, imo it's a good idea, tbh."
result = replace_slangs(text)
print(result)

#Q. Replace Slangs, Abbreviations, and Emojis
import re

def replace_slangs_emojis(text):
    slangs = {
        "btw": "by the way",
        "imo": "in my opinion",
        "tbh": "to be honest"
    }
    
    emojis = {
        "😊": "smiling face",
        "👍": "thumbs up"
    }
    
    for slang, full_form in slangs.items():
        text = text.replace(slang, full_form)
    
    for emoji, description in emojis.items():
        text = text.replace(emoji, description)
    
    # Normalize punctuation
    text = re.sub(r'([.!?])\1+', r'\1', text)
    
    return text

# Example usage
text = "I think btw we should go, imo it's a good idea, tbh 😊👍."
result = replace_slangs_emojis(text)
print(result)

#q. Replace Slang, Standardize Punctuation, and Convert to Lowercase
import re

def normalize_text(text):
    slangs = {
        "btw": "by the way",
        "imo": "in my opinion",
        "tbh": "to be honest"
    }
    
    for slang, full_form in slangs.items():
        text = text.replace(slang, full_form)
    
    # Standardize punctuation
    text = re.sub(r'([.!?])\1+', r'\1', text)
    
    # Convert to lowercase
    text = text.lower()
    
    return text

# Example usage
text = "I THINK BTW WE SHOULD GO, IMO IT'S A GOOD IDEA, TBH!!!"
result = normalize_text(text)
print(result)

#Q. Part of Speech Tagging
import nltk

# Ensure necessary NLTK resources are downloaded
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    words = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    
    return pos_tags

# Example usage
text = "Running runs run quickly."
result = pos_tagging(text)
print(result)

#Q. Analyze Sentence Structure and Extract Noun Phrases
import spacy

# Load English language model
nlp = spacy.load('en_core_web_sm')

def analyze_sentence(text):
    doc = nlp(text)
    
    # Part of speech tagging
    pos_tags = [(token.text, token.pos_) for token in doc]
    
    # Dependency parsing
    dependencies = [(token.text, token.dep_, token.head.text) for token in doc]
    
    # Named Entity Recognition
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Noun phrase extraction
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    
    return pos_tags, dependencies, entities, noun_phrases

# Example usage
text = "Apple is looking at buying U.K. startup for $1 billion."
result_pos, result_dependencies, result_entities, result_noun_phrases = analyze_sentence(text)
print("POS Tags:", result_pos)
print("Dependencies:", result_dependencies)
print("Entities:", result_entities)
print("Noun Phrases:", result_noun_phrases)
