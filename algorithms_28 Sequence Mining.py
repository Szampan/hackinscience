from collections import Counter

def seq_mining(seqs: list, f: float, max_length: int):
    if max_length > len(max(seqs, key=len)):
        max_length = len(max(seqs, key=len))
    patterns = Counter()
    for i in range(max_length):
        for seq in seqs:
            new_seq = []
            for char_idx in range(len(seq) - i):  
                pattern = ''
                for k in range(i+1):                
                    pattern += seq[char_idx + k]              
                new_seq.append(pattern)
            patterns.update(set(new_seq))
    
    not_enough = [p for p in patterns if patterns[p] < f * len(seqs)]
    for i in not_enough:
        del patterns[i]
    return +patterns 


print(seq_mining(['ABCD', 'ABABC', 'BCAABCD'], 0.34, 1000000))