#!/usr/bin/python3
  
import sys
import re
import string

def remove_punctuation(word):
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    return regex.sub('', word)

def process_data():
    for line in sys.stdin:
        line = line.strip()
        words = line.split()

        for word in words:
            formatted_word = remove_punctuation(word)
            if len(formatted_word) > 0:
                lower_case_word = formatted_word.lower()
                print(f'{lower_case_word}\t1')

if __name__ == "__main__":
    process_data()
