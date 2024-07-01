import pandas as pd
from io import StringIO

bulk = '''>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
'''

def find_consensus_profile(bulk):
    bulks = bulk[1:].split('\n>')
    txt = [list(''.join(b.split('\n')[1:])) for b in bulks]

    df = pd.DataFrame(txt)
    dic = {'A':[], 'C':[], 'G':[], 'T':[]}

    consensus = ''
    for i in df:
        counts = df[i].value_counts()
        bases = counts.index
        consensus += bases[0]
        if len(bases) != 4:
            for k in ({'A', 'T', 'G', 'C'} - set(bases)):
                dic[k].append(str(0))
        for k, v in counts.to_dict().items():
            dic[k].append(str(v))



    for i in dic:
        f(f"{concensus} \n {i}: {' '.join(dic[i])}")
        
if __name__ ='__main__':
    find_consensus_profile(bulk)