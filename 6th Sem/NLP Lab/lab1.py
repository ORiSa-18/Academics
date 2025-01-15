import nltk
import re

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
