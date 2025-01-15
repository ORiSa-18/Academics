import re

sentence = "*Hello, World!*"

if not re.match(r'^[a-zA-Z0-9]', sentence):
    sentence = sentence[1:]
if not re.match(r'[a-zA-Z0-9]$', sentence):
    sentence = sentence[:-1]

print(f"Original Sentence: *Hello, World!*")
print(f"Modified Sentence: {sentence}")
