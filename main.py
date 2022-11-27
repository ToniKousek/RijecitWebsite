# wordle game logic

import glob
from random import choice
import hashlib

# the check_words function is the most important
# returns -1 if word is not in the file
# returns 1 if word is correct
# it returns a tuple with two elements
# a list of the given words
# a list with the coloring lists
# example:
#[['g', ' ', ' ', ' ', ' '], ['g', ' ', 'y', ' ', ' ']]
# when the answer is "aeiou"
# the 'g' is green
# the 'y' is yellow

len_of_words = 5
num_of_tries = 6

# the lookup table
lookup = []
with open(glob.glob('**/*.txt', recursive=True)[0], "r", encoding="utf-8") as file:
    for line in file:
        lookup.append(line.split()[0].lower())

# print(lookup[:100])


def check_coloring(answer: str, word: str):

    word_col = [" " for i in range(len_of_words)]
    temp_answer = [answer[i] for i in range(len_of_words)]
    # set all green
    for i in range(len_of_words):
        if word[i] == temp_answer[i]:
            word_col[i] = "g"
            temp_answer[i] = " "

    # set all yellow
    for i in range(len_of_words):
        #print(f"{(word[i] in answer)=} {word[i]=} {answer=} ")
        if word[i] in temp_answer:
            word_col[i] = "y"
            # find the index of the letter
            temp_answer[temp_answer.index(word[i])] = " "

    return word_col


def check_words(answer: str, words: list[str]):
    print(f"{words=} {words[-1]=} ")
    # check if last word is in the lookup table
    if not (words[-1] in lookup):
        return -1

    # calculate the coloring
    else:
        colored_words = []
        for word in words:
            colored_words.append(check_coloring(answer, word))

    # see if the word is the answer
    if words[-1] == answer:
        return (1, colored_words)
    return (colored_words)


def random_word(date: str) -> str:
    hash = int(hashlib.sha1(date.encode()).hexdigest()[:5], 16)+2007_04_02
    return lookup[hash % (len(lookup))]


def list_word(word_list: list):
    result = []
    for word in word_list:
        for letter in word:
            result.append(letter)
    return result


# example
#words_to = ["aaaaa", "amper"]
#print(check_words("amper", words_to))
