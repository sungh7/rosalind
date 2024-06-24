bulk = '''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT'''

dic = {}
for line in bulk.split('>')[1:]:
  tag, seq = line.split('\n', 1)
  seq = seq.replace('\n', '')
  base_count = Counter(seq)
  gc_contents = (base_count['G'] + base_count['C']) / len(seq) * 100
  dic[tag] = gc_contents

max_gc = max(dic, key=dic.get)
print(f"{max_gc}\n{gc_contents:.6f}")
