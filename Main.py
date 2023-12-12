
from Caesar_code import *
from Genomics import *

shift = 3
phrase = 'Sweet Home Alabama!'
code_phrase = ceaser(phrase, shift)
phrase_2 = ceaser_ans(code_phrase, shift)




if __name__ == '__main__':
    print(code_phrase)
    print(phrase_2)

    genom_1 = makeDNA(25)
    genom_2 = genom_1.copy()
    genom_2.append("R")
    print(*genom_1)

    str_1 = 'ATAGCATGVSATDGSACTAGC'
    print(*complementWC(genom_2))
    print(isValidDNA(genom_1))
    print(*complementWC(str_1))

    dna_sequence = "ATGGTAGTAAATGATGATGTAATGAGTAGTGA"
    potential_genoms = find_potential_genom(dna_sequence, 3)
    print(potential_genoms)
    print(find_potential_genom(str_1, 3))