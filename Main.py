
from Caesar_code import *
from Genomics import *

shift = 3
phrase = 'Sweet Home Alabama!'
code_phrase = ceaser(phrase, shift)
phrase_2 = ceaser_ans(code_phrase, shift)

if __name__ == '__main__':
    print(code_phrase)
    print(phrase_2)