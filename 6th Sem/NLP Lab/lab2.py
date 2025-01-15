import re

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
