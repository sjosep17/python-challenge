# libraries import
import os
  
# file path storage
file = 'paragraph_1.txt'
  
# declaring variables
letter_count = 0
  
# open file
with open(file, 'r') as txtfile:
    # reading file
    paragraph = txtfile.read()
  
    # word count
    word_count = paragraph.count(" ") + 1 # +1 to account for the last word
  
    # sentence count
    sentence_count = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")
  
    # average letter count
    for character in paragraph:
        if character.isalpha():
            letter_count += 1 # counting how many characters are letters
    avg_letter_count = letter_count/word_count
  
    # average sentence in length
    avg_sentence = word_count/sentence_count
  
# tests
# print(word_count)
# print(sentence_count)
print(letter_count)
# print(avg_letter_count)
# print(avg_sentence)
  
# printing results to terminal
print("Paragraph Analysis")
print("----------------------------------")
print("Approximate Word Count:", word_count)
print("Approximate Sentence Count:", sentence_count)
print("Average Letter Count:", avg_letter_count)
print("Average Sentence Length:", avg_sentence)

