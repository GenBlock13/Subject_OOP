# PotentialGene
import random
def isPotentialGene(dna):
    # длина кратна 3
    if (len(dna) % 3) != 0: return False
    # начинается с кодона начала
    if not dna.startswith('ATG'): return False
    # не имеет кодонов конца внутри
    for i in range(len(dna) - 3):
        if i % 3 == 0:
            if dna[i:i + 3] == 'TAA': return False
            if dna[i:i + 3] == 'TAG': return False
            if dna[i:i + 3] == 'TGA': return False
    # завершается кодоном конца
    if dna.endswith('TAA'): return True
    if dna.endswith('TAG'): return True
    if dna.endswith('TGA'): return True
    return False


def makeDNA(len):
    codons = ['A', 'G', 'C', 'T']
    dna = []
    if len % 3 == 0:
        for i in range(len):
            dna.append(random.choice(codons))
        return 'ATG' + str(dna) + 'TAG'


def isValidDNA(genom):
    status = True
    codons = ['A', 'G', 'C', 'T']
    for x in genom:
        if x not in codons:
            status = False
    return status


def complementWC(genom):
    output = []
    for x in genom:
        match (x):
            case 'A':
                output.append('T')
            case 'T':
                output.append('A')
            case 'C':
                output.append('G')
            case 'G':
                output.append('C')
            case _:
                output.append(x)
    return output


def palindromWC(genom):
    wc_genom = genom[::-1]
    if wc_genom == complementWC(genom):
        return True
    else:
        return False


def shift_DNA(st_1: str, st_2: str):
    if len(st_1) == len(st_2):
        for i in range(len(st_1)):
            if st_1[i:] + st_1[:i] == st_2:
                print('DNA Shift founded!')


def find_potential_genom(dna, length):
    new_genom = []
    tail = ['TAA', 'TAG', 'TGA']
    for i in range(len(dna)):
        if (dna[i:i + 3] == 'ATG'):
            for j in range(i, len(dna), 3):
                if (dna[j:j + 3] in tail):
                    new_genom.append(dna[i:j + 3])
                    i = j + 3
                    break
    return new_genom
