import numpy as np
import json

def make_pair(list):
    for i in range(len(list) - 1):
        yield (list[i], list[i+1])

text = open('D:/codding_and_programming/Python/program/markov_chain/shakespeare_mod.txt', 'r').read()
text_words = text.split()

pairs = make_pair(text_words)

words_dist = {}
for word_1, word_2 in pairs:
    if word_1 in words_dist.keys():
        words_dist[word_1].append(word_2)
    else:
        words_dist[word_1] = [word_2]

# with open('D:/codding_and_programming/Python/program/markov_chain/dist.json', 'w') as f:
#     json.dump(words_dist, f)

first_word = np.random.choice(text_words)

while first_word.islower():
    first_word = np.random.choice(text_words)

chain = [first_word]

n_word = 20

for i in range(n_word):
    chain.append(np.random.choice(words_dist[chain[-1]]))

print(' '.join(chain))