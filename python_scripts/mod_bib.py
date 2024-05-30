import re

def text_cleaner(text):
  text = re.sub(r'--', ' ', text)
  text = re.sub('[\[].*?[\]]', '', text)
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  text = ' '.join(text.split())
  return text

file = open('D:/codding_and_programming/Python/program/markov_chain/shakespeare.txt', encoding='utf8').read()
file = re.sub(r'Chapter \d+', '', file)

file = text_cleaner(file)

with open('D:/codding_and_programming/Python/program/markov_chain/shakespeare_mod.txt', 'w') as f:
    f.write(file)



# file = open('D:/codding_and_programming/Python/program/markov_chain/shakespeare.txt', encoding='utf8').read()
# paras = file.split('\n\n')

# def del_first_word(para):
#     word = para.split()
#     if len(word) > 5:
#         word.pop(0)
#     else:
#         word.clear()
#     return ' '.join(word)

# with open('D:/codding_and_programming/Python/program/markov_chain/shakespeare_mod.txt', 'w') as f:
#     for para in paras:
#         mod_para = del_first_word(para)
#         mod_file = ''.join(mod_para)
#         f.write(mod_file)
