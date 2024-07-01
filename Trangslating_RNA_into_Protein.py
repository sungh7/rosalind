import pandas as pd
from io import StringIO

codons = '''UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G '''

df = pd.read_csv(StringIO(codons), delim_whitespace=True, header=None); df.head()

dic = {}

codons = df.iloc[:,[0,2,4,6]].values.reshape(1, -1)[0]
proteins = df.iloc[:, [1,3,5,7]].values.reshape(1,-1)[0]

codon_table = {k:v for k, v in zip(codons, proteins)}

def rna2protein(seq):
    seq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    seq = seq.replace('\n', '')

    protein = []
    for i in range(len(seq)//3):
        if codon_table[seq[3*i:3*i+3]] == 'Stop':
            break
        protein.append(codon_table[seq[3*i:3*i+3]])

    return ''.join(protein)