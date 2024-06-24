tt = '''GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT'''
for ix in range(len(tt.split('\n'))//2):
    ref, query = tt.split('\n')[ix], tt.split('\n')[ix+1]
    count = 0
    for i in range(len(ref)):
        if ref[i] != query[i]:
            count += 1
    print(count)
